---
aliases: [진도 대시보드, Progress Dashboard]
tags: [통계학, Dashboard, Hub]
date_modified: 2026-06-11
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
> | **E. 투영·LSE** | `[[LIE]]` ↔ `[[Hat Matrix]]` ↔ `[[PCA]]` |
> | **F. 점근이론** | `[[CLT·Delta]]` ↔ `[[MLE 점근]]` ↔ `[[단위근 검정]]` |

---

## 🧭 현재 집중 학습 위치 (Current Focus)
* **과목**: 회귀분석 Cluster A 추정효율성 (GLS·Aitken은 교재 외 고전결과 — 교재 관련: §6.3 WLS, Ch6)
* **챕터/개념**: `[[Aitken 정리]]` — GLS가 BLUE 증명 ✅ **완결** (2026-06-29, L·U·B 전부 통과 + 유일성)
* **진행 중인 작업**: 트랙 A 백지유도. **다음 출발점(확정)**: `[[이차형식]]` — 교재 **§3.4 이차형식과 제곱합의 분포(p114–119, Ch3)**. ANOVA·F-검정의 엔진 → `[[이차형식과 Cochran 정리]]`. Cluster B `[[MOC_이차형식]]`. (보류: WLS §6.3) 핸드오프 `[[_세션핸드오프_2026-06-29_Aitken_B완결]]`

---

## 📚 교재 목록 (Textbooks)

| 과목 | 교재 | 비고 |
|------|------|------|
| 수리통계학 | Hogg, McKean & Craig, *Introduction to Mathematical Statistics*, 8th ed. (Pearson, 2019) | Ch1~Ch10 |
| 회귀분석 | 김충락, *회귀분석* (Note I & II) | Ch1~Ch12 + 부록 A·B |
| 실험설계법 | Montgomery, *Design and Analysis of Experiments*, 8th ed. (Wiley, 2012) | Ch1~Ch15 |
| 다변량분석 | Johnson & Wichern, *Applied Multivariate Statistical Analysis*, 6th ed. (Pearson) | Ch1~Ch12 ⭐추천 |
| 시계열분석 | Levendis, *Time Series Econometrics: Learning Through Replication* | BU EC-490 강의노트 Ch1~Ch12 |
| 비모수통계 | Hogg 8판 Ch10 (비모수 섹션 활용) | — |
| 베이즈통계 | (교재 미업로드 — 추후 추가) | — |

---

## 📁 업로드된 자료 현황

```
튜터워크스페이스/
├── introduction_to_mathematical_statistics_8.pdf        ← Hogg 8판
├── Design_and_Analysis_of_Experiments_Wiley_2012.pdf   ← Montgomery 8판
├── regression_김충락/
│   ├── Regression Analysis_note (I).pdf
│   ├── Regression Analysis_note (II).pdf
│   ├── 회귀분석_chapters/  (ch01~ch12 챕터별 분할)
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

### 📘 회귀분석 — 김충락 교수 Note

#### Ch1~2. 단순선형회귀
- [ ] `[[정규방정식과 LSE 유도]]`
- [ ] `[[불편성(Unbiasedness) 증명]]`
- [ ] `[[회귀계수의 분산 유도]]`
- [ ] `[[신뢰구간 및 예측구간의 분산 차이]]`

#### Ch3~4. 중선형회귀 · 회귀진단
- [ ] `[[Gauss-Markov 정리]]`
- [ ] `[[Hat Matrix의 멱등성 및 대칭성]]`
- [ ] `[[이차형식과 Cochran 정리 — 회귀분석 맥락]]`

#### Ch5~7. 변수선택 · 편의추정
- [ ] `[[AIC, BIC 유도와 변수선택 기준]]`
- [ ] `[[Ridge 회귀와 편향-분산 트레이드오프]]`
- [ ] `[[다중공선성 진단 (VIF, 조건수)]]`

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

#### Ch13~14. 랜덤효과 · 혼합모형
- [ ] `[[랜덤효과 모형과 분산성분 추정 (REML)]]` §13
- [x] `[[반복측정 설계와 구형성 가정 (Mauchly 검정)]]` §14 ✅ 2026-06-09 (SS 분해·잔차 유도 완료)

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
| 2026-06-12 | [Hub] 세션 시작 — 오늘 목표: `[[이차형식과 Cochran 정리]]` 자유도 분해 (트랙 A). 튜터워크스페이스로 라우팅. Cluster B (`[[Cochran 정리]]` ↔ `[[Hat Matrix]]` ↔ `[[ANOVA SS 분해]]`) 연결 심화 |
| 2026-06-28 | [트랙 A] 오차 독립성(진단) + GLS(처방) — `[[Durbin-Watson 검정]]`·`[[Breusch-Godfrey 검정]]`·`[[일반화최소제곱(GLS)]]` 노트. 표백변환 $P'P=V^{-1}$ → GLS 공식 유도 |
| 2026-06-29 | [트랙 A] `[[Aitken 정리]]` 백지유도 착수(6/28 1순위) — BLUE=B·L·U·E 분해. **L**(β̂=Cy)·**U**(불편 → $CX=I_p$, $XC=I$ 차원/계수 오류 교정) 통과, 경쟁자 집합 $\mathcal C=\{Cy:CX=I_p\}$ 확정·β̂_GLS 소속 확인. **B(최소분산) 미완** → 다음: $\text{Var}(\tilde\beta)=\sigma^2 CVC'$, $C=C_{GLS}+D$ 분해. stub 2개(`[[행렬 곱의 계수 부등식]]`·`[[양의 준정부호 순서(Löwner order)]]`), 핸드오프 노트 작성 |
| 2026-06-29 | [트랙 A] `[[Aitken 정리]]` **B단계 완결 → 증명 종료** ✅. $C=C_{GLS}+D$ 분해 → 불편성 $DX=0$ → $C_{GLS}V=(X'V^{-1}X)^{-1}X'$ 로 교차항 소거 → $X'C_{GLS}'=(C_{GLS}X)'=I$ 로 첫 항=$\text{Var}(\hat\beta_{GLS})$ 확인 → $\text{Var}(\tilde\beta)=\text{Var}(\hat\beta_{GLS})+\sigma^2 DVD'\succeq\text{Var}(\hat\beta_{GLS})$, 유일성($D=0$)까지. (교정: $C=X^{-1}$ 오류 → $X$ 비정사각, $CX=I_p$ 는 왼쪽역행렬). status "완료" 갱신, MOC 등록, 핸드오프 `[[_세션핸드오프_2026-06-29_Aitken_B완결]]` |
| 2026-06-29 | [검증] **교재 대조** — 김충락 회귀분석 PDF로 Ch3 목차·색인 확인. **GLS·Aitken 교재 미수록** 발견(색인에 generalized least squares·Aitken 없음). 비-$\sigma^2I$ 처방은 §6.3 가중최소제곱법(WLS, p253-254, Ch6)뿐, Gauss-Markov는 Ch2 p55. `[[Aitken 정리]]`·`[[일반화최소제곱(GLS)]]` 의 chapter·book_pages·교재위치 박스를 사실대로 **정정**. |
| 2026-06-11 | [트랙 A] Ch14 정리노트에 **가정 위배 대응(등분산성·정규성) 심화** 섹션 보강 + `exam34_problem3` R 디버깅(`shapiro.test`→`shapiro_test`, rstatix 로드). **학습 인프라 신설**: `[[이어가기_handoff_템플릿]]`(세션 연속성)·`[[MOC_이차형식]]`(Cluster B 허브). 커리큘럼↔MOC 4단 위계 정리. ⚠️ **다음 출발점**: 세 파일 위키링크 *이름 불일치* 정규화(정규명+alias) — 미착수 |
