---
aliases: [Montgomery 불균형 ANOVA, 불균형 요인배치 Type SS, 공변량 요인실험 Type III, Exact Method ANOVA]
tags: [회귀분석, 실험설계법, 분산분석, TypeI_II_III, 불균형, ANCOVA, Montgomery, 교차항]
subject: 회귀분석
source_book: "Montgomery, Design and Analysis of Experiments, Wiley 2012 (8e)"
date_created: 2026-06-18
status: 초안 (튜터 작성 — 학습자 백지유도 후 교체)
---

# [[Montgomery 불균형·공변량 ANOVA와 Type I·II·III]]

> **한 줄 요약**: Montgomery는 "Type I/II/III"라는 라벨 대신 **불균형이 직교성을 깨면 분산분석모형을 회귀모형으로 바꿔 `[[일반회귀유의성검정(General Regression Significance Test)]]`으로 SS를 만든다**고 본다. 그런데 *"이 작업을 여러 방식으로 할 수 있고, 방식마다 SS가 달라진다"* — 이 여러 방식이 곧 Type I·II·III다.

관련 노트: `[[Type I·II·III 제곱합과 부분 F-검정]]` · `[[Type II 제곱합 (정식화)]]`

---

## 0. 우리 예제와의 연결

우리가 손으로 세운 모형은 **요인 A(3수준) + 연속형 $X_1,X_2$ + 교차항 $A{:}X_1$**, $n=10$. 이것은 Montgomery 분류로 두 절에 걸쳐 있다:

- **요인 + 교차항의 불균형** 측면 → **§15.2** (Unbalanced Factorial)
- **요인 + 연속형 공변량 + (공변량×처리) 교차항** 측면 → **§15.3.4** (Factorial Experiments with Covariates)

즉 우리 예제는 Montgomery의 **§15.2.3 + §15.3.4 결합형**이다.

---

## 1. 왜 Type이 갈리는가 — 직교성의 붕괴 (§15.2 도입, 인쇄 p.652)

> "The orthogonality property of main effects and interactions present in balanced data **does not carry over to the unbalanced case**. … the usual analysis of variance techniques do not apply."

핵심: **균형설계에서는 주효과·교차항이 직교**라 SS가 순서·보정에 무관하게 유일하다 → Type I=II=III. **불균형이거나 연속형 공변량이 섞이면 직교가 깨져** "무엇을 먼저/무엇에 보정해 넣느냐"가 SS를 바꾼다. 우리 예제는 $X_1,X_2$ 상관 + 군별 $X_1$ 평균 차이로 이미 비직교 → 세 타입이 갈린다.

---

## 2. §15.2의 3가지 처리 방식 (인쇄 p.652–655)

| 절 | 내용 | Type 대응 |
|---|---|---|
| **§15.2.1 Proportional Data** (p.652–653) | $n_{ij}=n_{i.}n_{.j}/n_{..}$ 면 직교 회복. "factor A fit before B"의 **sequential model fitting** | `[[Type I 제곱합]]` (순차) |
| **§15.2.2 Approximate Methods** (p.654–655) | 결측 추정·set aside·unweighted means·weighted squares of means (Yates 1934) | (근사) |
| **§15.2.3 The Exact Method** (p.655) | 분산분석모형 → 회귀모형 → 일반회귀유의성검정. **"several ways → different SS"** | **Type I·II·III의 출처** |

**§15.2.3 원문 핵심**: 빈 셀($n_{ij}=0$)이나 셀 크기가 크게 다르면 근사법이 부적절 → exact analysis 필요. 그 방법이 *"this may be done in several ways, and these methods may result in different values for the sums of squares. Furthermore, the hypotheses being tested are not always direct analogs of those for the balanced case, nor are they always easily interpretable."*

> ⚠️ 이 마지막 문장이 **Type III가 대비코딩에 민감하고 해석이 까다로운 이유**의 교재적 근거다. → `[[Type II 제곱합 (정식화)]]` 5절(추정가능함수)과 연결.

---

## 3. §15.3.4 공변량 있는 요인실험 (인쇄 p.667–669)

우리 예제의 $A{:}X_1$(처리×공변량 교차)을 정면으로 다루는 절.

핵심 논점 정리:
- **포화 위험**: 셀마다 별도 기울기(공변량×처리 교차항)를 주면 셀당 관측치가 모자라 오차 자유도가 없어진다. $2^3$이면 최소 3반복 필요. → **우리 $n=10$, 모수 7개, $df_E=3$도 같은 빠듯함**.
- **3가지 가정 선택지**:
  1. 공변량 효과 없음 (보통 최악) — 무시하면 결론이 크게 틀어질 수 있음.
  2. **처리×공변량 교차 없음(공통 기울기)** — 틀려도 평균적 공변량 보정으로 정밀도↑. 단, 여러 수준이 서로 다른 방향으로 교차하면 상쇄되어 공변량이 무의미해 보일 수 있음.
  3. 일부 고차 교차항을 무시해 오차 자유도 확보.
- "treatment SS를 adjusted main effects $SS_A, SS_B$ 와 adjusted interaction $SS_{AB}$ 로 분할" → 이게 **공변량 보정 후의 Type II/III 분해**.

---

## 4. 개념 엔진: 일반회귀유의성검정 (앞 장 토대)

Montgomery의 모든 Type SS는 **추가제곱합 $R(\cdot\mid\cdot)$** 한 가지로 환원된다.

$$SS(\text{항}) = SSE(\text{축소}) - SSE(\text{완전}) = \mathbf y'(P_{\text{큰}}-P_{\text{작}})\mathbf y$$

등장 위치: §3.3.4 불균형 일원배치(p.79), §4.1 RCBD의 $R(\mu,\tau,\beta)$(p.157), 제10장 extra sum of squares method. → 김충락 **3장(추가제곱합·분산분석표)** + **5장(일반선형가설 $A\boldsymbol\beta=\mathbf c$)** 과 1:1 대응. 자세히는 `[[Type I·II·III 제곱합과 부분 F-검정]]` 참조.

---

## 5. 정직한 주의 — "Type" 라벨의 출처

Montgomery **인쇄본 본문은 "Type I/II/III"를 직접 명명하지 않는다.** 개념(§15.2.3 "several ways → different SS")만 제시하고, **명시적 Type 분류와 SAS PROC GLM식 정의는 이 장의 보충자료 §S15.4 "Analysis of Unbalanced Data"** 로 미룬다(온라인 supplement). 명시적 명명·SAS 대응을 보려면 Searle(1971a), Milliken & Johnson(1984), SAS PROC GLM 문서가 1차 출처.

---

## 6. 한 장 요약표

| 관점 | 균형 | 불균형/공변량 |
|---|---|---|
| 직교성 | 성립 | 깨짐 |
| Type I/II/III | 모두 일치 | 갈림 |
| 계산 도구 | 닫힌형 공식 | 회귀모형 + 일반회귀유의성검정 |
| Montgomery 절 | 본문 대부분 | §15.2, §15.3.4 |
| 김충락 대응 | 3장 분산분석표 | 3장 추가제곱합 + 5장 일반선형가설 |

---

## 7. 참고 페이지 (PDF = 인쇄쪽 + 16)

- Montgomery **§15.2 Unbalanced Data in a Factorial Design** — 인쇄 p.652–655 / PDF p.668–671
  - §15.2.1 Proportional Data (p.652–653) / §15.2.2 Approximate (p.654–655) / **§15.2.3 The Exact Method (p.655)**
- Montgomery **§15.3 Analysis of Covariance** — 인쇄 p.655– / **§15.3.4 Factorial Experiments with Covariates 인쇄 p.667 / PDF p.683**
- Montgomery §3.3.4 (p.79), §4.1 (p.157), 제10장 (extra SS method)
- 김충락·강근석 『회귀분석』 3장(p.97–162), 5장(p.201–230)
- 보충: Searle (1971a); Milliken & Johnson (1984); SAS PROC GLM
