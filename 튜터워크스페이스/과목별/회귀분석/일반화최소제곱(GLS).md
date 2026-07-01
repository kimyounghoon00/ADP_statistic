---
aliases: [GLS, 일반화최소제곱, Generalized Least Squares, Aitken 추정량, 표백변환]
subject: 회귀분석
chapter: "일반 GLS는 교재 외 — 교재상 대각 특수경우 WLS가 §6.3 가중최소제곱법(Ch6 변환, p253-254)"
concept: '[[일반화최소제곱(GLS)]]'
cluster:
- 추정법
- 효율성
- 오차구조
tags:
- 회귀분석
- GLS
- 일반화최소제곱
- BLUE
- 표백변환
- Aitken
- 효율성
cross_ref:
- '[[Gauss-Markov 정리]] (V=I 가정 → GLS가 일반화)'
- '[[회귀계수의 분산 유도]] (샌드위치 분산)'
- '[[Durbin-Watson 검정]] · [[Breusch-Godfrey 검정]] (독립성 \"진단\" → GLS는 \"처방\")'
- '[[Breusch-Pagan 검정]] (등분산 진단 → WLS 처방)'
- '[[Cholesky 분해]] / [[Aitken 정리]]'
date_created: "2026-06-28"
date_modified: "2026-06-29"
status: "백지유도 통과 — LSE 붕괴→표백→GLS 공식"
---

# [[일반화최소제곱(GLS)]] — 오차가 $\sigma^2 I$ 가 아닐 때의 BLUE

> **진단 vs 처방 (이 노트의 위치)**: [[Durbin-Watson 검정]]·[[Breusch-Godfrey 검정]]은 독립성 위반을 *탐지*하는 **진단**, [[Breusch-Pagan 검정]]은 등분산 위반 *진단*. 이 노트의 GLS는 그 위반을 *교정*하는 **처방(추정법)**이다. 진단은 Ch4 회귀진단, 처방은 여기.

> **한 줄 핵심**: 오차를 *표백(whitening)* 해 Gauss-Markov 세계로 되돌린 뒤 OLS를 적용. 결과: $\hat{\boldsymbol\beta}_{GLS}=(X'V^{-1}X)^{-1}X'V^{-1}\mathbf y$.

> [!info] 📖 교재 위치 (2026-06-29 PDF 대조)
> 김충락·강근석 『회귀분석』 2판에 **"일반화최소제곱(GLS)"·Aitken 정리는 미수록** (색인에 generalized least squares·Aitken 항목 없음). 교재가 비-$\sigma^2 I$ 를 다루는 본문은 **§6.3 가중최소제곱법(WLS)** — 책 253–254쪽(제6장 변환). 거기선 $\text{Cov}(\boldsymbol\varepsilon)=\sigma^2 W^{-1}$($W$ 대각)에 $P^2=W$ 변환으로 $\hat{\boldsymbol\beta}=(X'WX)^{-1}X'W\mathbf y$ 를 얻는다. **본 노트의 일반 $V$ GLS = 그 일반화**($W=V^{-1}$: 대각 → 임의 양정치). 표백변환 $P'P=V^{-1}$ 도 교재의 $P^2=W$($W$ 대각, $P=\sqrt W$)와 동일 구조. [[Gauss-Markov 정리]]·BLUE는 Ch2(p55). → [[가중최소제곱(WLS)]]

---

## 1. 동기 — $\text{Cov}(\boldsymbol\varepsilon)\neq\sigma^2 I$

독립성(자기상관) 또는 등분산성이 깨지면 오차 공분산이 $\sigma^2 I$ 가 아니다:
$$\text{Cov}(\boldsymbol\varepsilon)=\sigma^2 V,\qquad V\neq I$$
- 자기상관 → $V$ 의 **비대각**이 0이 아님 (이웃 오차 상관)
- 이분산 → $V$ 의 **대각**이 서로 다름

---

## 2. 이때 [[최소제곱추정량(LSE)]]에 무슨 일이 — 무엇이 살고 무엇이 죽나

$\hat{\boldsymbol\beta}=\boldsymbol\beta+(X'X)^{-1}X'\boldsymbol\varepsilon$ 에서:

**① 불편성: 살아남음 ✅**
$$E[\hat{\boldsymbol\beta}]=\boldsymbol\beta+(X'X)^{-1}X'\,E[\boldsymbol\varepsilon]=\boldsymbol\beta$$
**오직 $E[\boldsymbol\varepsilon]=\mathbf 0$ 에만 의존.** 공분산 구조($V$)는 1차 적률 계산에 끼어들 자리가 없으므로 $V\neq I$ 여도 불편.

**② 분산: 공식이 바뀜 ❌ (샌드위치)**
$A=(X'X)^{-1}X'$ 로 두면 $\text{Var}(\hat{\boldsymbol\beta})=A(\sigma^2V)A'$:
$$\text{Var}(\hat{\boldsymbol\beta})=\sigma^2(X'X)^{-1}\underbrace{X'VX}_{\text{약분 안 됨}}(X'X)^{-1}$$
- $V=I$ → 가운데 $X'IX=X'X$ → $\sigma^2(X'X)^{-1}$ 로 **붕괴**(약분).
- $V\neq I$ → $X'VX\neq X'X$ → 샌드위치 잔존. **우리가 외워 쓰던 $\sigma^2(X'X)^{-1}$ 은 틀린 분산.**

**두 가지 붕괴**:
- (분산추정/추론) 소프트웨어가 보고하는 SE·$t$·신뢰구간이 틀린 공식 기반 → **무효**.
- (효율성) [[Gauss-Markov 정리]]는 $\text{Cov}=\sigma^2 I$ 가정 위에서만 LSE=BLUE 보장. $V\neq I$ 면 그 보장 소멸 → **LSE보다 분산 작은 선형불편추정량이 존재**(=GLS).

---

## 3. GLS 아이디어 — 표백(whitening) 변환

문제의 원인이 $\text{Cov}=\sigma^2V$ 라면, 모형을 변환해 오차 공분산을 다시 $\sigma^2 I$ 로 되돌리자. 모형 양변에 행렬 $P$ 를 곱하면:
$$P\mathbf y = PX\boldsymbol\beta + P\boldsymbol\varepsilon,\qquad \text{Cov}(P\boldsymbol\varepsilon)=\sigma^2 PVP'$$
원하는 건 $PVP'=I$. 정리하면:
$$PVP'=I \iff V=(P'P)^{-1} \iff \boxed{P'P=V^{-1}}$$
$V$ 가 **대칭 양의 정부호**(공분산행렬)이므로 $V^{-1}$ 도 그러하고, 그런 제곱근 $P$($\approx V^{-1/2}$)가 항상 존재 ([[Cholesky 분해]]). — "양수는 제곱근을 갖는다"의 행렬판.

(스칼라 직관: 분산이 $\sigma^2 v$ 면 $1/\sqrt v$ 를 곱해 표준화. $P$ 는 그 행렬판.)

---

## 4. GLS 공식 유도

변환 모형 $\mathbf y^*=P\mathbf y,\ X^*=PX$ 는 $\text{Cov}(\boldsymbol\varepsilon^*)=\sigma^2 I$ 라 Gauss-Markov 만족 → OLS 적용:
$$\hat{\boldsymbol\beta}_{GLS}=(X^{*\prime}X^*)^{-1}X^{*\prime}\mathbf y^*$$
두 조각을 따로 계산하고 $P'P=V^{-1}$ 대입:
$$X^{*\prime}X^*=X'\underbrace{P'P}_{V^{-1}}X=X'V^{-1}X,\qquad X^{*\prime}\mathbf y^*=X'\underbrace{P'P}_{V^{-1}}\mathbf y=X'V^{-1}\mathbf y$$
$$\boxed{\ \hat{\boldsymbol\beta}_{GLS}=(X'V^{-1}X)^{-1}X'V^{-1}\mathbf y\ }$$

- **$V=I$ → OLS** $(X'X)^{-1}X'\mathbf y$. 즉 **OLS는 GLS의 특수경우.**
- [[Aitken 정리]]: $V\neq I$ 에서 $\hat{\boldsymbol\beta}_{GLS}$ 이 진짜 BLUE.
- GLS의 (옳은) 분산: $\text{Var}(\hat{\boldsymbol\beta}_{GLS})=\sigma^2(X'V^{-1}X)^{-1}$.

---

## 5. ⚠️ 이번 세션에 자주 틀린 부분

> 다음에 다시 유도할 때 여기부터 읽을 것.

1. **불편성 증명에 공분산 가정이 필요하다고 착각 ❌**
   → 불편성은 $E[\boldsymbol\varepsilon]=\mathbf 0$ **하나에만** 의존. $\text{Cov}$ 는 무관. ($V\neq I$ 여도 불편 유지, 무너지는 건 분산뿐.)
2. **$\big((PX)'(PX)\big)^{-1}=(PX)^{-1}\big((PX)'\big)^{-1}$ 로 쪼갬 ❌ (가장 치명적)**
   → $X$ 는 $n\times p$ ($n>p$), **정사각 아님 → $X^{-1}$ 없음.** $(X'X)^{-1}$ 만 가역. $(X^{*\prime}X^*)^{-1}$ 은 **통째로** 두고 $P'P=V^{-1}$ 만 꽂을 것.
3. **추정량 식에 $+\boldsymbol\varepsilon^*$ 를 붙임 ❌** → 그건 적합값/모형식 얘기. 추정량은 $\hat{\boldsymbol\beta}=(X^{*\prime}X^*)^{-1}X^{*\prime}\mathbf y^*$ 뿐.

---

## 6. 실전 변형 (한눈에)

| 상황 | $V$ 구조 | 처방 |
|---|---|---|
| 이분산 (독립) | 대각, 원소 상이 | **WLS** (가중최소제곱, GLS의 대각 특수경우) |
| 자기상관 AR(1) | 비대각 (밴드) | GLS / Cochrane–Orcutt, Prais–Winsten |
| $V$ 미지 | 추정해야 | **FGLS** (feasible GLS): $\hat V$ 로 GLS — $V$ 를 자료에서 먼저 추정 |

---

## 7. 계산 예시 (기본 R) — 공식 그대로

$V$ 를 안다고 가정하면 GLS는 base R 행렬연산만으로 계산된다 (유도식 직접 확인):

```r
# X, y, V (n×n 오차공분산) 가 주어졌을 때
Vinv <- solve(V)
beta_gls <- solve(t(X) %*% Vinv %*% X) %*% t(X) %*% Vinv %*% y   # (X'V^{-1}X)^{-1} X'V^{-1} y
# V = I 이면 위 식은 정확히 OLS = solve(t(X)%*%X) %*% t(X)%*%y 로 환원

# V를 모를 때(현실): AR(1) 오차 등은 nlme::gls 가 FGLS 수행
# library(nlme); gls(y ~ x, correlation = corAR1())   # (패키지 필요)
```

---

## 정리노트 가이드 (Obsidian)
```yaml
---
aliases: [GLS, 일반화최소제곱, Aitken 추정량]
tags: [회귀분석, GLS, BLUE, 표백변환]
---
```

## 다음 할 것
- [ ] [[Aitken 정리]] 백지유도: GLS가 BLUE임을 Gauss-Markov 증명에 표백변환을 얹어 보이기
- [ ] WLS 별도 정리 (이분산 → 가중치 $w_i=1/\sigma_i^2$)
- [ ] FGLS의 2단계 절차 ($\hat V$ 추정 → GLS) 와 일치성 조건
- [ ] Ch4 잔차진단(정규성·등분산·독립성·영향점) MOC + "진단→처방(WLS/GLS)" 연결도
