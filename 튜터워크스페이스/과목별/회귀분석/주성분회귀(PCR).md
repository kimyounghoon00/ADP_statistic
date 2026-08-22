---
aliases: [PCR, principal component regression, 주성분회귀, 주성분분석, PCA]
tags: [회귀분석, 7장, 편의추정, 다중공선성]
chapter: ["제7장 편의추정법 (능형회귀 인접 절 추정 — 교재 목차 상 정확한 절 번호 미확인)"]
book_pages: "미확인"
moc: ["[[MOC_추정효율성]]"]
date_created: 2026-08-21
status: 유도+사용예 완료
---

# 주성분회귀 (Principal Component Regression, PCR)

> [!info] 📖 위치 · 커리큘럼
> [[다중공선성]] 의 대처법 중 하나. 편의(bias)를 대가로 분산을 줄이는 방법이라는 점에서 [[Gauss-Markov 정리]] 의 BLUE(불편 조건)를 의도적으로 깨는 부류 — 커리큘럼: [[MOC_추정효율성]] 가지 ④ 편의를 허용한 효율.

> [!definition] 정의
> 설계행렬 $X$ (열은 중심화·표준화됨) 의 $X^\top X$ 를 고유분해해 얻은 **서로 직교하는** 선형결합(주성분) $Z=XV$ 중 일부를 새 설명변수로 삼아 $y$ 를 회귀하는 방법.

---

## 유도 1 — 주성분은 왜 서로 직교하는가

**출발**: $S=X^\top X$ 는 대칭행렬(표준화하면 상관행렬 $R$과 같음) → 스펙트럼 정리에 의해 항상
$$
S=V\Lambda V^\top,\qquad V^\top V=VV^\top=I,\qquad \Lambda=\text{diag}(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_p\ge0)
$$
로 분해된다 ($V$의 열 $v_k$ = 고유벡터/적재벡터, $\lambda_k$ = 고유값).

**주성분 정의**: $Z=XV$, 즉 $k$번째 주성분 $z_k=Xv_k$ (원래 변수들의 선형결합).

**직교성 증명** — $Z^\top Z$ 를 직접 계산:
$$
Z^\top Z=(XV)^\top(XV)=V^\top X^\top X V=V^\top S V=V^\top(V\Lambda V^\top)V=(V^\top V)\Lambda(V^\top V)=\Lambda
$$
($V^\top V=I$ 두 번 사용.) **$Z^\top Z$ 가 대각행렬** — 이것이 정확히 "주성분끼리 무상관(직교)"라는 뜻이며, 대각원소 $\lambda_k$ 는 $k$번째 성분의 (제곱합으로 잰) 분산이다.

> 이 한 줄 $Z^\top Z=\Lambda$ 이 PCR 전체 아이디어의 뿌리다. [[분산팽창인자(VIF)]] 유도에서 쓴 $x_j^\top M_{-j}x_j$ 처럼, 여기서도 "행렬을 어떻게 분해하면 대각(=직교)이 되는가"가 핵심 질문이다.

## 유도 2 — 원래 회귀모형과의 관계 (재모수화일 뿐)

$V$가 직교행렬이므로 $VV^\top=I$, 따라서 $X=XVV^\top=ZV^\top$. 원래 모형에 대입:
$$
X\beta=(ZV^\top)\beta=Z\underbrace{(V^\top\beta)}_{=:\gamma}=Z\gamma
$$
즉 $\gamma=V^\top\beta \Longleftrightarrow \beta=V\gamma$ ($V^{-1}=V^\top$ 이므로).

**중요한 사실**: $p$개 주성분을 **전부** 써서 $y$ 를 $Z$ 에 OLS로 적합하면, $X\beta$ 와 $Z\gamma$ 는 같은 열공간 $\text{col}(X)=\text{col}(Z)$ 위의 같은 적합값을 준다 — 즉 전부 사용한 PCR = 원래 OLS를 좌표만 바꿔 쓴 것과 완전히 동일 ($R^2$, 적합값 불변). PCR이 실제로 "다른" 결과를 주는 것은 **일부 성분을 버릴 때**뿐이다.

## 유도 3 — 다중공선성이 어떻게 제거되는가

$Z$로 OLS를 하면 Gauss–Markov 공식이 그대로 적용된다:
$$
\text{Cov}(\hat\gamma)=\sigma^2(Z^\top Z)^{-1}=\sigma^2\Lambda^{-1}=\sigma^2\,\text{diag}(1/\lambda_1,\dots,1/\lambda_p)
$$
- **비대각이 정확히 0** → $\hat\gamma_k$ 들끼리 공분산 0, VIF는 전부 정확히 1 (완전 직교 설계이므로). [[분산팽창인자(VIF)]] 유도의 5단계($\text{VIF}_j=[(X^\top X)^{-1}]_{jj}$)를 이 좌표계에 적용하면 자명하게 1이 나오는 구조다.
- 하지만 **$\lambda_k$가 작으면 $\hat\gamma_k$의 분산 $\sigma^2/\lambda_k$ 는 오히려 폭발**한다. 다중공선성이 있다는 것 자체가 "어떤 방향(작은 $\lambda_k$의 고유벡터 방향)으로는 $X$가 정보를 거의 담고 있지 않다"는 뜻이기 때문 — 원래 변수 좌표계에서의 VIF 폭발이, 회전만 시켰을 뿐인 이 좌표계에서는 "그 방향 성분의 극단적으로 큰 분산"으로 고스란히 옮겨간 것.
- **PCR의 처방**: $\lambda_k$가 작은(=원래 변수들이 "거의 선형종속"인 방향) 뒤쪽 성분들을 통째로 버리고 $k<p$개만 사용 → 그 방향의 극단적 분산을 원천 차단. 대신 그 방향에 $y$와 관련된 정보가 있었다면 편의(bias)가 생긴다 — **분산-편의 트레이드오프**.

## 성분 개수 $k$ 선택

- **누적기여율**: $(\lambda_1+\cdots+\lambda_k)/\sum_i\lambda_i \ge$ 80~90%
- **스크리도표**: $\lambda_k$ vs $k$ 그림의 팔꿈치(elbow)
- **Kaiser 기준**: 표준화(상관행렬) 시 $\text{tr}(R)=p=\sum\lambda_i$ 이므로 평균 고유값 = 1. $\lambda_k>1$ 인 성분만 채택.
- **조건수와의 관계**: $\kappa=\sqrt{\lambda_{\max}/\lambda_{\min}}$ — [[다중공선성]] 진단에 쓰는 조건수가 바로 이 고유값들로 정의됨. $\kappa>30$ 이면 심각한 공선성.

## 한계

- $Z=XV$ 는 **$y$를 전혀 보지 않고** $X$만으로 정해짐 → 분산은 크지만($\lambda_k$ 작음) $y$ 예측에 결정적인 성분이 뒤쪽으로 밀려 버려질 위험. (이 결함을 보완해 $\text{Cov}(X,y)$까지 반영해 성분을 뽑는 것이 PLS, Partial Least Squares.)
- 주성분은 원래 변수들의 선형결합이므로 $\hat\gamma_k$ 개별 계수의 실질적 해석이 어려움 → 최종 보고 시엔 $\hat\beta=V_k\hat\gamma_k$ 로 원래 변수 스케일로 되돌리는 경우가 많음(사용예 참고).

---

## 사용예 — `longley` 데이터 (R)

`longley`는 GNP·Population·연도 등이 서로 0.98~0.99대로 상관된 다중공선성의 고전적 예시([[분산팽창인자(VIF)]] 노트에서 VIF가 수백~수천까지 폭발한 바로 그 데이터).

```r
X  <- as.matrix(longley[, 1:5])   # GNP.deflator, GNP, Unemployed, Armed.Forces, Population
pc <- prcomp(X, scale. = TRUE)    # 표준화 후 상관행렬 고유분해
```

**1) 고유값과 누적기여율**
```
lambda:       3.610   1.175   0.199   0.015   0.001
누적기여율:   72.2%   95.7%   99.7%   100.0%  100.0%
```
→ 조건수 $\kappa=\sqrt{3.610/0.001}\approx 61.5$ (경험적 심각 기준 30을 두 배 초과).

**2) 적재행렬 $V$ (고유벡터)**
```
               PC1    PC2    PC3    PC4    PC5
GNP.deflator  0.521  0.058  0.189 -0.777  0.293
GNP           0.520  0.053  0.317  0.136 -0.779
Unemployed    0.366 -0.595 -0.710 -0.005 -0.087
Armed.Forces  0.230  0.798 -0.551  0.079 -0.003
Population    0.521 -0.045  0.236  0.610  0.547
```
PC1의 적재값이 GNP.deflator·GNP·Population 모두에서 비슷하게 큼(≈0.52) — "경제규모" 방향 하나로 세 변수가 뭉쳐 있다는 뜻, 이게 바로 다중공선성의 실체.

**3) 직교성 검증** ($Z^\top Z$, 비대각이 정확히 0인지)
```
      PC1   PC2    PC3    PC4     PC5
PC1  54.15  0     0      0       0
PC2   0    17.63  0      0       0
PC3   0     0     2.987  0       0
PC4   0     0     0      0.223   0
PC5   0     0     0      0       0.014
```
→ 유도 1의 $Z^\top Z=\Lambda$ 가 정확히 재현됨(대각원소 $=(n-1)\lambda_k=15\lambda_k$).

**4) PCR — 성분 개수 $k$에 따른 원 변수 스케일 회귀계수 $\hat\beta=V_k\hat\gamma_k$**

```r
Z <- pc$x
for (k in c(2,3,5)) {
  fit_k   <- lm(longley$Employed ~ Z[,1:k])
  gamma_k <- coef(fit_k)[-1]
  beta_k  <- pc$rotation[,1:k] %*% gamma_k     # 표준화 스케일로 역변환
}
```

| $k$ | 누적기여율 | GNP.deflator | GNP | Unemployed | Armed.Forces | Population | $R^2$ |
|---|---|---|---|---|---|---|---|
| 2 | 95.7% | 0.939 | 0.935 | 0.409 | 0.717 | 0.898 | 0.919 |
| 3 | 99.7% | 1.316 | 1.568 | −1.007 | −0.383 | 1.369 | 0.983 |
| 5 (전체) | 100.0% | −0.523 | 7.157 | −0.377 | −0.390 | −2.807 | 0.987 |

**읽는 법**:
- $k=5$(전체 사용, 유도 2에서 증명했듯 원래 OLS와 동일 모형)에서는 GNP 계수가 7.16으로 부호·크기가 요동 — 바로 VIF 639에 해당하는 극단적 불안정성이 표준화 계수로 나타난 것.
- $k=2,3$처럼 작은 $\lambda_k$ 방향(잡음성 공선성 방향)을 버리면 계수가 훨씬 안정적이고 부호가 직관과 맞음(모든 변수가 양의 영향) — 대신 $R^2$가 0.987→0.919로 소폭 하락(=버린 방향에 실렸던 정보의 손실=편의).
- $k$ 선택은 이 "분산 안정화" 이득과 "정보 손실" 비용의 균형점 — 누적기여율 95~99% 부근이 관행적 절충점.

## 관련 노트
- [[다중공선성]]
- [[분산팽창인자(VIF)]] — 같은 데이터, 같은 $X^\top X$ 구조를 진단 vs 처방의 관점에서 봄
- [[Gauss-Markov 정리]] — PCR이 의도적으로 포기하는 불편성(BLUE) 조건
