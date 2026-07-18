---
type: MOC
title: 비모수 추론 (Nonparametric Inference)
aliases: [MOC_비모수, Nonparametric Inference MOC, Cluster G]
cluster: G
tags: [MOC, 비모수, 순위검정, EDF, 부트스트랩, 커널회귀, ClusterG, Hub]
date_created: 2026-07-05
date_modified: 2026-07-05
---

# 🗺️ MOC — [[비모수 추론]] (Nonparametric Inference) · Cluster G

> **Map of Content**: "분포 가정(정규성)을 내려놓아도 추정·검정이 성립하는가, 그 대가는 무엇인가"라는 한 뿌리에서 뻗어나간 가지를 모으는 허브.
> **주 교재**: Kvam & Vidakovic, *Nonparametric Statistics with Applications to Science and Engineering* (Wiley) — 이하 K&V. (PDF: 튜터워크스페이스, offset 11)

> [!note] 상태: 골격(skeleton)
> 2026-07-05 골격만 생성. 아래 가지의 `[[ ]]` 노드는 전부 **stub 예정** — 첫 개념 통과 시점부터 [[_MOC자동등록_규칙]]에 따라 채워 나간다.

## 왜 이 클러스터가 백본인가
모수적 세계(Cluster A–F)의 모든 결과는 "오차 분포를 안다"는 가정 위에 서 있다. 이 클러스터는 그 가정을 하나씩 내려놓으며 **같은 질문(추정·검정·회귀)이 어디까지 성립하는지**를 재조명한다.
- 순위(rank)와 경험분포함수(EDF)가 분포무관(distribution-free) 추론의 원재료.
- t-검정 ↔ Wilcoxon, ANOVA ↔ Kruskal-Wallis, CLT 근사 ↔ 부트스트랩, 전역 LSE ↔ 국소(커널) 회귀 — **기존 클러스터의 거울상**이므로 B·C·E·F와 맞물린다.

---

## 🌳 핵심 가지 (Branches)

### ① 원재료 — 순위와 경험분포함수 (뿌리)
- [[순서통계량과 표본분위수]] — 순위의 분포 이론. (Hogg §4.4 + K&V Ch5)
- [[경험분포함수(EDF)와 Glivenko-Cantelli]] — F̂_n → F 균등수렴: "데이터 자체가 분포의 추정량". (K&V §3.2, Ch10)

### ② 분포무관 검정 (줄기)
- [[콜모고로프-스미르노프(KS) 적합도 검정]] — sup|F̂_n − F₀|의 분포무관성. (K&V Ch6)
- [[순위 검정 — 부호·Wilcoxon·Mann-Whitney]] — t-검정의 분포무관 대응물, ARE = 3/π ≈ 0.955. (K&V Ch7)
- [[Kruskal-Wallis·Friedman 검정]] — 순위에 적용한 일원 ANOVA·RCBD. → Cluster B 교차. (K&V Ch8)

### ③ 재표본추출 (확장 가지)
- [[부트스트랩과 잭나이프]] — 점근 근사(CLT·Delta)를 재표본추출로 대체. → Cluster F 교차. (K&V Ch15)
- 연결 후보: 순열검정(permutation test), 베이지안 부트스트랩. (K&V §15.5–15.6)

### ④ 비모수 추정 — 분포·밀도·회귀 (잎)
- [[Kaplan-Meier 추정량]] — 중도절단 하의 생존함수 추정. → 김충락 Ch12 (중도절단 회귀). (K&V Ch10)
- [[커널 밀도추정과 비모수 회귀]] — 히스토그램 → 커널·대역폭 → 국소 가중 LSE. → Cluster E 교차 + 김충락 Ch11. (K&V Ch11–13)

---

## 🧭 권장 학습 경로 (뿌리 → 잎)
1. [[순서통계량과 표본분위수]] → 2. [[경험분포함수(EDF)와 Glivenko-Cantelli]] → 3. [[콜모고로프-스미르노프(KS) 적합도 검정]] → 4. [[순위 검정 — 부호·Wilcoxon·Mann-Whitney]] → 5. [[Kruskal-Wallis·Friedman 검정]] (Cluster B 이후 권장) → 6. [[부트스트랩과 잭나이프]] → 7. [[커널 밀도추정과 비모수 회귀]].

> 한 바퀴 돌면: "분포를 모른 채 무엇이 가능한가(①②) → 검정은 순위로 재현된다(②) → 표집분포는 재표본으로 근사한다(③) → 회귀·밀도까지 확장(④)"이 **하나의 논리**로 연결된다.

## 🔗 다른 클러스터와의 교차점
- **Cluster B (이차형식)**: Kruskal-Wallis가 순위 세계에서 ANOVA SS 분해를 재현 → `[[MOC_이차형식]]`.
- **Cluster E (투영·LSE)**: 커널 회귀 = LSE의 국소화(국소 가중 최소제곱).
- **Cluster F (점근이론)**: 부트스트랩이 CLT·Delta 근사의 대안; EDF 수렴이 KS 검정의 기반.
- **Cluster C (우도 추론)**: 순위 검정은 t-검정(정규모형 LRT)의 분포무관 대응물; 경험우도(K&V §10.8)가 우도 원리의 비모수 확장.

## 📚 교재 소재 (cross-textbook)
- **K&V**: Ch5 (순서통계량), Ch6 (적합도), Ch7 (순위 검정), Ch8 (실험설계), Ch10 (분포함수 추정·Kaplan-Meier), Ch11–13 (밀도·곡선적합), Ch15 (부트스트랩).
- 김충락 회귀분석 Ch11 (비모수회귀모형), Ch12 (중도절단자료의 회귀모형).
- Hogg 8판 §4.4 (순서통계량), §10 (비모수·로버스트 개관).

---

## 🔁 이어가기 — 2026-07-05 세션 (골격 생성)
1. **대상**: `[[MOC_비모수]]` 허브 신규 생성 · Cluster G 백본 (교재 K&V 편입에 따른 골격).
2. **오늘 한 것**: [[01_Concept_Connection_Curriculum]]에 Cluster G 신설(연결 사슬·K&V 장별 매핑 표)과 동시에 본 MOC 골격 생성. 가지 ①–④ 구조와 학습 경로 설계. 노드 생성은 하지 않음.
3. **핵심 상태**: 골격만 존재. 모든 `[[ ]]` 노드 미생성(stub 예정), 통과 개념 0 / 7.
4. **다음 출발점** →: 가지 ① [[순서통계량과 표본분위수]] (Hogg §4.4는 기수강 범위라 진입 장벽 낮음), 또는 Cluster B 완료 후 [[Kruskal-Wallis·Friedman 검정]]으로 교차 진입.
5. **연결**: `[[01_Concept_Connection_Curriculum]]` (Cluster G 섹션) · `[[_MOC자동등록_규칙]]`.
