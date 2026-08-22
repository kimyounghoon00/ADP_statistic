---
aliases: [등분산성, homoscedasticity, 등분산 가정, 이분산성, heteroscedasticity, 분산 동일성]
tags: [회귀분석, 실험설계, 4장, 등분산성, 이분산, 회귀진단, ANOVA가정, ClusterB]
subject: 회귀분석
chapter: ["김충락 Ch4 회귀진단", "김충락 §6.3 가중최소제곱", "Montgomery Ch3 §3.4 잔차분석"]
book_pages: "김충락 Ch4 / §6.3 p253–254 / Montgomery 8th §3.4"
moc: ["[[MOC_이차형식]]"]
cluster: [B]
cross_ref: ["김충락 §6.3", "Montgomery §3.4", "Hogg §9.2"]
date_created: 2026-08-22
---

# 등분산성 (homoscedasticity)

> [!info] 📖 교재 위치 · 커리큘럼
> **본거지**: 김충락 §3.1 의 $\operatorname{Cov}(\varepsilon)=\sigma^2 I$ 가정 중 **대각원소가 모두 같다**는 부분. 위배 시 처방은 §6.3 [[가중최소제곱(WLS)]] / [[일반화최소제곱(GLS)]].
> **커리큘럼 연결**: [[MOC_이차형식]] (Cluster B) 가지 ⑤ 회귀진단. ANOVA 3대 가정(정규성·**등분산성**·독립성) 중 둘째.

## 1. 정의

$$
\operatorname{Var}(\varepsilon_i)=\sigma^2\quad\text{for all } i
\qquad\Longleftrightarrow\qquad \operatorname{Cov}(\varepsilon)=\sigma^2 I_n
$$

$\sigma^2 I$ 는 **두 가지**를 동시에 주장한다 — 대각원소가 전부 같다(**등분산성**), 비대각원소가 전부 0(**무상관**). 둘은 별개의 가정이며 별개로 깨진다.

## 2. 깨지면 무엇을 잃는가

| 성질 | 등분산 위배 시 |
|---|---|
| $\hat\beta$ 불편성 | **유지** ($E[\hat\beta]=\beta$ 는 1차 적률만 쓴다) |
| $\hat\beta$ 일치성 | **유지** |
| BLUE (최소분산) | **상실** → [[Gauss-Markov 정리]] 전제 붕괴, [[Aitken 정리]]에 의해 GLS가 BLUE |
| $\widehat{\operatorname{Var}}(\hat\beta)$ | **편향** → t·F 검정과 신뢰구간이 무효 |

> [!important] 실무 우선순위
> 점추정은 살아 있고 **추론(표준오차)이 죽는다.** 그래서 처방은 두 갈래다 — 추정량을 바꾸거나([[가중최소제곱(WLS)]]·[[일반화최소제곱(GLS)]]), 표준오차만 고치거나(White 강건표준오차).

## 3. 진단

| 방법 | 성격 | 노트 |
|---|---|---|
| Residuals vs Fitted 산점도 | 시각적 — 나팔모양 확인 | [[잔차의 직교성과 진단 그림의 가로축]] |
| **Breusch–Pagan** | $e^2$ 을 $X$ 에 회귀, LM 검정 | [[Breusch-Pagan 검정]] |
| **Levene / Brown–Forsythe** | 집단별 분산 비교 (ANOVA 맥락) | [[Levene 검정]] |
| Bartlett | 정규성에 민감 — 실무 비권장 | — |
| White | 이분산 + 설정오류 동시 검정 | — |

> [!warning] 가로축 주의
> 잔차 산점도의 가로축은 반드시 **적합값 $\hat y$**. 관측값 $y$ 를 놓으면 $y^\top e=SSE$ 때문에 기울기 $1-R^2$ 의 가짜 우상향이 나타난다 → [[잔차의 직교성과 진단 그림의 가로축]]

## 4. 반례 — 등분산이 성립해도 결론이 무의미할 수 있다

> [!danger] 2026-08-22 세션에서 확인
> $N(50,100)$ 을 평균에서 잘라 두 집단을 만들면([[자기참조적 집단화와 F검정의 함정]]):
> - 집단내 분산: 남 36.29 / 여 36.19 — 이론 $\sigma^2(1-2/\pi)=36.34$. **완전한 등분산**
> - [[Levene 검정]] 기각률 5.17% (명목 5%) — 잡을 것이 없다
> - 그럼에도 F검정 기각률 **100%** (존재하지 않는 효과)
>
> **등분산성 통과는 결론의 타당성을 보증하지 않는다.** 가정검정은 모형 내부의 조건만 볼 뿐, 설계의 타당성은 볼 수 없다. → [[무작위화 (Randomization)]]

## 5. 연결

[[Levene 검정]] · [[Breusch-Pagan 검정]] · [[가중최소제곱(WLS)]] · [[일반화최소제곱(GLS)]] · [[Aitken 정리]] · [[Gauss-Markov 정리]] · [[Ch04_잔차가정검정_백지유도]] · [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]] · [[MOC_이차형식]]
