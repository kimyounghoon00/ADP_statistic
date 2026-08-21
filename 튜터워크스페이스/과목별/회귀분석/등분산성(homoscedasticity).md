---
subject: 회귀분석
chapter: Ch4 회귀진단 — 오차항 가정 3축 중 ② 등분산성
concept: "[[등분산성(homoscedasticity)]]"
aliases: [등분산성, homoscedasticity, 등분산, 이분산, heteroscedasticity, 등분산성 검정]
cluster: [B, E]
cross_ref:
  - "김충락·강근석 『회귀분석』 2판 — 제4장 회귀진단"
  - "[[Breusch-Pagan 검정]] (검정통계량 유도 본체)"
  - "[[Ch04_잔차가정검정_백지유도]] §2 (백지유도 원본)"
moc: ["[[MOC_이차형식]]"]
tags: [회귀분석, 4장, 회귀진단, 등분산성, 이분산, 가정, ClusterB, ClusterE, 인덱스노트]
date_created: 2026-08-21
status: 인덱스 (본체는 [[Breusch-Pagan 검정]]·[[Ch04_잔차가정검정_백지유도]] §2)
date_modified: 2026-08-21
---

# 등분산성 (homoscedasticity)

> [!info] 📖 교재 위치 · 커리큘럼
> 제4장 회귀진단. 커리큘럼: [[MOC_이차형식]] (Cluster B) 가지 ⑤ 회귀진단.
> **이 노트는 인덱스다.** 유도·검정통계량 본체는 아래 두 노트에 있다.

> [!definition] 정의
> 오차의 분산이 관측치와 무관하게 일정하다는 가정.
> $$\mathrm{Var}(\varepsilon_i)=\sigma^2\quad(\forall i)\;\iff\;\mathrm{Cov}(\boldsymbol\varepsilon)=\sigma^2 I\ \text{의 \textbf{대각} 원소가 모두 같음}$$
> 비대각(=0)은 무상관 가정이고, 대각이 이 가정이다. → [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]] §5

## 어디에 무엇이 있나

| 내용 | 위치 |
|---|---|
| $H_0$ 를 검정 가능한 모수 제약으로 번역, $e_i^2$ 프록시, $nR^2\sim\chi^2_q$ | [[Breusch-Pagan 검정]] |
| 백지유도 원본(§2 전체), 잔차는 원래 비등분산($\mathrm{Var}(e_i)=\sigma^2(1-h_{ii})$) | [[Ch04_잔차가정검정_백지유도]] |
| 진단 그림에서 무엇을 보는가(깔때기·Scale–Location) | [[잔차의 직교성과 진단 그림의 가로축]] §3 |
| 위배 시 처방(WLS·GLS) | [[일반화최소제곱(GLS)]] |
| 실전 적용(Boston: BP=65.122, ncvTest=15.244 → 위배) | [[Ch04_ADP32_Boston_회귀가정검토]] |
| 집단 간 등분산(ANOVA 맥락) | [[Levene 검정]] |

> [!warning] 주어는 오차이지 잔차가 아니다
> 모형이 완벽해도 $\mathrm{Var}(e_i)=\sigma^2(1-h_{ii})$ 라 **잔차는 원래 등분산이 아니다.** 가정·검정의 주어는 오차 $\varepsilon_i$ 다.
