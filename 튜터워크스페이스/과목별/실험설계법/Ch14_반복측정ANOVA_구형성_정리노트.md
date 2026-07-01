---
subject: 실험설계법
chapter: Ch14 반복측정 설계 (+ Ch5 이원ANOVA, Ch3.5 다중비교)
concept: '[[반복측정 설계와 구형성 가정 (Mauchly 검정)]]'
cluster:
- B
- C
cross_ref:
- Montgomery §5 (이원 ANOVA·교호작용)
- Montgomery §3.5 (다중비교 — Tukey/Bonferroni)
- Montgomery §13 (랜덤효과 — 개체를 random block으로)
- Hogg §9.2, §9.5 (ANOVA SS 분해, 교호작용의 이론적 유도)
tags:
- 반복측정
- 혼합설계
- Mauchly
- 구형성
- GreenhouseGeisser
- 사후분석
- 주변성원칙
- 상호작용위계
- 심슨역설
- ClusterB
- 실험설계법
date_created: "2026-06-08"
date_modified: "2026-06-14"
status: "ADP exam34-문제3 풀이 연계 노트"
source: ADP기출 exam34 problem3 (40명 x 성별 x 학습방법 3수준)
---

# [[반복측정 설계와 구형성 가정 (Mauchly 검정)]] — Ch14 정리노트

## 핵심 아이디어

**같은 개체(subject)를 반복 측정**하면 측정치들이 서로 독립이 아니다. 일반 이원 ANOVA는
모든 관측치 독립을 가정하므로 그대로 쓰면 오차자유도가 부풀려져 **제1종 오류가 증가**한다.
→ 개체(ID)를 **랜덤효과(random block)** 로 분리하는 **반복측정 ANOVA**가 필요.

이 문제처럼 한 요인은 개체 간(gender), 한 요인은 개체 내(method) 인 구조를
**혼합설계(Mixed-design / Split-plot) 반복측정 ANOVA**라 한다.

| 요인 | 유형 | 오차항 |
|------|------|--------|
| gender (M/F) | between-subject | 개체 간 오차 |
| method (Trad/Online/Mix) | **within-subject (반복)** | 개체 내 오차 |
| gender × method | 상호작용 | 개체 내 오차 |

---

## 사전 가정 (3가지) — 검정 전 반드시 확인

| 가정 | 검정 | 위배 시 대응 |
|------|------|--------------|
| **정규성** | Shapiro–Wilk (셀별 또는 잔차) | 비모수(Friedman) 전환 |
| **등분산성** (between) | Levene | Welch 보정 / 변환 |
| **구형성(Sphericity)** ⭐ | **Mauchly 검정** | **Greenhouse–Geisser / Huynh–Feldt** 자유도 보정 |

### 구형성(Sphericity)이란?
반복측정 요인의 **모든 수준 쌍 차이(diff)의 분산이 동일**하다는 가정.
$$\mathrm{Var}(Y_i - Y_j) = \text{const}\quad \forall i,j$$
- within 요인이 2수준이면 차이가 한 개뿐 → 구형성 자동 충족 (검정 불필요)
- 3수준 이상이면 Mauchly 검정 필요.
- **Mauchly p > .05 → 구형성 충족** (보정 불필요)
- **p < .05 → 위배** → F검정의 분자/분모 자유도에 보정계수 $\hat\varepsilon$ 곱함
  - $\hat\varepsilon$ 작을수록 위배 심함 ($1/(k-1) \le \hat\varepsilon \le 1$)
  - GG: 보수적, HF: $\hat\varepsilon$ 클 때(>0.75) 권장

---

## SS 분해 · 잔차 유도 *(2026-06-09 세션)*

### 왜 반복측정이 더 예리한가 — 한 줄 요약
독립설계에서 **오차**로 들어갔을 분산을, **개체(subject) SS만큼 떼어내** 분모를 줄인다.
→ $SS_{within}=SS_{개체}+SS_{잔차}$, 분모가 $\sigma^2+\sigma_\pi^2$ → $\sigma^2$로 작아져 검정력↑.

### 모형 (RCBD 관점: 개체=블록, 방법=처리)
$$Y_{ij}=\mu+\tau_j+\beta_i+\varepsilon_{ij}\qquad(\textstyle\sum\tau_j=0,\ \sum\beta_i=0)$$
- $\tau_j$: 처리(방법) 효과 (고정), $\beta_i$: 개체(블록) 효과 — 반복측정에선 랜덤 $\pi_i\sim N(0,\sigma_\pi^2)$
- 평균 기호: $\bar Y_{\cdot j}$(처리평균), $\bar Y_{i\cdot}$(개체평균), $\bar Y_{\cdot\cdot}$(전체평균)

### 핵심 항등식 (편차의 3분할 → 직교)
$$Y_{ij}-\bar Y_{\cdot\cdot}=\underbrace{(\bar Y_{\cdot j}-\bar Y_{\cdot\cdot})}_{\text{처리}}+\underbrace{(\bar Y_{i\cdot}-\bar Y_{\cdot\cdot})}_{\text{개체}}+\underbrace{(Y_{ij}-\bar Y_{\cdot j}-\bar Y_{i\cdot}+\bar Y_{\cdot\cdot})}_{\text{잔차}}$$
교차항이 모두 0(직교) → $SS_T=SS_{처리}+SS_{개체}+SS_{잔차}$
자유도: $nk-1=(k-1)+(n-1)+(n-1)(k-1)$

핵심 분리: $\;\boxed{SS_{within}=SS_{개체}+SS_{잔차}}\;$, $\;k(n-1)=(n-1)+(n-1)(k-1)$

### 잔차 공식은 어디서? (예측값 = 부품 조립)
최소제곱 추정: $\hat\mu=\bar Y_{\cdot\cdot},\ \hat\tau_j=\bar Y_{\cdot j}-\bar Y_{\cdot\cdot},\ \hat\beta_i=\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}$
$$\hat Y_{ij}=\hat\mu+\hat\tau_j+\hat\beta_i=\bar Y_{\cdot j}+\bar Y_{i\cdot}-\bar Y_{\cdot\cdot}$$
$$\therefore\ e_{ij}=Y_{ij}-\hat Y_{ij}=\boxed{\,Y_{ij}-\bar Y_{\cdot j}-\bar Y_{i\cdot}+\bar Y_{\cdot\cdot}\,}$$
**"+전체평균"의 정체**: 두 보너스($\hat\tau,\hat\beta$)가 $\bar Y_{\cdot\cdot}$를 두 번 빼므로 한 번 도로 더해 보정(포함-배제).

### 손풀이 예제 — 친구 5명 × 방법 3수준
| 친구 | M1 | M2 | M3 | 개체평균 |
|------|----|----|----|------|
| A | 5 | 5 | 8 | 6 |
| B | 9 | 13 | 14 | 12 |
| C | 16 | 18 | 20 | 18 |
| D | 22 | 24 | 26 | 24 |
| E | 28 | 30 | 32 | 30 |
| 방법평균 | 16 | 18 | 20 | 전체 18 |

- $SS_T=1124,\ SS_{처리}=40,\ SS_{개체}=1080,\ SS_{잔차}=4$ (A·B 6칸에서만, $1{+}1{+}0{+}1{+}1{+}0$)
- 잔차 예: A·M1 $=5-16-6+18=+1$ → 예측 $18+(-2)+(-12)=4$, 실제 5

| 분석 | 분모 SS | F | 판정 |
|------|---------|---|------|
| 독립(15명 취급) | 1084 (df12) | $20/90.3\approx\mathbf{0.22}$ | 효과 없음(개인차에 묻힘) |
| 반복(같은 5명) | 4 (df8) | $20/0.5=\mathbf{40}$ | 강하게 유의 ✅ |

→ 같은 데이터, 정반대 결론. 개인차 1080을 오차에서 분리한 것이 차이의 전부.

### 잔차의 줄 합·열 합 = 0 (직교성의 정체)
$\sum_j e_{ij}=k\bar Y_{i\cdot}-k\bar Y_{\cdot\cdot}-k\bar Y_{i\cdot}+k\bar Y_{\cdot\cdot}=0$ (열 합도 대칭으로 0).
줄 평균·열 평균을 이미 빼냈으므로 그 방향엔 정보가 없음 → 제약 $n+k-1$개 → 잔차 자유도 $(n-1)(k-1)$.
이 직교 제약이 [[이차형식과 Cochran 정리]]에서 SS의 독립 $\chi^2$ 분해를 보증.

---

## 가정 위배 시 대응 — 심화 *(2026-06-11 세션)*

> 위 "사전 가정" 표의 압축 대응을, **등분산성·정규성** 두 가정에 대해 깊이 있게 보강.
> 공통 원칙: ① **검정 대상은 원자료가 아니라 모형 잔차** ② **p값만이 아니라 위배의 방향·크기**로 실질성 판단 ③ [[중심극한정리 (CLT)]]에 의한 F검정의 강건성을 먼저 고려.

### A. 집단 간 등분산성([[Levene 검정]], between=gender) 위배 시
선택 순서(간명 → 정공법):

1. **분산안정화 변환** — 분산이 평균에 의존하면 로그·√·[[Box-Cox 변환]] 후 재점검. 등분산성과 정규성을 *동시 회복*하는 경우 많음. 비용: 변환 척도 해석.
2. **등분산 미가정 검정** — between 주효과 한정 [[Welch ANOVA]](Welch 1951, Satterthwaite 자유도 보정)·[[Brown-Forsythe 검정]]. 단 상호작용 있는 혼합설계엔 직접 적용 곤란.
3. **이분산을 모형에 명시한 [[혼합효과모형]] (가장 원리적)** — `nlme::lme`의 `weights = varIdent(form=~1|gender)`로 집단별 잔차분산을 추정 → [[일반화최소제곱법 (GLS)]] 틀에서 위배를 모형 일부로 흡수. within 상관도 `correlation=corSymm/corCompSymm`로 동시 처리. 등분산 vs 이분산 모형은 [[우도비 검정 (LRT)]]·AIC로 비교(REML 척도 주의).
4. **강건·비모수** — 절사평균 기반 [[강건 통계 (Robust Statistics)]](`WRS2::bwtrim`), 상호작용 가능한 [[정렬순위변환 (ART)]] ANOVA(`ARTool`), 부트스트랩.

### B. 정규성([[Shapiro-Wilk 검정]]) 위배 시
1. **잔차로 재확인** — 셀별 원점수가 아니라 적합 후 잔차의 Q-Q·검정이 이론적으로 옳음. Shapiro는 n 커지면 과민.
2. **강건성 평가** — 균형설계·큰 표본·중간 비대칭이면 [[중심극한정리 (CLT)]]로 표준 ANOVA 유지 가능.
3. **변환** — 평균-분산 연동형 왜곡이면 [[Box-Cox 변환]]이 정규성+등분산성 동시 해결.
4. **비모수** — 구조별 선택: within만 [[Friedman 검정]], between만 [[Kruskal-Wallis 검정]]/[[Mann-Whitney 검정]], **상호작용 포함 혼합설계는 [[정렬순위변환 (ART)]] ANOVA**(주효과+상호작용 모두 비모수 검정 가능).
5. **강건 통계** — 이상치·두꺼운 꼬리면 절사평균/M-추정(`WRS2`).
6. **순열·부트스트랩** — 분포 가정 없이 F의 경험적 영분포. 반복측정은 **개체 단위 재표집**으로 교환가능성 유지.
7. **분포를 바꾸는 [[일반화선형혼합모형 (GLMM)]]** — 반응변수가 본질적으로 계수형·이항형·양의 왜곡 연속형이면 적절한 분포+[[GLM 연결함수]] 지정(점수 0~100 비율형은 베타회귀 계열).

### 의사결정 한 줄 요약
경미+큰표본 → CLT로 표준 ANOVA · 평균-분산 연동 왜곡 → 변환 · 상호작용 핵심+비정규 → ART · 이상치/두꺼운 꼬리 → 절사평균 강건법 · 반응변수 자체가 비정규 종 → GLMM · 가정 회피 → 순열검정.

### 구형성(within) 위배와 혼동 금지
등분산성·정규성과 **별개 트랙**. within 자유도 보정([[Greenhouse-Geisser 보정]]/[[Huynh-Feldt 보정]]) 또는 구형성 미가정 다변량 접근([[MANOVA]], Pillai·Wilks' Λ). 현 스크립트의 `anova_test(..., correction="auto")`가 자동 적용.

### 디버깅 메모 (오늘 실제 발생)
- `shapiro.test(score)`(점, base R) → 파이프에서 `unused argument` 에러. base는 벡터 1개만 받고 group_by 미인식.
- `shapiro_test`(밑줄, **rstatix**)로 고쳐야 셀별·tidy(`p` 열) 출력. 단 `library(rstatix)` 로드 필수 — 미로드 시 `could not find function`. `suppressPackageStartupMessages({...})`는 패키지 로드 실패 에러까지 가려 뒤 단계가 조용히 깨질 수 있으니 진단 시 직접 `library()` 실행 권장.

### 참고문헌
- Montgomery, *DAE* (8th) §3.4·§3.11(변환)·Ch15 · Welch (1951) *Biometrika* 38 · Box & Cox (1964) *JRSS-B* · Pinheiro & Bates, *Mixed-Effects Models in S* (varIdent) · Conover, *Practical Nonparametric Statistics* (3rd) · Wobbrock et al. (2011) ART, *CHI* · Wilcox, *Robust Estimation and Hypothesis Testing* (4th).

### 후속 탐구 질문 (다음 세션 출발점)
**등분산성 트랙**
- Q1. `nlme::lme`의 `varIdent` 이분산 모형 vs 등분산 모형을 [[우도비 검정 (LRT)]]으로 비교할 때 REML/ML 중 무엇으로 적합해야 타당한가?
- Q2. [[Welch ANOVA]]의 Satterthwaite 분모 자유도 공식 유도와, 이분산이 심할수록 검정력에 주는 영향은?
- Q3. 정규성·등분산성 동시 위배 시 [[정렬순위변환 (ART)]]이 단순 순위변환보다 상호작용 검정에서 우월한 이유(aligning의 수학적 의미)?

**정규성 트랙**
- Q4. 반복측정 순열검정에서 within 라벨을 개체 *내*에서 섞는 것과 개체 *자체*를 섞는 것은 각각 어떤 귀무가설을 검정하나?
- Q5. ART의 효과 분리(aligning)에서 다른 효과 추정치를 빼주는 과정을 수식으로 보면, 단순 순위변환이 상호작용을 왜곡하는 이유는?
- Q6. 반응변수가 0~100 점수일 때 [[Box-Cox 변환]]+정규 ANOVA vs 베타 [[일반화선형혼합모형 (GLMM)]] 중 무엇이 타당하며, 추론 대상(평균 vs 조건부 기댓값)은 어떻게 다른가?

---

## 검정 절차 & R 구현 (rstatix)

```r
library(tidyr); library(rstatix)
long <- wide %>% pivot_longer(c(Tradition,Online,Mix),
                              names_to="method", values_to="score")
# 혼합 ANOVA (Mauchly·GG 보정 자동 포함)
res <- anova_test(long, dv=score, wid=ID, between=gender, within=method)
get_anova_table(res)            # 보정된 ANOVA 표
res$`Mauchly's Test for Sphericity`
# within 주효과 유의 시 사후분석
long %>% pairwise_t_test(score ~ method, paired=TRUE,
                         p.adjust.method="bonferroni")
```

---

## 사후분석 (Post-hoc)

within 요인(method) 주효과가 유의하면, **어느 쌍이 다른지** 본다.
- 반복측정이므로 **paired** 비교 사용
- 다중비교 보정: **Bonferroni**(보수적) 또는 Tukey HSD
- 보고: 조정 p값(p.adj)과 평균차 방향 함께 해석

---

## ADP exam34-문제3 실제 결과 (이 데이터)

**가정 검토**: 정규성 6셀 모두 p>.05 충족 · Levene 모두 p>.05 충족 ·
**Mauchly W=0.964, p=0.506 → 구형성 충족** (보정 불필요)

**혼합 ANOVA**:

| 효과 | F | p | 판정 |
|------|---|---|------|
| gender (주효과) | F(1,38)=1.27 | 0.267 | 유의하지 않음 |
| **method (주효과)** | **F(2,76)=8.69** | **0.0004** | **유의** ✅ |
| gender×method (상호작용) | F(2,76)=0.26 | 0.773 | 유의하지 않음 |

**사후분석 (Bonferroni)**:

| 비교 | 조정 p | 판정 |
|------|--------|------|
| Tradition vs Online | 0.059 | ns |
| Tradition vs Mix | 0.399 | ns |
| **Online vs Mix** | **0.00013** | ***** 유의** |

**해석**: 성별은 성적에 영향 없음. 학습방법은 유의한 차이 존재
→ 핵심은 **Mix(복합, 평균~72.6) > Online(온라인, 평균~65.7)**.
상호작용 없음 → 학습방법 효과는 남녀 공통으로 동일하게 나타남.

---

## 막혔던 포인트 & 튜터 힌트
- ⚠️ 데이터가 wide format → 반드시 long으로 pivot 후 분석.
- ⚠️ 같은 ID가 3방법 모두 측정 → 일반 `aov(score~gender*method)` 쓰면 **틀림**.
  반드시 `wid=ID`로 개체 내 상관 처리.
- ⚠️ within 사후검정은 `paired=TRUE`. 일반 t검정 쓰면 자유도·오차 잘못됨.

## 다요인 상호작용의 해석 위계 (주변성 원칙) *(2026-06-14 세션)*

> Datanovia 삼원 혼합 ANOVA([[Datanovia_Mixed_ANOVA_R_튜토리얼_번역]]) 번역을 계기로, **"상호작용이 유의하면 왜 주효과를 단독 해석하지 않는가"** 를 [[주변성 원칙 (Principle of Marginality)]] 중심으로 정리.

### 핵심 한 줄
**자기를 포함하는 더 높은 차수의 유의한 항이 없을 때만, 그 항을 단독 해석한다.** — 위계 전체를 관통하는 *재귀* 규칙.

### 왜 주효과를 "패스"하는가 (버리는 게 아님)
- ANOVA 주효과 = **나머지 요인 수준에 걸쳐 평균낸** 효과(주변효과).
- 상호작용 유의 = "한 요인 효과가 나머지 조합에 따라 달라진다"는 정의. → 그 평균(주효과)은 **실재하지 않는 가상의 값**이거나, 정반대 효과를 상쇄해 오도.
- 그래서 버리는 게 아니라 **나머지를 고정한 [[단순 주효과 (Simple Main Effect)]]로 조건부 복원** → 번역본의 분해 절차(단순 이원 → 단순단순 주효과 → 단순단순 비교).

### 하향 절차 (삼원 설계 기준)
| 상위 검정 | 다음 단계 |
|-----------|-----------|
| **삼원 유의** | 삼원 분해에서 멈춤(세 번째 요인 접기 금지) |
| **삼원 비유의** | 세 이원 상호작용 점검 → 유의한 이원은 분해(세 번째 요인 접기 정당), 비유의 이원의 요인만 주효과 후보 |
| 주효과 단독해석 가능 조건 | **그 요인이 든 모든 상호작용이 비유의**일 때만 |

- 삼원 비유의가 "세 번째 요인 접기"를 정당화하는 근거: 이원 패턴이 세 번째 요인 수준에 걸쳐 **일관**됨을 뜻하므로 평균이 거짓말하지 않음.

### 회귀 ↔ ANOVA 연결 (코딩의 차이일 뿐)
동일 모형 $Y=\beta_0+\beta_1 A+\beta_2 B+\beta_3(A\times B)$를 다른 [[대비 코딩 (Contrast Coding)]]으로 본 것:
- **처치(dummy) 코딩**(회귀 기본): $\beta_1$ = "B가 기준(=0)일 때 A의 *조건부*효과" → 기준 바꾸면 값 변함.
- **효과(sum-to-zero) 코딩**(ANOVA): $\beta_1$ = "B 전 수준 평균낸 *주변*효과" → 기준 불변. [[Type III 제곱합]]이 이 등가중을 사용.

### 심슨의 역설 = 가중치 충돌
주변효과 $\bar\mu_A=\sum_k w^A_k\mu_{Ak}$. 모든 층에서 $\mu_{Ak}>\mu_{Bk}$여도 **$w^A_k\neq w^B_k$가 층과 상관(불균형 설계)** 이면 $\bar\mu_A<\bar\mu_B$로 부호 역전.
→ 등가중([[Type III 제곱합]], $w_k=1/K$)이 역전 차단. "어떤 가중치로 평균낼 것인가"의 문제.

### 다중비교·검정력 주의
- **Bonferroni는 요인별(가족별)로 따로** 적용. 세 요인 전체를 한 가족으로 합치면 과도하게 보수적 → 검정력 손실. ([[가족별 오류율 (Family-wise Error Rate)]]의 "가족"=하나의 연구질문 단위)
- **"삼원 비유의 = 효과 없음"은 위험**: 증거의 부재 ≠ 부재의 증거([[제2종 오류 (Type II Error)]]). 고차 상호작용은 구조상 검정력 낮음(차이의 차이의 차이) → 효과크기(ges·partial $\eta^2$)·CI 병행 보고.
- **전 셀 일원 다중비교는 부적절**: 비교 폭발·구조 상실·교란된 대비(여러 요인 동시 차이)·모형오차 비효율. 위계적 분해는 *고정*을 통해 교란 없는 해석 가능 비교만 수행.

### 막혔던/짚은 포인트 (이번 세션 Q&A)
- 주효과를 "패스"한다는 표현의 오해 → "조건부 복원"으로 교정.
- 처치코딩에서 기준 바꾸면 $\beta_1$ 변하는데 ANOVA 주효과는 불변인 이유 = 등가중 평균이라서.
- 단순단순 비교가 교란 없는 이유 = 나머지 요인을 *고정*했기 때문(주변화 아님).

### 후속 탐구 질문 (다음 세션 출발점)
**위계·코딩 트랙**
- Q1. 이원으로 내려가도 주변성 원칙은 재귀 적용되는가? (→ 그렇다: 이원→주효과에서 한 번 더)
- Q2. 효과코딩 vs 처치코딩에서 상호작용 계수 $\beta_3$의 의미 차이는?
- Q3. 비계층적 모형(주효과 없이 상호작용만)이 부적절한 근거 = 모형의 불변성(invariance) 관점?

**심슨·다중비교·검정력 트랙**
- Q4. Type III가 심슨 역전을 막는다면, 반대로 Type I(순차) SS를 일부러 써야 타당한 상황은?
- Q5. 고차 상호작용 저검정력 보완책 — 표본 증대 외 효과크기 사전지정·축소추정(shrinkage)?
- Q6. "가족(family)" 경계의 자의성을 막는 사전등록(pre-registration)의 역할?
- Q7. 삼원 비유의 시 "세 번째 요인 접기"의 정당성을, 동등성 검정(equivalence test)으로 보강할 수 있는가?

---

## 연결 개념 (클러스터 참조)
- Cluster B(이차형식): [[ANOVA SS 분해]] → 개체 SS를 추가로 분리하는 것이 반복측정
- [[랜덤효과 모형과 분산성분 추정 (REML)]] — 개체를 random effect로 보는 관점
- [[이원 ANOVA와 교호작용 (Interaction)]] — 상호작용 해석의 기초
- [[Datanovia_Mixed_ANOVA_R_튜토리얼_번역]] — **이원 → 삼원 혼합설계** 확장(개체간 2+개체내 1, 개체간 1+개체내 2)과 단순·단순단순 효과 분해 절차의 R(`rstatix`) 실습 참조자료

## 참고 교재 페이지
- Montgomery §14 (반복측정), §5 (이원ANOVA), §3.5 (다중비교) — p.___
- Hogg §9.2, §9.5 — p.___

---

## 🔁 이어가기 — 2026-06-11 세션
1. **대상**: `[[반복측정 설계와 구형성 가정 (Mauchly 검정)]]` 가정 위배 대응 + 학습 인프라 · 실험설계 Ch14 · 트랙 A
2. **오늘 한 것**: ⓐ 본 노트에 "가정 위배 시 대응—심화"(등분산성·정규성) 섹션 + 후속질문 Q1~Q6 보강 ⓑ `exam34_problem3` 디버깅(`shapiro.test`(점,base) → `shapiro_test`(밑줄,rstatix), 패키지 미로드·`suppressPackageStartupMessages` 함정) ⓒ 세션 연속성 도구 신설: `[[이어가기_handoff_템플릿]]`·`[[MOC_이차형식]]` ⓓ 커리큘럼↔MOC 4단 위계 정리
3. **핵심 상태** ⭐: 도구·문서 골격 완성. **다음 줄부터**: 세 파일(대시보드·커리큘럼·MOC)의 위키링크 *이름 불일치*가 그래프를 조각냄 → 정규 이름 통일 + alias 흡수 작업이 미착수로 남음
4. **막힌 지점**: 같은 개념이 `[[이차형식과 Cochran 정리]]` / `[[이차형식의 분포와 독립성 (Cochran 정리)]]` 등 3가지 이름으로 흩어짐 — 정규 이름 기준 파일을 무엇으로 할지 미결정
6. **다음 출발점** →: Cluster B 개념들의 정규 이름을 커리큘럼 기준으로 통일하고 대시보드·MOC 표기 정렬 (또는 `[[이차형식]]` 원자노트 작성 시작)
7. **열린 질문**: Q1 정규화 기준 파일 선정·alias 흡수 / Q2 커리큘럼 vs MOC 단일 진실원천 / Q3 6개 MOC 거느리는 커리큘럼 자동목차화
8. **연결**: `[[MOC_이차형식]]` · `[[01_Concept_Connection_Curriculum]]` · `[[ANOVA SS 분해]]`

---

## 🔁 이어가기 — 2026-06-14 세션

1. **대상**: 다요인 ANOVA 해석 위계([[주변성 원칙 (Principle of Marginality)]]) → 고정/랜덤효과 → 오차 독립 가정 → [[일반화최소제곱법 (GLS)]]까지 개념 다리 놓기. 실험설계 Ch14에서 **회귀분석 기초로 자연스럽게 넘어가는 길** 발견.

2. **오늘 한 것**:
   - ⓐ Datanovia "Mixed ANOVA in R" 전문 한국어 번역 → 별도 참조노트 [[Datanovia_Mixed_ANOVA_R_튜토리얼_번역]] 신설(실험설계법 폴더), 본 노트와 상호링크.
   - ⓑ 본 노트에 "**다요인 상호작용의 해석 위계(주변성 원칙)**" 섹션 추가: 상호작용 유의 시 주효과 단독해석 금지 이유, 삼원→이원→주효과 하향 분해, 회귀↔ANOVA 코딩(처치 vs 효과), 심슨 역설=가중치 충돌, Bonferroni 요인별 적용, 고차 상호작용 저검정력.
   - ⓒ **반대 방향 오류** 정리: 독립 자료를 반복으로 돌리면 → 잡음뿐인 개체 SS가 자유도만 낭비 → 검정력 손실(보수적), 제1종 오류는 [[이차형식과 Cochran 정리]]로 보존. (노트의 친구 예제 = 반대 방향: 반복→독립.)
   - ⓓ **고정효과 vs 랜덤효과**: 고정=평균구조 $E[Y]$, 랜덤=분산·공분산 구조 $\mathrm{Var}[Y]$. 랜덤효과 = 분산을 층으로 분해(variance component) + 개체 내 상관 유발(ICC, [[복합대칭 (Compound Symmetry)]]).
   - ⓔ **오차 독립 가정 → GLS**: 김충락 교재 $\mathrm{Var}(\boldsymbol\epsilon)=\sigma^2\mathbf{I}$의 *비대각선 0*이 독립가정. 반복측정 랜덤효과가 비대각선을 $\sigma_b^2$로 채워 깸 → OLS가 BLUE 아님([[Gauss-Markov 정리]] 전제 붕괴) → $\mathbf{V}\neq\mathbf{I}$ 다루는 GLS 등판([[Aitken 정리]]). OLS는 GLS의 $\mathbf{V}=\mathbf{I}$ 특수사례.

3. **핵심 상태** ⭐: 실험설계(반복측정)와 회귀분석(가정·GLS)을 잇는 개념 다리 완성. **다음 세션은 회귀분석 가정부터 새로 시작** — 오늘 ⓔ에서 도달한 "$\sigma^2\mathbf{I}$ 가정"이 그 진입점.

4. **다음 출발점** →: 김충락·강근석 『회귀분석』의 **선형모형 기본 가정**(선형성·$E(\epsilon)=0$·등분산·무상관·(정규성))을 처음부터 체계적으로. 오늘 GLS에서 거꾸로 온 길을, 정공법으로 다시 내려가기.

5. **다음 세션에 이어갈 열린 질문(오늘 미해결)**:
   - GLS 변환 $\mathbf{L}^{-1}$ 후 오차 공분산이 $\sigma^2\mathbf{I}$로 돌아오는 과정(탈상관) 손유도.
   - FGLS(추정된 $\mathbf{V}$)의 추가 불확실성.
   - Gauss-Markov·Aitken에서 정규성이 *불필요*하고, 정규성은 검정·구간추정 단계에서 비로소 필요해지는 경계.

6. **만들 빈 노트(흐린 링크)**: [[주변성 원칙 (Principle of Marginality)]] · [[급내상관계수 (ICC)]] · [[복합대칭 (Compound Symmetry)]] · [[Aitken 정리]] · [[심슨의 역설]] · [[Type III 제곱합]] · [[대비 코딩 (Contrast Coding)]]

7. **연결**: [[Datanovia_Mixed_ANOVA_R_튜토리얼_번역]] · [[일반화최소제곱법 (GLS)]] · [[Gauss-Markov 정리]] · [[랜덤효과 모형과 분산성분 추정 (REML)]] · [[이차형식과 Cochran 정리]]
