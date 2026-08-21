---
subject: 회귀분석
chapter: Ch4 회귀진단
concept: "[[Breusch-Pagan 검정]]"
aliases: [BP 검정, 등분산성 검정, Breusch-Pagan, 이분산 검정, 보조회귀 검정]
cluster: [B, E]
cross_ref:
  - "김충락·강근석 『회귀분석』 2판 — 제4장 회귀진단"
  - "Breusch & Pagan (1979), Econometrica 47(5), 1287–1294"
  - "Koenker (1981) — 스튜던트화(robust) 버전"
tags: [회귀분석, 4장, 회귀진단, 등분산성, 이분산, BreuschPagan, 보조회귀, LM검정, ClusterB, ClusterE]
date_created: 2026-06-23
status: 완료
date_modified: 2026-08-21
---

# [[Breusch-Pagan 검정]] — Ch4 등분산성 검정

> **목표**: 막연한 가설 "오차의 분산이 일정하다"를 검정 가능한 모수 제약으로 번역하고,
> 잔차 제곱을 보조회귀에 돌려 $nR^2 \sim \chi^2_q$ 검정통계량을 유도한다.

## 핵심 아이디어 — 한 줄 사슬

$$
\underbrace{H_0:\mathrm{Var}(\varepsilon_i)=\sigma^2}_{\text{막연}}
\;\to\; \mathrm{Var}(\varepsilon_i)=\sigma^2 g(z_i^\top\alpha)
\;\to\; \underbrace{H_0:\alpha=0}_{\text{검정가능}}
\;\to\; e_i^{\,2}\ \text{프록시}
\;\to\; \text{보조회귀}\ e_i^2\sim z_i
\;\to\; nR^2\sim\chi^2_q
$$

## 유도 과정

### 1. 귀무가설 — 주어는 잔차가 아니라 *오차*
등분산성의 대상은 잔차 $e_i$ 가 **아니라** 오차 $\varepsilon_i$ 다.
[[잔차 가정 검정 (정규성·등분산성·독립성)]] Section 0에서 보았듯, 모형이 완벽해도
$$
\mathrm{Var}(e_i)=\sigma^2(1-h_{ii})
$$
라 잔차는 *원래* 등분산이 아니다. 검정·가정의 주어는 오차다.
$$
H_0:\ \mathrm{Var}(\varepsilon_i)=\sigma^2\quad(\forall i,\ \text{일정})
$$

### 2. 검정 가능하게 — 분산을 모수화
"일정하지 않다면 어떻게?"를 못 박아야 분포가 나온다. 보조변수 벡터
$z_i=(1, z_{i1},\dots,z_{iq})$ (흔히 회귀변수 $x_i$ 자신 또는 적합값 $\hat y_i$)의 함수로 둔다:
$$
\mathrm{Var}(\varepsilon_i)=\sigma^2\, g(z_i^\top\alpha),\qquad g>0\ \text{매끄러움},\ g(0)=1\ (\text{예: } g(t)=e^t)
$$
등분산 $\Leftrightarrow$ $g(z_i^\top\alpha)$ 가 모든 $i$ 에서 상수 $1$ $\Leftrightarrow$ $z_i^\top\alpha=0\ (\forall i)$.
관측치마다 $z_i$ 가 다른 방향이므로, **고정된 $\alpha$** 가 그 모두와 동시에 직교하려면 $\alpha$ 는 영벡터뿐:
$$
\boxed{H_0:\ \alpha=0}\quad\text{vs}\quad H_1:\ \alpha\ne 0
$$
([[일반선형가설의 F 통계량 도출]] 의 "막연한 가설 → 모수 제약" 번역과 동일 정신.)

### 3. 분산의 프록시 — 잔차 *제곱*
$\mathrm{Var}(\varepsilon_i)$ 도, $\varepsilon_i$ 도 직접 관측 못 한다. 다리:
$$
\mathrm{Var}(\varepsilon_i)=E[\varepsilon_i^2]-(E[\varepsilon_i])^2=E[\varepsilon_i^2]
$$
기댓값 $E[\varepsilon_i^2]$ 의 "관측치 1개짜리" 추정값은 $\varepsilon_i^2$ 그 값. 다시 $\varepsilon_i\to e_i$ 대체:
$$
\mathrm{Var}(\varepsilon_i)=E[\varepsilon_i^2]\approx E[e_i^2]\ \xrightarrow{\text{관측치 1개}}\ e_i^{\,2}\ (\text{우리가 쥔 데이터})
$$
> ⚠️ 두 고비: ① 주어를 **오차**로, ② 분산은 못 보니 $e_i^2$ 로 대체하되 **제곱** 잊지 말 것.

### 4. 보조회귀 (auxiliary regression)
$H_0$ 면 $E[e_i^2]$ 수준이 $z_i$ 와 무관, $H_1$ 이면 $z_i$ 에 따라 체계적으로 변함.
이를 수치화하려면 $e_i^2$ 를 종속변수로 회귀를 한 번 더 돌린다:
$$
e_i^{\,2}=\gamma_0+\gamma_1 z_{i1}+\cdots+\gamma_q z_{iq}+(\text{오차})
$$
- $H_0\Rightarrow \gamma_1=\cdots=\gamma_q=0 \Rightarrow R^2_{\text{aux}}\approx 0$
- $H_1\Rightarrow z_i$ 가 $e_i^2$ 를 설명 $\Rightarrow R^2_{\text{aux}}$ 커짐 $\Rightarrow$ 등분산 기각

> **절편 $\gamma_0$ 의 역할 (필수 구조물)**: 등분산일 때 분산은 0이 아닌 *상수* $\sigma^2$.
> 절편을 빼면 $\gamma_1=\cdots=\gamma_q=0$ 이 곧 "분산$=0$"이라는 엉뚱한 가설이 됨.
> 따라서 $\gamma_0$ 는 0이 아닌 공통 분산 수준을 담는 자리 → **항상 두고, 검정(자유도)에서는 뺀다.**

### 5. 검정통계량
$R^2$ 는 분포를 모르니 증가함수이면서 알려진 영분포를 갖는 LM 통계량으로:
$$
\boxed{\text{BP}=nR^2_{\text{aux}}\ \xrightarrow{\ d\ }\ \chi^2_{q}\quad(\text{under }H_0)}
$$
- **자유도 $q$** = $H_0$ 에서 0으로 묶은 기울기 개수 ($\gamma_1,\dots,\gamma_q$). 절편은 안 셈.
  - $z_i=x_i$ 전체 → $q=p-1$ (절편 제외 설명변수 수)
  - $z_i=\hat y_i$ 하나 → $q=1$ (원논문의 단순형)
- Koenker 스튜던트화 버전 = $nR^2$ (비정규성에 강건).
  원 Breusch–Pagan 은 정규성 가정하 $\tfrac12\,\mathrm{ESS}/\hat\sigma^4$ — 같은 점근분포.

## 막혔던 포인트 & 튜터 힌트
- **주어 혼동**: 처음 "잔차의 분산이 등분산"이라 적음 → 잔차는 $\sigma^2(1-h_{ii})$ 라 원래 비등분산. 주어를 **오차**로 교정.
- **프록시의 제곱 누락**: $\mathrm{Var}=E[\varepsilon^2]$ 이므로 한 점 추정값은 $\varepsilon_i$ 가 아니라 $\varepsilon_i^2$ → $e_i^2$.
- **직교 함정**: "$\alpha$ 가 $z_i$ 와 직교?" → 직교는 *하나의* $z_i$ 얘기. *모든* $i$ 에서 동시에 성립 → $\alpha=0$ 뿐.
- **자유도 $q$ vs $q-1$**: "0으로 안 묶음"="자유롭게 추정"이지 "0이라 가정"이 아님. "$-1$"은 절편을 빼는 것이고, $\gamma_1,\dots,\gamma_q$ 는 이미 기울기만 $q$ 개 → 또 빼면 절편 이중 차감. df $=q$.

## 연결 개념
- 🗺️ 허브: [[MOC_이차형식]] · 가지 ⑤ (회귀진단 잔차 가정 검정)
- [[잔차 가정 검정 (정규성·등분산성·독립성)]] — Section 2 본체 (이 노트는 그 정리본)
- [[Hat Matrix의 멱등성 및 대칭성]] — $\mathrm{Var}(e)=\sigma^2(I-H)$ 의 토대
- [[일반선형가설의 F 통계량 도출]] — "막연한 가설 → 모수 제약" 번역의 동형
- [[Durbin-Watson 통계량 유도]] — Section 3 독립성 검정 (다음 단계)

## 참고 교재 페이지
- 김충락·강근석 『회귀분석』 2판, 제4장 회귀진단.
- Breusch, T. & Pagan, A. (1979). "A Simple Test for Heteroscedasticity and Random Coefficient Variation." *Econometrica* 47(5), 1287–1294.
- Koenker, R. (1981). "A Note on Studentizing a Test for Heteroscedasticity." *Journal of Econometrics* 17(1), 107–112.
