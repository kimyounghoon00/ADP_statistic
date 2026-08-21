---
aliases: [진도 대시보드, Progress Dashboard]
tags: [통계학, Dashboard, Hub]
date_created: 2026-06-07
date_modified: 2026-08-21
---

# 📊 통계학 전체 학습 진행 현황 (Progress Dashboard)

사전식(랜덤) 학습 | 수준: **대학원 (Graduate)** — 엄밀한 수학적 유도 및 증명 위주

> 🔗 **핵심 학습 전략**: 과목 경계를 넘어 개념의 뿌리로 공부한다.
> → [[01_Concept_Connection_Curriculum]] 참조
>
> | 클러스터 | 핵심 연결 고리 |
> |----------|----------------|
> | **A. 추정 효율성** | `[[CRLB]]` ↔ `[[Gauss-Markov 정리]]` ↔ `[[UMVUE]]` |
> | **B. 이차형식** | `[[Cochran 정리]]` ↔ `[[Hat Matrix]]` ↔ `[[ANOVA SS 분해]]` |
> | **C. 우도 추론** | `[[Neyman-Pearson]]` ↔ `[[LRT]]` ↔ `[[F-검정]]` ↔ `[[GLM]]` |
> | **D. 지수족·GLM** | `[[지수족]]` ↔ `[[GLM 연결함수]]` ↔ `[[켤레 사전분포]]` |
> | **E. 투영·LSE** | `[[최소제곱추정량(LSE)]]` ↔ `[[Hat Matrix]]` ↔ `[[PCA]]` |
> | **F. 점근이론** | `[[중심극한정리 (CLT) 와 Delta Method]]` ↔ `[[MLE 점근]]` ↔ `[[단위근 검정]]` |
> | **G. 비모수** | `[[경험분포함수(EDF)와 Glivenko-Cantelli]]` ↔ `[[순위 검정 — 부호·Wilcoxon·Mann-Whitney]]` ↔ `[[부트스트랩과 잭나이프]]` (K&V, 2026-07-05 신설) → `[[MOC_비모수]]` |

---

## 🧭 현재 집중 학습 위치 (Current Focus)
*(2026-08-21 갱신 — 6/29 이후 6개 세션이 미기록이던 것을 무결성 검토에서 복원)*

* **과목**: 회귀분석 **Ch4 회귀진단** (Cluster B·E) — 잔차 가정 3축 완주 후 ADP 기출 실전 적용 중
* **최근 완료**: `[[Ch04_ADP32_Boston_회귀가정검토]]` **문제 1 완료** (2026-08-02) — 4가지 가정 전수 검정, 전부 위배 + `medv==50` 상한절단 16건 발견. 이론 토대 `[[잔차의 직교성과 진단 그림의 가로축]]` 완결
* **다음 출발점 — 두 갈래 중 택1**
  1. **(직전 흐름)** `[[Ch04_ADP32_Boston_회귀가정검토]]` 열린 질문 **Q1**(순서 없는 자료에 DW를 어떻게 쓸 것인가) 해결 → **문제 2**(상관행렬·`[[분산팽창인자(VIF)]]`) 진입
  2. **(6/29 확정분, 보류 중)** `[[이차형식]]` — 교재 **§3.4 이차형식과 제곱합의 분포(책 114–119, Ch3)**. ANOVA·F-검정의 엔진 → `[[이차형식과 Cochran 정리]]`. Cluster B `[[MOC_이차형식]]`. 핸드오프 `[[_세션핸드오프_2026-06-29_Aitken_B완결]]`
* **완결된 가지**: `[[Aitken 정리]]` GLS=BLUE (2026-06-29, L·U·B + 유일성) · `[[일반화최소제곱(GLS)]]` · 잔차 3축(`[[Ch04_잔차가정검정_백지유도]]` §0–§2, `[[Breusch-Pagan 검정]]`, `[[Durbin-Watson 검정]]`, `[[Breusch-Godfrey 검정]]`)
* **미완으로 남은 것**: `[[Ch04_잔차가정검정_백지유도]]` **§3(독립성) 본문이 비어 있음** — DW 노트로 분리돼 있으니 §3에 링크 한 줄로 닫을 것 · `[[Cook's Distance 유도]]`(진단 4축째) 미착수

---

## 📚 교재 목록 (Textbooks)

| 과목 | 교재 | 비고 |
|------|------|------|
| 수리통계학 | Hogg, McKean & Craig, *Introduction to Mathematical Statistics*, 8th ed. (Pearson, 2019) | Ch1~Ch10 |
| 회귀분석 | **김충락·강근석, 『회귀분석』 2판** | Ch1~Ch12 + 부록 A·B (총 506p, 책쪽+16=PDF쪽 → `regression_김충락/chapter_page_mapping.json`) |
| 실험설계법 | Montgomery, *Design and Analysis of Experiments*, 8th ed. (Wiley, 2012) | Ch1~Ch15 (PDF쪽 = 책쪽+15) |
| **범주형자료분석** | **Agresti, *Categorical Data Analysis*, 3rd ed. (2013)** + *An Introduction to CDA*, 2nd ed. | Ch11 대응쌍 진행 (2026-07-14) |
| 다변량분석 | Johnson & Wichern, *Applied Multivariate Statistical Analysis*, 6th ed. (Pearson) | Ch1~Ch12 ⭐추천 |
| 시계열분석 | Levendis, *Time Series Econometrics: Learning Through Replication* | BU EC-490 강의노트 Ch1~Ch12 |
| 비모수통계 | **Kvam & Vidakovic, *Nonparametric Statistics with Applications…* (Wiley)** — 주교재 (2026-07-05 편입) | Ch5~Ch15, 보조: Hogg 8판 §10 |
| 베이즈통계 | (교재 미업로드 — 추후 추가) | — |

> ⚠️ **2026-08-21**: 위 교재 PDF는 **저작권 자료라 저장소에서 제외**돼 있다(`.gitignore`). 로컬 볼트에만 존재하며, 노트는 쪽수·절 번호로만 인용한다. → `[[2026-08-21_전체_무결성]]` F-01

---

## 📁 업로드된 자료 현황

> 🔒 **로컬 볼트 전용** — 아래 PDF·스캔본은 저작권 자료라 **git 저장소에는 올리지 않는다**(`.gitignore`). 저장소에는 노트(.md)·스크립트·자체 생성 그림만 들어간다.

```
튜터워크스페이스/                                        (로컬 전용 ⬇)
├── introduction_to_mathematical_statistics_8.pdf        ← Hogg 8판
├── Design_and_Analysis_of_Experiments_Wiley_2012.pdf   ← Montgomery 8판
├── nonparametric_statistics_with_applications….pdf     ← Kvam & Vidakovic (offset 11)
├── Agresti_Categorical_Data_Analysis_3e.pdf            ← Agresti 3판 (offset 18)
├── regression_김충락/
│   ├── 회귀분석_김충락.pdf   (= Regression Analysis_note I·II 합본, 506p)
│   ├── 회귀분석_chapters/  (ch01~ch12 챕터별 분할 — split_by_chapter.py 산출)
│   └── regressiona_Analysis_midandfinal_term_김충락/  (기출문제)
└── timeseries/   (Levendis 강의노트)
    ├── Ch1~2: 기초·정상성
    ├── Ch3: ARMA 모형선택 (Wold 분해정리)
    ├── Ch4~7: ARIMA, 단위근, 예측
    ├── Ch8a: 추가 주제
    ├── Ch9: ARCH-GARCH
    ├── Ch10: VAR
    └── Ch12: 공적분 (Cointegration)
```

---

## 🧠 트랙 A: 핵심 개념 유도 진행도
*(튜터워크스페이스에서 진행. 완료 시 `[x]` 처리)*

---

### 📗 수리통계학 — Hogg 8판 챕터 순서

#### Ch1. Probability and Distributions (확률과 분포)
- [ ] `[[확률측도와 공리계 (Kolmogorov)]]` §1.3
- [ ] `[[조건부 확률과 독립성]]` §1.4
- [ ] `[[기댓값과 적률생성함수 (MGF)]]` §1.8–1.9
- [ ] `[[Markov 부등식과 Chebyshev 부등식]]` §1.10

#### Ch2. Multivariate Distributions (다변량 분포)
- [ ] `[[결합분포와 주변분포]]` §2.1
- [ ] `[[조건부 기댓값과 반복기댓값 법칙 (LIE)]]` §2.3
- [ ] `[[공분산과 상관계수]]` §2.5

#### Ch3. Special Distributions (특수분포)
- [ ] `[[지수족 (Exponential Family) 정의와 성질]]` §3.6 (t, F, χ²)
- [ ] `[[다변량 정규분포 — 二次형식과 독립성]]` §3.5

#### Ch5. Consistency & Limiting Distributions (점근이론)
- [ ] `[[확률수렴과 분포수렴]]` §5.1–5.2
- [ ] `[[중심극한정리 (CLT) 와 Delta Method]]` §5.3, §5.2.2

#### Ch6. Maximum Likelihood Methods (최대우도법)
- [ ] `[[최대우도추정량 (MLE) 유도와 불변성]]` §6.1
- [ ] `[[Fisher 정보량과 Rao–Cramér 하한 (CRLB)]]` §6.2
- [ ] `[[우도비 검정 (LRT) 과 점근 카이제곱 분포]]` §6.3, §6.5
- [ ] `[[다모수 MLE — Score 벡터와 Fisher 정보행렬]]` §6.4

#### Ch7. Sufficiency (충분통계량)
- [ ] `[[충분통계량과 인수분해 정리 (Fisher-Neyman)]]` §7.2
- [ ] `[[Rao-Blackwell 정리]]` §7.3
- [ ] `[[완비통계량 (Complete Statistic) 과 Lehmann-Scheffé 정리]]` §7.4
- [ ] `[[지수족과 완비충분통계량]]` §7.5
- [ ] `[[최소충분통계량과 보조통계량 (Ancillary)]]` §7.8

#### Ch8. Optimal Tests (최적검정)
- [ ] `[[Neyman-Pearson 보조정리]]` §8.1
- [ ] `[[균일최강력검정 (UMP Test)]]` §8.2
- [ ] `[[우도비 검정 (LRT) — 정규분포 적용]]` §8.3

#### Ch9. Normal Linear Models (정규선형모형)
- [ ] `[[일원 ANOVA 제곱합 분해 — Hogg §9.2]]`
- [ ] `[[이원 ANOVA와 교호작용 — Hogg §9.5]]`
- [ ] `[[이차형식의 분포와 독립성 (Cochran 정리) — Hogg §9.8–9.9]]`

#### Ch10. Nonparametric Statistics (비모수 — Hogg §10)
- [ ] `[[부호검정과 Wilcoxon 부호순위검정]]` §10.2–10.3
- [ ] `[[Mann-Whitney-Wilcoxon 검정]]` §10.4
- [ ] `[[점근상대효율 (ARE) — 비모수 vs 모수]]` §10.2.1, §10.3.1

---

### 📘 회귀분석 — 김충락·강근석 『회귀분석』 2판

#### Ch1~2. 단순선형회귀
- [ ] `[[최소제곱추정량(LSE)]]` (stub 2026-08-21 — 본문 미완)
- [ ] `[[회귀계수의 불편성 증명]]` (stub 2026-08-21)
- [ ] `[[회귀계수의 분산 유도]]` — 단순회귀판 통과분은 `주차별/01주차_단순회귀LSE/08_정리노트.md`
- [ ] `[[신뢰구간 및 예측구간의 분산 차이]]`

#### Ch3~4. 중선형회귀 · 회귀진단
- [x] `[[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]]` ✅ 2026-06-29 (모수/추정량 구분, $\sigma^2 I$ 구조)
- [x] **잔차 가정 3축 완주** ✅ — `[[Ch04_잔차가정검정_백지유도]]` §0 잔차 성질(6/21) → §1 정규성·Shapiro–Wilk(6/23) → §2 등분산 `[[Breusch-Pagan 검정]]`(6/23) → §3 독립성 `[[Durbin-Watson 검정]]`·`[[Breusch-Godfrey 검정]]`(6/28)
- [x] `[[잔차의 직교성과 진단 그림의 가로축]]` ✅ 2026-08-02 ($\hat y^\top e=0$ → 가로축이 $\hat y$ 인 이유)
- [x] `[[Ch04_ADP32_Boston_회귀가정검토]]` **문제 1** ✅ 2026-08-02 (ADP 32회, 4가정 전수검정 — 전부 위배)
- [ ] `[[Gauss-Markov 정리]]` (stub — BLUE 증명 미착수. ⚠️ 교재 위치 Ch2/Ch3 확인 필요)
- [ ] `[[Hat Matrix]]` (stub 2026-08-21 — 멱등·대칭 유도 미완)
- [ ] `[[이차형식]]` → `[[이차형식과 Cochran 정리]]` (stub 2026-08-21 — **다음 출발점 후보**)
- [ ] `[[Cook's Distance 유도]]` (진단 4축째, 미착수) · `[[Ch04_ADP32_Boston_회귀가정검토]]` 문제 2·3

#### Cluster A 효율성 가지 (교재 외 확장 포함)
- [x] `[[일반화최소제곱(GLS)]]` ✅ 2026-06-28 (LSE 붕괴 → 표백변환 → 공식)
- [x] `[[Aitken 정리]]` ✅ 2026-06-29 (GLS=BLUE, L·U·B + 유일성 완결)
- [ ] `[[가중최소제곱(WLS)]]` (교재 §6.3, 책 253–254) · `[[FGLS]]`
- [ ] `[[크라메르-라오 하한 (CRLB)]]` (stub 2026-08-21 — Hogg §6.2)

#### Ch5~7. 변수선택 · 편의추정
- [x] `[[Type I·II·III 제곱합과 부분 F-검정]]` · `[[Type II 제곱합 (정식화)]]` · `[[Montgomery 불균형·공변량 ANOVA와 Type I·II·III]]` ✅ 2026-06-15~18 (튜터 초안 — 학습자 백지유도 대기)
- [x] `[[누락변수 편의와 유의성 반전]]` ✅ 2026-07-19 (튜터 초안 — OVB·억제·교란·매개, 보호검정)
- [ ] `[[일반선형가설의 F 통계량 도출]]` (stub — 골격만, 백지유도 대상)
- [ ] `[[AIC, BIC 유도와 변수선택 기준]]` · `[[Mallows Cp]]` (stub)
- [ ] `[[Ridge 회귀와 편향-분산 트레이드오프]]`
- [ ] `[[다중공선성]]` · `[[분산팽창인자(VIF)]]` 본문 (stub 상태)

#### Ch8~12. GLM · 비선형 · 비모수 회귀
- [ ] `[[로지스틱 회귀와 MLE 유도]]`
- [ ] `[[포아송 회귀와 연결함수]]`
- [ ] `[[Cox 비례위험모형 (중도절단자료)]]`

---

### 📙 실험설계법 — Montgomery 8판 챕터 순서

#### Ch2~3. 단일요인 실험 · 일원 ANOVA
- [ ] `[[일원 ANOVA 제곱합 분해 — Montgomery §3]]`
- [ ] `[[비중심 F분포와 검정력 (Power)]]` §3.4
- [ ] `[[다중비교 — Tukey, Bonferroni, Fisher LSD]]` §3.5

#### Ch4. 블록설계 (Blocking)
- [ ] `[[난괴법 (RCBD) — 블록효과 분리]]` §4.1
- [ ] `[[라틴방격 설계 (Latin Square)]]` §4.2
- [ ] `[[그레코-라틴방격 설계]]` §4.3

#### Ch5~6. 요인설계 · 2^k 설계
- [ ] `[[이원 ANOVA와 교호작용 (Interaction) — Montgomery §5]]`
- [ ] `[[완전요인설계 (2^k Design) — 주효과와 교호작용 추정]]` §6
- [ ] `[[정규확률도를 이용한 유의효과 선별]]` §6.3

#### Ch7~8. 블록화 · 부분요인설계
- [ ] `[[혼동 (Confounding) 과 블록화 — 2^k 설계]]` §7
- [ ] `[[부분요인설계 (2^{k-p}) 와 해상도 (Resolution)]]` §8
- [ ] `[[별칭구조 (Alias Structure) 와 생성관계]]` §8.3

#### Ch9~10. 반응표면법 (RSM)
- [ ] `[[중심합성설계 (CCD) 와 회전가능성]]` §11
- [ ] `[[반응표면 최적화 — 정류점 분석 (Canonical Analysis)]]` §11.4

#### Ch13~15. 랜덤효과 · 혼합모형 · 반복측정
- [ ] `[[랜덤효과 모형과 분산성분 추정 (REML)]]` §13 (+ §13.5 EMS 규칙)
- [x] `[[반복측정 설계와 구형성 가정 (Mauchly 검정)]]` **§15.4**(책 677–679) ✅ 2026-06-09 (SS 분해·잔차 유도) → 2026-06-11 가정 위배 대응 심화 → 2026-06-14 주변성 원칙 → 2026-07-17 §15.4·§14.4 절 대조
  - ⚠️ 옛 표기 "§14 = 반복측정"은 **오기**였다(2026-07-15 목차 대조). Ch14는 *Nested and Split-Plot*, 반복측정 정본은 §15.4. 혼합설계 ≡ split-plot(§14.4) 이라 파일명 `Ch14_…` 는 링크 보존을 위해 유지.

---

### 📗 범주형자료분석 — Agresti 3판 *(2026-07-14 신설 — 대시보드에 누락돼 있던 과목)*

#### Ch11. 대응쌍 모형 (Matched Pairs)
- [x] `[[McNemar 검정]]` ✅ 2026-07-14 (주변동질성 ⟺ 대칭성, 스코어 검정 $z_0^2\sim\chi^2_1$, 소표본=부호검정, CMH 동치)
- [x] `[[Cohen의 kappa (관측자 일치도)]]` ✅ 2026-07-14 (우연 보정, Fleiss 분산, 가중 kappa, 준독립·준대칭 모형)
- [ ] `[[대칭성·준대칭성·주변동질성 모형]]` ($I\times I$ 확장, §11.3–11.4)
- [ ] `[[조건부 로지스틱 회귀]]` (§11.2)

> 📌 이 과목은 아직 커리큘럼 클러스터 A~G에 매핑되지 않았다 → 다음 허브 세션에서 결정할 것 (교차점: McNemar↔Cluster C·G, kappa↔Cluster D). `[[2026-08-21_전체_무결성]]` F-13

---

### 📕 다변량분석 — Johnson & Wichern 6판

#### Ch2~3. 다변량 정규분포 · 표본추론
- [ ] `[[다변량 정규분포 — 밀도함수, 조건부 분포, 편상관]]` J&W §4
- [ ] `[[Wishart 분포와 표본공분산행렬의 분포]]` §7.2
- [ ] `[[Hotelling T² 검정과 신뢰타원]]` §5

#### Ch4~5. 평균벡터 비교
- [ ] `[[MANOVA — Wilks' Λ, Pillai, Roy 검정통계량]]` §6
- [ ] `[[프로파일 분석 (Profile Analysis)]]` §6.5

#### Ch6. 주성분분석 (PCA)
- [ ] `[[PCA — 스펙트럼 분해와 분산 설명비]]` §8
- [ ] `[[상관행렬 기반 PCA vs 공분산행렬 기반 PCA]]` §8.3

#### Ch7. 요인분석 (Factor Analysis)
- [ ] `[[요인분석 — 직교회전 (Varimax) 과 요인부하량]]` §9

#### Ch8. 정준상관분석 (CCA)
- [ ] `[[정준상관분석 — 정준변량과 정준상관계수]]` §10

#### Ch9~11. 분류 · 군집
- [ ] `[[판별분석 (LDA) — Fisher 판별함수와 오분류율]]` §11
- [ ] `[[이차판별분석 (QDA) 와 정규분포 가정]]` §11.4
- [ ] `[[군집분석 — k-means, 계층적 클러스터링, 덴드로그램]]` §12

---

### 📓 시계열분석 — Levendis (BU EC-490 강의노트)

#### Ch1~2. 기초 · 정상성
- [ ] `[[정상성 (Stationarity) 조건과 검정]]` Ch1~2
- [ ] `[[자기상관함수 (ACF) 와 편자기상관함수 (PACF)]]` Ch2

#### Ch3. ARMA 모형
- [ ] `[[Wold 분해정리와 ARMA(p,q) 표현]]` Ch3
- [ ] `[[ARMA 모형 — Yule-Walker 방정식]]` Ch3

#### Ch4~7. ARIMA · 단위근 · 예측
- [ ] `[[ARIMA 차분과 단위근 검정 (ADF, PP 검정)]]` Ch4
- [ ] `[[최적예측과 예측구간 — Box-Jenkins 절차]]` Ch5~7

#### Ch8~9. 변동성 모형
- [ ] `[[ARCH-GARCH 모형과 조건부 분산 추정]]` Ch9

#### Ch10. 다변량 시계열
- [ ] `[[VAR 모형과 그레인저 인과성 (Granger Causality)]]` Ch10
- [ ] `[[충격반응함수 (IRF) 와 분산분해 (FEVD)]]` Ch10

#### Ch12. 공적분
- [ ] `[[공적분 (Cointegration) 과 오차수정모형 (VECM)]]` Ch12
- [ ] `[[Johansen 공적분 검정]]` Ch12

---

### 📔 베이즈통계 *(교재 미업로드)*

- [ ] `[[사전분포와 사후분포 — 켤레 사전 (Conjugate Prior)]]`
- [ ] `[[베이즈 추정량과 최소기대손실]]`
- [ ] `[[마르코프 연쇄 몬테카를로 (MCMC) — Metropolis-Hastings]]`
- [ ] `[[깁스 샘플러 (Gibbs Sampler)]]`
- [ ] `[[베이즈 모형 선택 — Bayes Factor]]`
- [ ] `[[계층 베이즈 모형 (Hierarchical Bayes)]]`

---

## 📝 트랙 B: 과목별 연습문제 채점 진행도
*(채점워크스페이스에서 진행. 통과 시 `[x]` 처리)*

### 수리통계학 (Hogg 8판)
- [ ] Ch1 확률·분포 — 점수: ___
- [ ] Ch2 다변량 분포 — 점수: ___
- [ ] Ch3 특수분포 — 점수: ___
- [ ] Ch5 점근이론 — 점수: ___
- [ ] Ch6 MLE — 점수: ___
- [ ] Ch7 충분통계량 — 점수: ___
- [ ] Ch8 최적검정 — 점수: ___
- [ ] Ch9~10 — (미시작)

### 회귀분석 (김충락)
- [ ] Ch1~2 단순회귀 — 점수: ___
- [ ] Ch3~4 중선형·진단 — 점수: ___
- [ ] Ch5~7 변수선택·공선성 — 점수: ___
- [ ] Ch8~12 GLM·비선형 — (미시작)

### 실험설계법 (Montgomery 8판)
- [ ] Ch2~3 ANOVA — 점수: ___
- [ ] Ch4 블록설계 — 점수: ___
- [ ] Ch5~6 요인설계 — 점수: ___
- [ ] Ch7~8 부분요인설계 — 점수: ___
- [ ] Ch9~14 RSM·혼합모형 — (미시작)

### 다변량분석 (Johnson & Wichern 6판)
- [ ] Ch4~5 다변량 추론 — 점수: ___
- [ ] Ch6 MANOVA — 점수: ___
- [ ] Ch8~9 PCA·요인분석 — 점수: ___
- [ ] Ch10~12 CCA·판별·군집 — (미시작)

### 시계열분석 (Levendis)
- [ ] Ch1~2 정상성 — 점수: ___
- [ ] Ch3 ARMA — 점수: ___
- [ ] Ch4~7 ARIMA·예측 — 점수: ___
- [ ] Ch9~12 GARCH·VAR·공적분 — (미시작)

### 베이즈통계
- [ ] 사전·사후분포 — 점수: ___
- [ ] MCMC·모형선택 — (미시작)

---

## 🗓️ 세션 기록 (Session Log)

| 날짜 | 작업 내용 |
|------|-----------|
| 2026-06-07 | 대시보드 초기 구성 (회귀분석 → 통계학 전체 확장) |
| 2026-06-07 | 교재 확인 및 반영: Hogg 8판, Montgomery 8판, Levendis 시계열, Johnson & Wichern 다변량 추천 |
| 2026-06-07 | 트랙 A: Hogg·Montgomery 챕터 순서로 재정렬, 시계열 공적분·VECM 항목 추가 |
| 2026-06-09 | [트랙 A] 실험설계법 Ch14 `[[반복측정 설계와 구형성 가정 (Mauchly 검정)]]` 유도 — 반복측정 ANOVA의 `[[ANOVA SS 분해]]`에서 개체(subject) SS가 오차에서 분리되는 과정($SS_{within}=SS_{개체}+SS_{잔차}$), 잔차 공식 $e_{ij}=Y_{ij}-\bar Y_{\cdot j}-\bar Y_{i\cdot}+\bar Y_{\cdot\cdot}$를 RCBD 모형에서 유도. 5명×3수준 손풀이 예제(독립 F≈0.22 vs 반복 F=40)로 검정력 이득 확인 |
| 2026-06-11 | [트랙 A] Ch14 정리노트에 **가정 위배 대응(등분산성·정규성) 심화** 섹션 보강 + `exam34_problem3` R 디버깅(`shapiro.test`→`shapiro_test`, rstatix 로드). **학습 인프라 신설**: `[[이어가기_handoff_템플릿]]`(세션 연속성)·`[[MOC_이차형식]]`(Cluster B 허브). 커리큘럼↔MOC 4단 위계 정리. ⚠️ **다음 출발점**: 세 파일 위키링크 *이름 불일치* 정규화(정규명+alias) — 미착수 |
| 2026-06-12 | [Hub] 세션 시작 — 오늘 목표: `[[이차형식과 Cochran 정리]]` 자유도 분해 (트랙 A). 튜터워크스페이스로 라우팅. Cluster B (`[[Cochran 정리]]` ↔ `[[Hat Matrix]]` ↔ `[[ANOVA SS 분해]]`) 연결 심화 |
| 2026-06-28 | [트랙 A] 오차 독립성(진단) + GLS(처방) — `[[Durbin-Watson 검정]]`·`[[Breusch-Godfrey 검정]]`·`[[일반화최소제곱(GLS)]]` 노트. 표백변환 $P'P=V^{-1}$ → GLS 공식 유도 |
| 2026-06-29 | [트랙 A] `[[Aitken 정리]]` 백지유도 착수(6/28 1순위) — BLUE=B·L·U·E 분해. **L**(β̂=Cy)·**U**(불편 → $CX=I_p$, $XC=I$ 차원/계수 오류 교정) 통과, 경쟁자 집합 $\mathcal C=\{Cy:CX=I_p\}$ 확정·β̂_GLS 소속 확인. **B(최소분산) 미완** → 다음: $\text{Var}(\tilde\beta)=\sigma^2 CVC'$, $C=C_{GLS}+D$ 분해. stub 2개(`[[행렬 곱의 계수 부등식]]`·`[[양의 준정부호 순서(Löwner order)]]`), 핸드오프 노트 작성 |
| 2026-06-29 | [트랙 A] `[[Aitken 정리]]` **B단계 완결 → 증명 종료** ✅. $C=C_{GLS}+D$ 분해 → 불편성 $DX=0$ → $C_{GLS}V=(X'V^{-1}X)^{-1}X'$ 로 교차항 소거 → $X'C_{GLS}'=(C_{GLS}X)'=I$ 로 첫 항=$\text{Var}(\hat\beta_{GLS})$ 확인 → $\text{Var}(\tilde\beta)=\text{Var}(\hat\beta_{GLS})+\sigma^2 DVD'\succeq\text{Var}(\hat\beta_{GLS})$, 유일성($D=0$)까지. (교정: $C=X^{-1}$ 오류 → $X$ 비정사각, $CX=I_p$ 는 왼쪽역행렬). status "완료" 갱신, MOC 등록, 핸드오프 `[[_세션핸드오프_2026-06-29_Aitken_B완결]]` |
| 2026-06-29 | [검증] **교재 대조** — 김충락 회귀분석 PDF로 Ch3 목차·색인 확인. **GLS·Aitken 교재 미수록** 발견(색인에 generalized least squares·Aitken 없음). 비-$\sigma^2I$ 처방은 §6.3 가중최소제곱법(WLS, p253-254, Ch6)뿐, Gauss-Markov는 Ch2 p55. `[[Aitken 정리]]`·`[[일반화최소제곱(GLS)]]` 의 chapter·book_pages·교재위치 박스를 사실대로 **정정**. |
| 2026-07-05 | [커리큘럼] **Cluster G 비모수 신설** — 교재 Kvam & Vidakovic(K&V) 편입. `[[01_Concept_Connection_Curriculum]]`에 연결사슬(EDF→KS→순위검정→부트스트랩→커널회귀)과 K&V 장별 매핑표 추가, 허브 `[[MOC_비모수]]` 골격 생성(가지 ①~④, 학습경로 7단계). 노드는 미생성(통과 0/7) |
| 2026-07-14 | [트랙 A·신규 과목] **범주형자료분석 Agresti Ch11 대응쌍** — `[[McNemar 검정]]`(주변동질성 ⟺ 대칭성, 스코어 통계량 $z_0=(n_{21}-n_{12})/\sqrt{n_{21}+n_{12}}$, 소표본=부호검정, CMH 동치)·`[[Cohen의 kappa (관측자 일치도)]]`(우연 보정 $\kappa=(P_o-P_e)/(1-P_e)$, Fleiss 분산, 가중 kappa, 준독립·준대칭) 두 노트 완료 |
| 2026-07-15 | [검증] **Montgomery 목차 대조** — "§14 = 반복측정"이 **오기**임을 확인. 반복측정 정본은 **§15.4(책 677–679)**, Ch14는 *Nested and Split-Plot*(혼합설계의 이론적 뼈대는 §14.4, 책 621–627). `[[Ch14_반복측정ANOVA_구형성_정리노트]]` 참고 페이지표를 사실대로 정정 |
| 2026-07-17 | [트랙 A] **§15.4 렌즈로 재정리** — 단일요인 반복측정(§15.4 Table 15.26)의 2단 분해 위에 gender를 얹으면 split-plot이 됨을 자유도로 검산(Between 39 = gender 1 + whole-plot error 38 / Within 80 = method 2 + 교호 2 + subplot error 76). `anova_test()` 분모 자유도로 `wid=ID` 누락 여부를 진단하는 법 정리 |
| 2026-07-19 | [트랙 A] `[[누락변수 편의와 유의성 반전]]` 신규 — ADP exam34 #4의 `index`(행 번호)가 다변량에서만 유의($p=0.0345$)한 현상을 **누락변수 대리(proxy)** 로 해석. $E[\hat\beta_1]=\beta_1+(X_1'X_1)^{-1}X_1'X_2\beta_2$, $C_p$ 편의항 $\mu'(I-H)\mu$, 반전 4패턴(억제·교란·매개·공선성), 전체 F 비유의 + 개별 t 유의의 보호검정 원칙. R 시뮬레이션 3종으로 재현. stub `[[Mallows Cp]]` 생성. **저작권 자료 저장소에서 제거**(커밋 0b9e5c7) |
| 2026-08-02 | [트랙 A] **Ch4 회귀진단 실전 적용** — `[[잔차의 직교성과 진단 그림의 가로축]]` 백지유도 완결($\hat y^\top e=0$ vs $y^\top e=e^\top e=SSE$ → 가로축 $y$ 면 기울기 $1-R^2$ 의 가짜 우상향). `[[Ch04_ADP32_Boston_회귀가정검토]]` 문제 1 완료 — Boston 506×14 완전모형의 4가정 **전부 위배**(RESET 97.853 / DW 1.0784 / BP 65.122 / SW 0.90138), `medv==50` 상한절단 16건 발견. 소수점 6자리 수치검증 |
| 2026-08-21 | [메타] **전체 무결성 검토 + 조치** → `[[2026-08-21_전체_무결성]]`. 유도 24건·수치 20여 항목 재검증 결과 **수학 오류 0건**(Boston 원자료 재적합, DW Imhof 정확 p=0.0101, BG·McNemar·κ·SS분해 전부 일치). 조치: 끊긴 위키링크 복구(별칭 5건 + 정규 stub 7건 신설 → 참조 해결률 60%), 빈 노트 2개 채움, 프론트매터 단일 규격 확정(`cluster` A~G 코드화 20건), 대시보드 6개 세션 복원, Montgomery §14→§15.4 전파, 스크립트 경로 상대화. **⚠️ 미조치(사용자 결정 필요): 공개 저장소 git 히스토리에 교재 PDF 잔존(F-01)** |
