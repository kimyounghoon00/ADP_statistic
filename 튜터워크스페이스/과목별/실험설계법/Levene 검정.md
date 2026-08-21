---
subject: 실험설계법
chapter: Montgomery §3.4 (등분산 가정 점검) — 반복측정 사전가정으로 사용
concept: "[[Levene 검정]]"
aliases: [Levene, Levene test, 르빈 검정, 레빈 검정, 집단 간 등분산 검정, Brown-Forsythe 검정]
cluster: [C]
cross_ref:
  - "Levene (1960); Brown & Forsythe (1974), JASA 69, 364–367"
  - "[[Ch14_반복측정ANOVA_구형성_정리노트]] (사전 가정 3종 중 between 등분산)"
  - "[[등분산성(homoscedasticity)]] (회귀 맥락의 같은 가정)"
tags: [실험설계법, ANOVA, 등분산성, Levene, BrownForsythe, 사전가정, ClusterC, stub]
date_created: 2026-08-21
status: stub (정의·용법만 — 백지유도 대상)
date_modified: 2026-08-21
---

# Levene 검정

> [!info] 📖 교재 위치 · 커리큘럼
> ANOVA의 **집단 간 등분산** 점검. `[[Ch14_반복측정ANOVA_구형성_정리노트]]` 사전 가정 표의 between 축(gender)에서 사용했다.
> 회귀 맥락의 같은 가정은 [[등분산성(homoscedasticity)]] → [[Breusch-Pagan 검정]].

> [!definition] 정의 (요지)
> $H_0:\ \sigma_1^2=\cdots=\sigma_k^2$. 각 관측치를 **집단중심으로부터의 절대편차**
> $$z_{ij}=\bigl|y_{ij}-\tilde y_{i\cdot}\bigr|$$
> 로 바꾼 뒤, $z_{ij}$ 에 **일원 ANOVA의 $F$ 를 그대로 적용**한다.
> - $\tilde y_{i\cdot}=\bar y_{i\cdot}$ (평균) → 원 Levene(1960)
> - $\tilde y_{i\cdot}=\text{median}$ → **Brown–Forsythe 변형**, 비정규·두꺼운 꼬리에 강건. R `car::leveneTest` 기본값이 중앙값 버전이다.

## 왜 이 변환이 통하는가 (백지유도 과제)
- "분산이 다르다"를 "절대편차의 **평균**이 다르다"로 번역하면 분산 비교가 평균 비교로 내려온다 → 이미 가진 도구($F$)를 재사용.
- 확인할 것: ① 왜 제곱이 아니라 절대편차인가(꼬리 민감도) ② 중앙값 중심이 강건한 이유 ③ Bartlett 검정과의 대비(정규성 의존).

## 연결
- [[Ch14_반복측정ANOVA_구형성_정리노트]] — 사전 가정 3종(정규성·등분산·구형성) 중 두 번째
- [[등분산성(homoscedasticity)]] · [[Breusch-Pagan 검정]] — 회귀 맥락의 대응물
- 위배 시 대응: Welch ANOVA / 변환 / 이분산 혼합모형 → Ch14 노트 "가정 위배 시 대응" §A

> [!note] stub
> 씨앗 노트다. 위 세 확인 항목과 Bartlett 대비를 직접 채워 넣을 것.
