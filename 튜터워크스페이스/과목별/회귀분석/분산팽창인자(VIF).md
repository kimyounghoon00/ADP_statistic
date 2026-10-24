---
aliases: [VIF, variance inflation factor, 분산팽창계수]
tags: [회귀분석, 7장, 진단, 다중공선성]
chapter: ["제7장 편의추정법"]
book_pages: "275-300"
moc: ["[[MOC_추정효율성]]"]
date_created: 2026-08-21
status: 정착
status_note: "유도+사용예 완료"
---

# 분산팽창인자 (VIF)

> [!info] 📖 교재 위치 · 커리큘럼
> 제7장 편의추정법 (책 275–300쪽) — 다중공선성 진단 지표. 커리큘럼: [[MOC_추정효율성]] 가지 ④ 편의를 허용한 효율.

> [!definition] 정의
> $j$번째 설명변수의 분산팽창인자
> $$\text{VIF}_j=\frac{1}{1-R_j^2}$$
> 여기서 $R_j^2$ 는 $x_j$ 를 나머지 설명변수들에 회귀시켰을 때의 결정계수.

## 유도 — $R_j^2$ 는 왜 $(X^\top X)^{-1}$ 의 대각 원소를 결정하는가

**출발점**: [[Gauss-Markov 정리]] 에서 $\text{Cov}(\hat\beta)=\sigma^2(X^\top X)^{-1}$. 즉 $\hat\beta_j$ 의 분산을 알려면 $(X^\top X)^{-1}$ 의 $j$번째 대각 원소만 있으면 된다. 이걸 $R_j^2$ 로 표현하는 것이 목표.

**1단계 — 설계행렬을 $j$번째 변수와 나머지로 블록 분할**
$$
X=\begin{bmatrix}X_{-j} & x_j\end{bmatrix},\qquad
X^\top X=\begin{bmatrix}X_{-j}^\top X_{-j} & X_{-j}^\top x_j\\ x_j^\top X_{-j} & x_j^\top x_j\end{bmatrix}
$$
(모든 변수는 중심화되어 있다고 가정 — 절편은 이미 제거, $\text{SST}_j=x_j^\top x_j$.)

**2단계 — 블록행렬 역행렬의 (우하단) 원소 (Schur complement)**
2×2 블록행렬의 역행렬 공식에서, 우하단 스칼라 블록의 역원은
$$
\big[(X^\top X)^{-1}\big]_{jj}=\Big(x_j^\top x_j - x_j^\top X_{-j}(X_{-j}^\top X_{-j})^{-1}X_{-j}^\top x_j\Big)^{-1}=\big(x_j^\top M_{-j}\,x_j\big)^{-1}
$$
여기서 $M_{-j}=I-X_{-j}(X_{-j}^\top X_{-j})^{-1}X_{-j}^\top$ 는 $\text{col}(X_{-j})$ 로의 사영을 걷어내는 행렬 — [[Ch04_잔차가정검정_백지유도]] 에서 쓴 hat matrix $H$ 와 정확히 같은 구조($M_{-j}=I-H_{-j}$).

**3단계 — $x_j^\top M_{-j} x_j$ 를 $R_j^2$ 로 표현**
$x_j$ 를 $X_{-j}$ 에 회귀시킨 보조회귀를 생각하면
$$
x_j^\top M_{-j} x_j = \underbrace{x_j^\top x_j}_{\text{SST}_j} - \underbrace{x_j^\top X_{-j}(X_{-j}^\top X_{-j})^{-1}X_{-j}^\top x_j}_{\text{SSR}_j\ (\text{보조회귀의 설명제곱합})} = \text{SST}_j-\text{SSR}_j=\text{SST}_j(1-R_j^2)
$$
($\text{SSR}_j/\text{SST}_j=R_j^2$ 는 보조회귀의 결정계수 그 자체.)

**4단계 — 결합**
$$
\big[(X^\top X)^{-1}\big]_{jj}=\frac{1}{\text{SST}_j(1-R_j^2)}
\;\;\Longrightarrow\;\;
\text{Var}(\hat\beta_j)=\sigma^2\big[(X^\top X)^{-1}\big]_{jj}=\underbrace{\frac{\sigma^2}{\text{SST}_j}}_{\text{공선성 없을 때 분산}}\times\underbrace{\frac{1}{1-R_j^2}}_{=\,\text{VIF}_j}
$$

**해석**: $\sigma^2/\text{SST}_j$ 는 $x_j$ 가 다른 변수와 완전히 무관($R_j^2=0$)할 때의 "기저 분산". VIF는 이 기저 분산에 곱해지는 **배율**이다.

**5단계 — 표준화 특수 케이스 (자주 쓰는 형태)**
모든 $x_j$ 를 평균 0, 분산 1로 표준화하면 $\text{SST}_j=1\;\forall j$ 이고 $X^\top X=$ 상관행렬 $R$. 이때
$$
\text{VIF}_j=\big[(X^\top X)^{-1}\big]_{jj}=\big[R^{-1}\big]_{jj}
$$
즉 **표준화된 설계행렬에서는 VIF가 상관행렬 역행렬의 대각원소와 정확히 같다.**

## 의미

- $x_j$ 가 다른 설명변수들로 잘 설명될수록($R_j^2\to 1$) $\text{VIF}_j\to\infty$ → [[다중공선성]] 심각.
- $\hat{\beta}_j$ 의 분산이 "공선성이 없을 때 대비 몇 배 부풀려졌는가"를 나타냄.
- 경험칙: $\text{VIF}_j>10$ (혹은 $>5$)이면 공선성 의심.

## 뿌리

VIF가 재는 것도 결국 고정행렬 $X^\top X$ 의 비대각 구조다 — 확률이 아닌 결정론적 양. → [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]]

## 사용예 — `longley` 데이터 (R, 다중공선성의 고전적 예시)

```r
library(car)
data(longley)
fit <- lm(Employed ~ ., data = longley)
vif(fit)
```

```
GNP.deflator          GNP   Unemployed Armed.Forces   Population         Year
      135.53      1788.51        33.62         3.59       399.15       758.98
```

**수기 검증** (보조회귀 $R_j^2$ 를 직접 계산해 $\text{VIF}_j=1/(1-R_j^2)$ 로 복원):

| 변수 | $R_j^2$ | $\text{VIF}_j=1/(1-R_j^2)$ |
|---|---|---|
| GNP.deflator | 0.9924 | 130.8 |
| GNP | 0.9984 | 639.1 |
| Unemployed | 0.9073 | 10.8 |
| Armed.Forces | 0.6009 | 2.5 |
| Population | 0.9971 | 339.0 |

(패키지 `vif()`가 `Year`까지 포함한 6변수 기준이라 값이 정확히 일치하진 않지만 — GNP·Population이 압도적으로 크다는 패턴은 동일. 5단계에서 유도한 항등식을 직접 확인하려면:)

```r
Xs <- scale(as.matrix(longley[,1:5]))          # 평균0·분산1 표준화
diag(solve(t(Xs) %*% Xs)) * (nrow(Xs) - 1)     # (X'X)^-1 대각 * (n-1) = VIF
```
```
GNP.deflator          GNP   Unemployed Armed.Forces   Population
      130.83       639.05        10.79         2.51       339.01
```
→ 5단계에서 유도한 $\text{VIF}_j=[(X^\top X)^{-1}]_{jj}$ (표준화 스케일) 가 수기 계산과 정확히 일치. GNP와 Population의 상관이 0.99에 달해 (첫 상관행렬 참고) VIF가 수백대까지 폭발 — 이 데이터가 [[주성분회귀(PCR)]] 의 대표 예시로 쓰이는 이유.

## 관련 노트
- [[다중공선성]]
- [[Gauss-Markov 정리]]
- [[주성분회귀(PCR)]] — VIF로 진단된 공선성을 구조적으로 제거하는 처방
- [[Ch04_잔차가정검정_백지유도]] — 사영행렬 $M=I-H$ 가 이 유도의 2단계에 재등장
