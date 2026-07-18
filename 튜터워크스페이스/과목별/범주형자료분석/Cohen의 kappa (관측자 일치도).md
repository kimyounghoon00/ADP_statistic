---
subject: 범주형자료분석
chapter: "Agresti 3e Ch11 대응쌍 모형 / Intro 2e Ch8"
concept: "[[Cohen의 kappa (관측자 일치도)]]"
aliases: [Cohen's kappa, 코헨의 카파, kappa 계수, 카파 통계량, 가중 kappa, weighted kappa, 관측자 일치도]
cross_ref:
  - "Agresti, *Categorical Data Analysis* 3rd ed. (2013) §11.5 — 책 p.432–436"
  - "Agresti, *An Introduction to Categorical Data Analysis* 2nd ed. (2007) §8.5.5 — 책 p.264"
  - "Cohen, J. (1960), *Educ. Psychol. Meas.* 20, 37–46"
  - "Fleiss, Cohen & Everitt (1969) — 점근분산; Spitzer et al. (1967) — 가중 kappa"
tags: [범주형자료분석, kappa, Cohen, 일치도, agreement, 준독립, 준대칭, 가중kappa]
date_created: 2026-07-14
status: 완료
---

# [[Cohen의 kappa (관측자 일치도)]] — 우연 일치를 걷어낸 일치도

> **목표**: "두 관측자가 얼마나 잘 맞는가"를, **우연히 맞을 몫을 빼고** 남은 일치를
> *가능한 최대 초과일치*로 나눈 하나의 지수 $\kappa\in[-1,1]$ 로 정규화한다.

## 핵심 아이디어 — 한 줄 사슬

$$
\underbrace{P_o=\sum_a \pi_{aa}}_{\text{관측 일치}}
\;-\;\underbrace{P_e=\sum_a \pi_{a+}\pi_{+a}}_{\text{독립일 때 기대 일치}}
\;\to\;\underbrace{\text{분모}=1-P_e}_{\text{완전일치 시 최대 초과}}
\;\to\;\boxed{\kappa=\frac{P_o-P_e}{1-P_e}}
\;\to\;\text{구간추정}\ \hat\kappa\pm z_{\alpha/2}\hat\sigma(\hat\kappa)
$$

## 유도 과정

### 0. 왜 "관측 일치율 $P_o$" 만으로는 안 되는가
관측자 A가 범주 $a$, B가 $b$ 로 분류할 확률을 $\pi_{ab}$ 라 하면
일치 확률은 대각합 $\sum_a\pi_{aa}$, 완전일치는 $\sum_a\pi_{aa}=1$.
그런데 **한 범주가 압도적으로 흔하면**, 두 관측자가 아무 생각 없이 그 범주만 찍어도 $P_o$ 는 0.9를 넘는다.
→ **우연에 의한 일치(chance agreement)를 기준선으로 깔고** 그 위 초과분만 세야 한다.

### 1. 기준선: 두 평정이 독립이었다면
독립 모형 하 대각 확률은 $\pi_{a+}\pi_{+a}$ 이므로
$$
P_e=\sum_a \pi_{a+}\pi_{+a}
$$
분자 $P_o-P_e$ = "우연 이상으로 더 맞은 몫".

### 2. 정규화: 분모는 "최대 가능 초과분"
분자에서 $P_o$ 를 그 **최댓값 1**(완전일치)로 바꾼 것이 분모 $1-P_e$.
$$
\boxed{\ \kappa=\frac{\sum_a \pi_{aa}-\sum_a \pi_{a+}\pi_{+a}}{1-\sum_a \pi_{a+}\pi_{+a}}\ }
$$
- $\kappa=0$: 일치가 딱 독립(우연) 수준.
- $\kappa=1$: 완전일치.
- $\kappa<0$: 우연보다도 못 맞음 — 실제로는 거의 발생하지 않음.
- 주변분포가 **고정된 상태**에서 일치가 강할수록 $\kappa$ 가 커진다. (← 이 단서가 나중에 논쟁의 핵심)

### 3. 추론 — 검정이 아니라 구간추정
다항표집에서 $\hat\kappa$ 는 대표본 정규분포를 따르고, 점근분산은 (Fleiss et al. 1969)
$$
\hat\sigma^2(\hat\kappa)=\frac1n\Bigg\{
\frac{P_o(1-P_o)}{(1-P_e)^2}
+\frac{2(1-P_o)\big[2P_oP_e-\sum_a p_{aa}(p_{a+}+p_{+a})\big]}{(1-P_e)^3}
+\frac{(1-P_o)^2\big[\sum_a\sum_b p_{ab}(p_{b+}+p_{+a})^2-4P_e^2\big]}{(1-P_e)^4}
\Bigg\}
$$
여기서 $P_o=\sum_a p_{aa},\ P_e=\sum_a p_{a+}p_{+a}$.

> ⚠️ **$H_0:\kappa=0$ 검정은 거의 무의미하다.** "두 병리학자의 진단이 우연 수준으로만 일치한다"는
> 애초에 그럴듯하지 않은 귀무가설이기 때문. 실무의 질문은 *"얼마나"* 이므로 **구간추정**이 옳다.

## 예제 — 자궁경부암 슬라이드 118장, 병리학자 A vs B (Agresti Table 11.8)

범주: (1) 음성, (2) 비정형 편평상피 증식, (3) 상피내암, (4) 편평/침윤암

| A \ B | 1 | 2 | 3 | 4 | 계 |
|---|---|---|---|---|---|
| 1 | **22** | 2 | 2 | 0 | 26 |
| 2 | 5 | **7** | 14 | 0 | 26 |
| 3 | 0 | 2 | **36** | 0 | 38 |
| 4 | 0 | 1 | 17 | **10** | 28 |
| 계 | 27 | 12 | 69 | 10 | 118 |

- $P_o=(22+7+36+10)/118=0.636$
- $P_e=\dfrac{26\cdot27+26\cdot12+38\cdot69+28\cdot10}{118^2}=0.281$
- $\hat\kappa=\dfrac{0.636-0.281}{1-0.281}=\mathbf{0.493}$ → 최대 가능 초과일치의 약 50% 달성.
- $\hat\sigma(\hat\kappa)=0.057$ → 95% CI $\approx(0.38,\ 0.60)$: **중간 정도의 일치**.

## 일치(agreement) ≠ 연관(association) — §11.5.1의 핵심 구분

> **강한 일치는 강한 연관을 함의하지만, 그 역은 성립하지 않는다.**
> A가 늘 B보다 정확히 한 단계 높게 매긴다면 연관은 완벽하지만 **일치도는 0에 가깝다.**

이 구분을 표에서 읽는 법:
- **독립모형 적합** ($G^2=117.96$, df=9): 대각의 **표준화잔차가 크게 양수**(22칸은 8.5) → 우연 이상의 일치.
- **준독립(quasi-independence) 모형** (§11.5.2): 대각 모수 $\{\delta_a\}$ 추가. $G^2=13.18$ (df=5).
  $$\tau_{ab}=\frac{\pi_{aa}\pi_{bb}}{\pi_{ab}\pi_{ba}}=\exp(\delta_a+\delta_b)$$
  $\delta_a$ 가 클수록 강한 일치. (예: $\hat\delta_2=0.60,\ \hat\delta_3=1.90\Rightarrow\hat\tau_{23}=12.3$)
- **준대칭(quasi-symmetry) 모형** (§11.5.3): 비대각의 연관까지 허용 → $G^2=0.98$ (df=2)로 훨씬 잘 맞음.
  대칭모형은 $G^2=39.18$ (df=5)로 나쁨. 차이 $G^2(S\mid QS)=38.20$ (df=3)
  → **주변이질성(marginal heterogeneity)의 강한 증거**.
  즉 **"일치도가 더 높지 못한 이유 중 하나가 두 관측자의 주변분포 자체가 다르기 때문"** 이다.
  ↳ 여기서 [[McNemar 검정]](주변동질성)과 정확히 맞물린다.

## 가중 kappa (§11.5.5) — 불일치의 "심각도"를 반영

kappa는 범주를 **명목형**으로 취급해 "1 vs 4"와 "3 vs 4"의 불일치를 똑같이 센다.
순서형이면 멀리 어긋난 불일치가 더 심각하므로 가중치 $\{w_{ab}\},\ 0\le w_{ab}\le1,\ w_{aa}=1,\ w_{ab}=w_{ba}$ 를 도입:
$$
\kappa_w=\frac{\sum_a\sum_b w_{ab}\pi_{ab}-\sum_a\sum_b w_{ab}\pi_{a+}\pi_{+b}}
{1-\sum_a\sum_b w_{ab}\pi_{a+}\pi_{+b}}
$$
대표적 가중치:
| 이름 | 가중치 | 특징 |
|---|---|---|
| 선형 | $w_{ab}=1-\dfrac{\lvert a-b\rvert}{I-1}$ | 대각에 가까울수록 부분점수 |
| 이차 (Fleiss–Cohen 1973) | $w_{ab}=1-\dfrac{(a-b)^2}{(I-1)^2}$ | 큰 어긋남에 더 큰 벌점 |

$w_{ab}=\mathbb 1(a=b)$ 로 두면 보통의 $\kappa$ 로 환원된다.

## kappa를 둘러싼 논쟁 — 반드시 알아야 할 약점

1. **주변분포 의존성**: $\kappa$ 와 $\kappa_w$ 의 값은 **주변분포에 강하게 의존**한다.
   *동일한 진단 과정*이라도 환자군의 유병률 구성이 달라지면 $\kappa$ 가 크게 달라진다 (Exercise 11.42).
   → 서로 다른 연구의 $\kappa$ 값을 액면 그대로 비교하면 안 된다.
2. **정보 압축의 대가**: 분할표 전체를 숫자 하나로 줄이므로 **어디서 왜 어긋났는지**가 사라진다.
3. **대안**:
   - 각 범주별로 "그 범주 vs 나머지 통합"의 $2\times2$ 표를 만들어 **범주별 kappa** 계산.
   - 아예 **모형**(준독립·준대칭)으로 일치/불일치 구조를 서술 — Agresti가 §11.5.2–11.5.3에서 권하는 길.
4. 관측자가 셋 이상이면 일반 로그선형 모형은 부적절 → 다관측자 확장 (§11.5.6).

## 막혔던 포인트 & 함정
- **$P_e$ 의 정체**: "우연"은 임의의 상수가 아니라 **독립모형이 예측하는 대각 확률**이다. 주변분포에서 나온다 → 그래서 주변분포 의존성이라는 약점이 따라온다.
- **분모 $1-P_e$ 를 왜 쓰나**: 분자를 그대로 쓰면 $P_e$ 가 큰 상황에서 아무리 잘 맞아도 값이 작아진다. 분모는 "이 주변분포에서 낼 수 있는 최대 초과일치"로 **눈금을 맞추는 장치**.
- **$\kappa$ 검정 vs 구간추정**: $H_0:\kappa=0$ 은 실질적으로 무의미. 항상 CI로 보고할 것.
- **연관 ≠ 일치**: 오즈비가 크다고 일치도가 높은 게 아니다. 한 관측자가 체계적으로 한 칸씩 높게 매기는 경우가 반례.

## 연결 개념
- [[McNemar 검정]] — 같은 정사각표의 **주변** 비교. 주변이질성이 kappa를 끌어내리는 원인이라는 점에서 직결 (§11.1 ↔ §11.5.3).
- [[대칭성·준대칭성·주변동질성 모형]] — 준독립·준대칭 적합으로 일치 구조를 모형화 (§11.4).
- [[표준화 잔차와 모형 적합도]] — 대각 양수·비대각 음수 잔차 패턴 읽기 (§3.3.1).
- [[로그선형모형]] — $\tau_{ab}=\exp(\delta_a+\delta_b)$ 의 배경.

## 참고 교재 페이지
- Agresti, *Categorical Data Analysis*, 3rd ed. (2013), **§11.5, 책 p.432–436** (PDF p.450–454, offset 18) — 스캔본. 전사본: [[_원문_Agresti3e_Ch11_McNemar_Kappa(OCR)]]
- Agresti, *An Introduction to Categorical Data Analysis*, 2nd ed. (2007), **§8.5.5, 책 p.264** (PDF p.284, offset 20).
- Cohen, J. (1960). "A coefficient of agreement for nominal scales." *Educational and Psychological Measurement* 20(1), 37–46.
- Fleiss, J. L., Cohen, J., & Everitt, B. S. (1969). "Large sample standard errors of kappa and weighted kappa." *Psychological Bulletin* 72(5), 323–327.
- Spitzer, R. L. et al. (1967) — 가중 kappa 원논문. Fleiss & Cohen (1973) — 이차 가중치.
- Landis, J. R. & Koch, G. G. (1977) — $\kappa$ 값 해석 관례(널리 인용되나 자의적이라는 비판도 있음).
