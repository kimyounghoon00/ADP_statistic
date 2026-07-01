---
aliases: [개념 연결 커리큘럼, Concept Connection Map]
tags: [통계학, 커리큘럼, 연결학습, Hub]
date_created: 2026-06-07
---

# 🔗 통계학 개념 연결 커리큘럼 (Concept Connection Curriculum)

> **핵심 철학**: 통계학의 과목 경계는 인위적이다.  
> 수리통계·회귀분석·실험설계·다변량·시계열은 **공통된 수학적 뿌리**에서 가지를 뻗는다.  
> 이 문서는 그 뿌리를 중심으로 클러스터를 묶어 학습 경로를 설계한다.

---

## 🗺️ 전체 연결 구조 (Big Picture)

```
[수리통계 — 뿌리]
        │
   ┌────┴────┬─────────┬──────────┬──────────┐
   ▼         ▼         ▼          ▼          ▼
[Cluster A] [Cluster B] [Cluster C] [Cluster D] [Cluster E]
추정 효율성  이차형식    우도 기반   지수족·GLM   투영과 LSE
(CRLB↔GM)  (Cochran)   추론(LRT)  (충분통계량)  (Hat Matrix)
   │             │          │          │           │
   ▼             ▼          ▼          ▼           ▼
회귀분석      실험설계    실험설계    회귀분석    다변량·PCA
Gauss-Markov  ANOVA SS   F-검정     로지스틱    주성분 투영
                분해       = LRT     포아송 회귀
                               │
                               ▼
                          [Cluster F]
                          점근 이론
                         (CLT·Delta)
                               │
                               ▼
                           시계열
                          (ARMA 추론)
```

---

## 📌 Cluster A — 추정의 효율성 (Estimation Efficiency)

> **핵심 질문**: "가장 좋은 추정량이란 무엇인가?"

### 개념 연결 사슬

```
[[Fisher 정보량과 Cramér-Rao 하한 (CRLB)]]   ← 수리통계 (Hogg §6.2)
            │
            │  "선형 불편추정량으로 제한하면?"
            ▼
[[Gauss-Markov 정리]]                          ← 회귀분석 (김충락 Ch3)
  LSE = BLUE (Best Linear Unbiased Estimator)
            │
            │  "정규성 가정 추가하면?"
            ▼
[[충분통계량과 인수분해 정리 (Fisher-Neyman)]] ← 수리통계 (Hogg §7.2)
            │
            ▼
[[Rao-Blackwell 정리]]                         ← 수리통계 (Hogg §7.3)
  조건부 기댓값으로 분산 줄이기
            │
            ▼
[[완비통계량과 Lehmann-Scheffé 정리]]          ← 수리통계 (Hogg §7.4)
  UMVUE (균일최소분산불편추정량) 존재성
            │
            │  "정규 오차 하에서 β̂ = MLE = UMVUE 인가?"
            ▼
[[LSE의 UMVUE 성질 — 정규성 하에서]]           ← 수리통계+회귀분석 연결
```

### 학습 포인트
- CRLB는 **모든** 불편추정량의 분산 하한 (모수 추정의 물리적 한계)
- Gauss-Markov는 **선형** 불편추정량 중 최적 (정규성 불필요)
- 정규 오차 가정 시: LSE = MLE = UMVUE — 세 가지 최적성이 일치

### 학습 순서 (권장)
1. `[[Fisher 정보량과 Cramér-Rao 하한]]` 유도 (Hogg §6.2)
2. `[[충분통계량과 인수분해 정리]]` (Hogg §7.2)
3. `[[Rao-Blackwell 정리]]` (Hogg §7.3)
4. `[[완비통계량과 Lehmann-Scheffé 정리]]` (Hogg §7.4)
5. `[[Gauss-Markov 정리]]` (김충락 Ch3) — 위 4개 이후 공부하면 "왜 BLUE인가"가 자명해짐

---

## 📌 Cluster B — 이차형식과 분포 (Quadratic Forms & Cochran)

> **핵심 질문**: "SST = SS_reg + SSE 분해는 왜 성립하고, 각 항은 왜 독립인가?"

### 개념 연결 사슬

```
[[다변량 정규분포 — 밀도함수]]                 ← 수리통계 (Hogg §3.5)
  X ~ N_n(μ, Σ) 정의
            │
            ▼
[[이차형식의 분포와 독립성 (Cochran 정리)]]    ← 수리통계 (Hogg §9.8–9.9)
  A가 멱등(idempotent)이면 X'AX ~ χ²(rank A)
            │
     ┌──────┴──────┐
     ▼             ▼
[[Hat Matrix의       [[일원 ANOVA 제곱합 분해]]  ← 실험설계 (Montgomery §3)
  멱등성과 대칭성]]    SST = SS_trt + SSE
  ← 회귀분석 (김충락) 각 SS는 멱등 행렬의 이차형식
            │             │
            └──────┬───────┘
                   ▼
      [[F-검정의 분포 유도]]
      SS_reg/p  ÷  SSE/(n-p-1) ~ F(p, n-p-1)
                   │
                   ▼
      [[MANOVA — Wilks' Λ 검정통계량]]         ← 다변량분석
      (이차형식의 다변량 확장)
```

### 학습 포인트
- 멱등 행렬(idempotent matrix, A² = A)이 모든 분해의 핵심 도구
- 회귀분석의 Hat Matrix H = X(X'X)⁻¹X' 는 멱등: H² = H
- ANOVA의 SS 분해 = 다른 멱등 행렬들의 합
- Cochran 정리 → 각 SS가 독립인 χ² → F분포 유도

### 학습 순서 (권장)
1. `[[다변량 정규분포]]` (Hogg §3.5) — 이차형식 이해의 기반
2. `[[Hat Matrix의 멱등성 및 대칭성]]` (김충락) — 구체적 예시
3. `[[이차형식과 Cochran 정리]]` (Hogg §9.8–9.9) — 일반 이론
4. `[[일원 ANOVA 제곱합 분해]]` (Montgomery §3) — 적용
5. `[[MANOVA — Wilks' Λ]]` (J&W) — 다변량 확장

---

## 📌 Cluster C — 우도 기반 추론 (Likelihood-Based Inference)

> **핵심 질문**: "t-검정, F-검정, 카이제곱 검정은 모두 같은 원리인가?"

### 개념 연결 사슬

```
[[Neyman-Pearson 보조정리]]                    ← 수리통계 (Hogg §8.1)
  "최강력 검정 = 우도비 기반"
            │
            ▼
[[균일최강력검정 (UMP Test)]]                  ← 수리통계 (Hogg §8.2)
  지수족에서 UMP 존재
            │
            ▼
[[우도비 검정 (LRT) 과 점근 카이제곱]]         ← 수리통계 (Hogg §6.3, §8.3)
  -2 log Λ →_d χ²(r)  (Wilks 정리)
            │
     ┌──────┴──────┬──────────┐
     ▼             ▼          ▼
[[F-검정 =      [[t-검정 =   [[Wald 검정,
  정규모형의      LRT 특수    Score 검정]]
  LRT]]           경우]]
  ← 실험설계      ← 회귀분석        │
  ANOVA           계수 검정         ▼
                           [[GLM 추론 —
                             로지스틱·포아송]]
                             ← 회귀분석 Ch8
```

### 학습 포인트
- 익숙한 t-검정, F-검정은 모두 LRT의 특수 경우 (정규 가정 하)
- GLM (비정규 모형)에서는 정확한 F-검정이 없어 점근 LRT 사용
- Wald 검정: (θ̂ - θ₀)² / Var(θ̂) — MLE의 점근정규성 활용

### 학습 순서 (권장)
1. `[[Neyman-Pearson 보조정리]]` (Hogg §8.1)
2. `[[균일최강력검정 (UMP)]]` (Hogg §8.2)
3. `[[우도비 검정과 Wilks 정리]]` (Hogg §8.3)
4. `[[F-검정이 LRT임을 증명]]` (수리통계+실험설계 연결)
5. `[[로지스틱 회귀와 MLE 유도]]` (김충락 Ch8) — GLM 맥락에서 LRT 적용

---

## 📌 Cluster D — 지수족과 GLM (Exponential Family → GLM)

> **핵심 질문**: "정규분포, 베르누이, 포아송은 왜 같은 틀(GLM)로 분석되는가?"

### 개념 연결 사슬

```
[[지수족 (Exponential Family) 정의와 성질]]    ← 수리통계 (Hogg §7.5)
  f(x;θ) = exp[η(θ)T(x) - B(θ) + h(x)]
            │
     ┌──────┴──────┐
     ▼             ▼
[[충분통계량과    [[자연모수(η)와
  지수족]]         정준연결함수]]
  T(x)가 충분          │
  통계량              ▼
               [[GLM — 연결함수와 지수족]]  ← 회귀분석 (김충락 Ch8–9)
               정규    → identity link
               베르누이 → logit link
               포아송  → log link
                    │
                    ▼
             [[베이즈 — 켤레 사전분포]]      ← 베이즈통계
             지수족의 켤레 사전 = 사후도 지수족
```

### 학습 포인트
- GLM의 정준연결함수(canonical link)는 지수족의 자연모수 η(θ)에서 직접 유도
- 지수족의 충분통계량 T(x)가 GLM에서 β̂의 계산 기반
- 베이즈의 켤레 사전(conjugate prior)도 지수족 구조에서 자연스럽게 도출

### 학습 순서 (권장)
1. `[[지수족 정의와 성질]]` (Hogg §7.5)
2. `[[지수족과 완비충분통계량]]` (Hogg §7.4–7.5)
3. `[[로지스틱 회귀와 MLE 유도]]` (김충락 Ch8)
4. `[[포아송 회귀와 연결함수]]` (김충락 Ch9)
5. `[[켤레 사전분포 (Conjugate Prior)]]` (베이즈) — 지수족 관점

---

## 📌 Cluster E — 투영과 최소제곱 (Projection & Least Squares)

> **핵심 질문**: "LSE는 왜 '최소'이고, 그 기하학적 의미는 무엇인가?"

### 개념 연결 사슬

```
[[조건부 기댓값과 반복기댓값 법칙 (LIE)]]     ← 수리통계 (Hogg §2.3)
  E[Y|X] = L₂ 공간에서 Y의 X 위로의 투영
            │
            ▼
[[정규방정식과 LSE 유도]]                      ← 회귀분석 (김충락 Ch1–2)
  β̂ = (X'X)⁻¹X'y
  y를 col(X) 위로 투영
            │
            ▼
[[Hat Matrix의 멱등성 및 대칭성]]              ← 회귀분석 (김충락 Ch3)
  H = X(X'X)⁻¹X',  H² = H,  H = H'
  Hy = ŷ (투영),  (I-H)y = ê (잔차)
            │
     ┌──────┴──────┐
     ▼             ▼
[[Gauss-Markov:   [[PCA — 스펙트럼 분해와   ← 다변량분석
  투영이 BLUE임    분산 설명비]]
  이유]]          공분산행렬 Σ의 고유벡터
                 = 분산 최대화 방향으로의 투영
                        │
                        ▼
                [[정준상관분석 (CCA)]]        ← 다변량분석
                두 변수 집합 간의 최적 투영
```

### 학습 포인트
- LSE, PCA, CCA 모두 수학적으로 "투영(projection)"
- Hat Matrix의 멱등성은 "한 번 투영하면 다시 투영해도 같다"는 기하학적 사실
- PCA의 주성분 = 공분산 행렬의 고유벡터 = 분산을 최대화하는 투영 방향

### 학습 순서 (권장)
1. `[[조건부 기댓값과 반복기댓값 법칙 (LIE)]]` (Hogg §2.3)
2. `[[정규방정식과 LSE 유도]]` (김충락 Ch1–2)
3. `[[Hat Matrix의 멱등성 및 대칭성]]` (김충락 Ch3)
4. `[[Gauss-Markov 정리]]` (김충락 Ch3)
5. `[[PCA — 스펙트럼 분해와 분산 설명비]]` (J&W §8)

---

## 📌 Cluster F — 점근 이론 (Asymptotic Theory)

> **핵심 질문**: "표본이 커지면 추정량은 어떻게 행동하는가?"

### 개념 연결 사슬

```
[[확률수렴과 분포수렴]]                        ← 수리통계 (Hogg §5.1–5.2)
  X_n →_p X,   X_n →_d X
            │
            ▼
[[중심극한정리 (CLT) 와 Delta Method]]         ← 수리통계 (Hogg §5.3)
  √n(X̄ - μ) →_d N(0, σ²)
            │
     ┌──────┴──────┬──────────┐
     ▼             ▼          ▼
[[MLE의 점근    [[GLM 추론   [[ARMA 추정량의
  정규성]]        (Wald,       점근정규성]]
  Hogg §6.1      Score, LRT]] ← 시계열 (Levendis)
                 김충락 Ch8
                        │
                        ▼
                [[단위근 검정 (ADF)]]           ← 시계열 (Levendis Ch4)
                비정상 시계열에서의 특수 점근론
                (Dickey-Fuller 분포 ≠ 정규)
```

### 학습 포인트
- MLE의 점근정규성 → 대표본에서 Wald/Score/LRT 세 검정이 동치
- 시계열의 단위근 검정은 표준 CLT가 적용되지 않는 예외 (Dickey-Fuller 분포)
- Delta Method: g(X̄)의 분산 ≈ [g'(μ)]² σ²/n — GLM에서 빈번히 사용

### 학습 순서 (권장)
1. `[[확률수렴과 분포수렴]]` (Hogg §5.1–5.2)
2. `[[중심극한정리와 Delta Method]]` (Hogg §5.3)
3. `[[MLE의 점근정규성]]` (Hogg §6.1)
4. `[[우도비 검정과 Wilks 정리]]` (Hogg §6.3, §8.3)
5. `[[ARIMA 차분과 단위근 검정 (ADF)]]` (Levendis Ch4) — 점근론의 예외 사례

---

## 🔄 클러스터 간 학습 흐름 (추천 순서)

```
Cluster E (투영·LSE 기하학)
      ↓
Cluster A (추정 효율성: CRLB ↔ Gauss-Markov)
      ↓
Cluster B (이차형식·Cochran → ANOVA 분해)
      ↓
Cluster C (우도 기반 추론: NP → LRT → F-검정)
      ↓
Cluster D (지수족 → GLM → 베이즈 켤레)
      ↓
Cluster F (점근 이론 → 시계열 단위근)
```

> 단, 사전식(랜덤) 학습이 원칙이므로 어느 클러스터에서 시작해도 무방합니다.
> 다만 같은 클러스터 내의 순서는 가급적 지키세요.

---

## 📝 진행 현황 (Cluster별 완료 체크)

| 클러스터 | 핵심 연결 | 완료 개념 수 |
|----------|-----------|:------------:|
| A. 추정 효율성 | CRLB ↔ Gauss-Markov | 0 / 5 |
| B. 이차형식 | Cochran ↔ ANOVA ↔ Hat Matrix | 0 / 5 |
| C. 우도 추론 | NP ↔ LRT ↔ F-검정 ↔ GLM | 0 / 5 |
| D. 지수족·GLM | 지수족 ↔ GLM ↔ 베이즈 켤레 | 0 / 4 |
| E. 투영·LSE | LIE ↔ Hat Matrix ↔ PCA | 0 / 5 |
| F. 점근이론 | CLT ↔ MLE 점근 ↔ 시계열 단위근 | 0 / 5 |
