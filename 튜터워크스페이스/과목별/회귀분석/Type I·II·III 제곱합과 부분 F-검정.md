---
subject: 회귀분석
chapter: Ch3 중선형회귀 (+ Ch5 일반선형가설)
concept: "[[Type I·II·III 제곱합과 부분 F-검정]]"
cluster: [B, E, A]
cross_ref:
  - "김충락 회귀분석 Ch3 중선형회귀모형 (book p.97–162) — 분산분석표·전체 F검정·회귀계수 t검정"
  - "김충락 회귀분석 Ch5 회귀모형의 선택 (book p.201–230) — 일반선형가설 H0:Aβ=c, 부분 F검정"
  - "Hogg 8판 §9.2 (ANOVA SS 분해), §9.8–9.9 (이차형식 분포·Cochran)"
  - "Fox & Weisberg, An R Companion to Applied Regression — car::Anova Type II/III"
tags: [ANOVA, TypeI_II_III, F검정, 부분F검정, 전체F검정, 이차형식, ClusterB, ClusterE, ClusterA, 회귀분석, ADP기출]
date_created: 2026-06-15
status: 초안 (튜터 작성 — 학습자 백지유도 후 교체)
source: ADP 기출 exam34 문제4 (lm(score ~ ., data=dat34_4))
aliases: ["Type I·II·III 제곱합과 부분 F-검정", Type I 제곱합, Type III 제곱합, 순차제곱합, 부분제곱합, 부분 F-검정, TypeI_II_III]
date_modified: 2026-08-21
---

# [[Type I·II·III 제곱합과 부분 F-검정]]

> **한 줄 요약**: Type I·II·III는 서로 다른 검정이 아니라, **같은 잔차제곱합을 어떤 부분공간으로 투영해 쪼개느냐**의 차이다. 세 타입 모두 `[[이차형식]]` $\mathbf{Y}^\top A\mathbf{Y}$이고, $A$가 멱등·대칭이라 `[[이차형식의 분포와 독립성 (Cochran 정리)]]`에 의해 $\chi^2$가 되어 `[[F-검정]]`이 성립한다.

---

## 0. 이번 문제 맥락 (ADP exam34 #4)

`lm(score ~ ., data = dat34_4)` — 설명변수 `studytime, failures, absences, index, paid, internet`. `absences`의 NA로 6개 관측치가 제외되어 $n=360$, 모수 $p=7$(절편 포함), 잔차 자유도 $353$.

`summary()` → 개별 회귀계수 유의성 + 맨 아래 전체 F검정.
`anova()` → **Type I** (순차 SS).
`car::Anova()` → 기본 **Type II** (부분 SS).

---

## 1. 통일된 관점: SS는 전부 투영의 길이² (Cluster B ∩ E)

설계행렬 $X$의 열공간으로의 투영행렬을 $P = X(X^\top X)^{-1}X^\top$ (= `[[Hat Matrix]]`, 대칭·멱등)이라 하자. 어떤 변수집합이 만드는 부분공간으로의 투영을 $P_{(\cdot)}$로 쓰면, "그 변수들이 추가로 설명한 변동(extra SS)"은 언제나

$$
SS = \mathbf{Y}^\top (P_{\text{큰모형}} - P_{\text{작은모형}})\,\mathbf{Y}.
$$

여기서 $A = P_{\text{큰}} - P_{\text{작}}$ 는 **두 중첩(nested) 투영의 차 → 다시 멱등·대칭**. 따라서 $SS/\sigma^2 \sim \chi^2_{\Delta\text{df}}$ (Cochran), 그리고 오차 SS와 독립이므로 비를 취하면 F가 된다. **세 타입의 차이는 오직 "$P_{\text{작은모형}}$을 무엇으로 잡느냐"** 뿐이다.

---

## 2. 세 타입의 정의

설명변수(항) 블록을 입력 순서대로 $X_1, X_2, \dots, X_m$이라 하고, $P_{1:k}$ = 처음 $k$개 블록이 만드는 부분공간으로의 투영.

### Type I — 순차 제곱합 (sequential)
$k$번째 항의 SS:
$$
SS^{\text{I}}_k = \mathbf{Y}^\top (P_{1:k} - P_{1:k-1})\,\mathbf{Y}.
$$
중첩 투영의 **직교 증분**이므로 $\sum_k SS^{\text{I}}_k = SSR$(모형 전체)로 **정확히 분해**되고, 증분들이 서로 독립이다(Cochran). **단점**: 순서 의존적. (앞에 들어온 변수가 공통 변동을 먼저 가져감.)

### Type III — 부분(주변) 제곱합, 완전보정
항 $j$의 SS = 완전모형에서 그 항만 뺀 효과:
$$
SS^{\text{III}}_j = \mathbf{Y}^\top (P_{\text{full}} - P_{(-j)})\,\mathbf{Y},
$$
$P_{(-j)}$ = 항 $j$의 열만 제거한 나머지 전체로의 투영. 즉 **다른 모든 항을 보정한** 그 항의 고유 기여. 상호작용이 있으면 contr.sum 등 직교대비가 없으면 무의미.

### Type II — 주변성(marginality) 존중
항 $j$를, **$j$를 포함하지 않는** 다른 모든 항으로만 보정. 상호작용을 가진 주효과는 그 상호작용을 빼고 검정.

> **핵심 정리**: 상호작용이 없는 **주효과만의 모형**(이번 문제가 정확히 그렇다)에서는 어떤 항을 빼도 "그를 포함하는 상위항"이 없으므로
> $$\boxed{\;\text{Type II} = \text{Type III} = summary()\text{의 회귀계수 검정}\;}$$

---

## 3. 부분 F-검정과 t-검정의 동치 (Cluster A 연결)

축소모형 vs 완전모형 비교의 **부분 F**(extra-sum-of-squares F):
$$
F = \frac{(SSE_{\text{reduced}} - SSE_{\text{full}})/q}{SSE_{\text{full}}/(n-p)} \sim F_{q,\,n-p}.
$$
이것이 `[[일반선형가설의 F 통계량 도출]]` $H_0: A\beta = c$의 특수형이다. 연속형 변수 하나를 빼는 경우 $q=1$이고, 그때

$$
F = t^2,\qquad t=\frac{\hat\beta_j}{\text{SE}(\hat\beta_j)}.
$$

즉 **Type II/III F값 = summary t값의 제곱**. (자유도 1인 F와 $t$의 잘 알려진 관계.)

### 3-1. 핵심 통합: Type I·II·III는 전부 "부분 F", 축소모형만 다르다 ★

세 타입은 별개의 검정이 아니라 **모두 같은 부분 F-검정**이다. **분모(완전모형의 MSE)는 셋 다 동일**하고, **분자의 축소모형(무엇을 빼고 비교하느냐)만 다르다.**

$$
F=\frac{(SSE_{\text{reduced}}-SSE_{\text{full}})/q}{SSE_{\text{full}}/(n-p)}\sim F_{q,\,n-p}
$$

| 타입 | 완전모형 | 축소모형 ($H_0$) | $q$ |
|---|---|---|---|
| **Type I** (항 $k$) | 1..$k$번째 항 | 1..$(k{-}1)$번째 항 | 그 항 df |
| **Type II** (항 $j$) | $j$ + ($j$ 미포함 항 전체) | $j$ 미포함 항 전체 | 그 항 df |
| **Type III** (항 $j$) | 전체 모형 | 전체 $-\,j$ | 그 항 df |

> **보정 대상이 다르다 = 축소모형이 다르다 = 다른 부분 F.** 검정의 *종류*는 모두 같다.

**같은 가족의 다른 멤버들:**
- **개별 계수 t검정** = $q=1$인 부분 F (완전 vs 그 변수 하나 뺀 모형) → $t^2=F$, 주효과-only면 곧 Type III(=II).
- **전체 F검정** = $q=k$인 부분 F (완전 vs 절편만).

**위계:** $\underbrace{t\text{검정}}_{q=1}\subset\underbrace{\text{Type I·II·III, 전체 F}}_{\text{부분 F}}\subset\underbrace{H_0:A\beta=c}_{\text{일반선형가설(Ch5)}}$

**exam34 수치 검증** (분모 = 완전모형 MSE = 30.282 공통):
- Type I `absences`: $140.085/30.282=4.626$ ✓
- Type II `absences`: $169.0/30.282=5.58$ ✓ — 같은 변수인데 F가 다른 건 **분자(축소모형)만 다르기 때문**.

**기하 (Cluster B 연결):** 분자는 언제나 두 투영의 차 $\mathbf{Y}^\top(P_{\text{full}}-P_{\text{reduced}})\mathbf{Y}$. $P_{\text{full}}-P_{\text{reduced}}$가 멱등·대칭 → `[[이차형식의 분포와 독립성 (Cochran 정리)]]`로 $\chi^2$. **Type I·II·III의 차이는 오직 $P_{\text{reduced}}$를 어느 부분공간으로 잡느냐**로 환원된다.

### 3-2. Type I의 순서 의존성 — 실증 (exam34)

Type I의 축소모형은 "그 변수 **앞에** 들어온 변수들"이다. 따라서 **입력 순서를 바꾸면 같은 변수의 축소모형이 바뀌어 SS·F가 달라진다.** 같은 데이터(분모 MSE = 30.282 공통)에서 `studytime` 하나만 추적해 보면:

| `studytime` 위치 | Type I SS | F | p |
|---|---|---|---|
| **맨 앞** (1번째 진입) | 41.751 | 1.379 | 0.241 |
| **맨 뒤** (마지막 진입) | 85.237 | 2.815 | ≈0.094 |

**같은 변수·같은 데이터인데 결론이 뒤집힌다** (비유의 → 경계 유의). 앞에 들어가면 다른 변수와의 공유 변동을 먼저 다 가져가고, 뒤에 들어가면 이미 다 보정된 뒤 *고유* 기여만 남기 때문이다.

> **음미할 포인트**: 변수를 **맨 마지막에** 넣은 Type I SS(85.237, F=2.815)는 그 변수의 **Type II/III SS와 정확히 같다**(=summary $t^2$=1.678²=2.816). 즉 "완전 보정"이란 곧 "순서상 맨 끝"과 동치 — Type III는 *모든 변수를 각각 맨 끝에 놓은* Type I이라고 볼 수 있다.

Type II/III가 순서 무관인 이유도 여기서 분명해진다: 항상 "나머지 전부를 먼저 넣은 뒤"를 가정하므로 진입 순서라는 자유도가 사라진다.

---

## 4. 전체 F-검정 (overall) — "모델의 유의성"

문제에서 "F검정으로 모형 유의성 평가"는 **summary 맨 아래 전체 F**를 뜻한다.
$$
H_0:\ \beta_1=\cdots=\beta_k=0 \quad\text{(절편 제외 모든 기울기=0)}.
$$
$$
F=\frac{SSR/k}{SSE/(n-k-1)}=\frac{R^2/k}{(1-R^2)/(n-k-1)} \sim F_{k,\,n-k-1}.
$$
기하학적으로 $H_0$는 "반응이 절편(상수)부분공간에 직교하는 성분을 안 가진다"는 뜻 → $SSR = \mathbf{Y}^\top(P - P_{\mathbf 1})\mathbf{Y}$ 역시 이차형식.

---

## 5. 이번 출력에서의 수치 검증 ✔

**전체 F** ($k=6,\ R^2=0.03466,\ n-k-1=353$):
$$
F=\frac{0.03466/6}{(1-0.03466)/353}=2.112,\quad p=0.05127.
$$
출력값과 일치. → $\alpha=0.05$에서 **$p=0.051>0.05$, $H_0$ 기각 실패 = 모형 전체는 (경계선에서) 유의하지 않음**. $R^2=0.035$로 설명력도 매우 낮다.

**Type II F = $t^2$** 동치 확인:

| 변수 | summary $t$ | $t^2$ | Anova(II) F |
|---|---|---|---|
| studytime | 1.678 | 2.816 | 2.8147 |
| absences | 2.362 | 5.579 | 5.5799 |
| index | −2.122 | 4.503 | 4.5027 |
| paid | 1.421 | 2.019 | 2.0180 |
| internet | −0.329 | 0.108 | 0.1084 |

**Type I ≠ Type II** (순서 의존 확인): 예) `studytime` Type I F=1.3787(단독)인데 Type II는 2.8147(나머지 전부 보정). `absences`도 4.626 → 5.5799로 달라짐.

유의한 변수: `absences`(+, 결석↑ 점수와 양의 관계?) 와 `index`(−). 부호 해석은 변수 정의 확인 필요.

---

## 6. 막혔던 포인트 & 주의 (튜터 힌트)

- **왜 차의 투영 $P_{\text{큰}}-P_{\text{작}}$이 다시 멱등인가?** 중첩이면 $P_{\text{큰}}P_{\text{작}}=P_{\text{작}}$ 성질을 쓰면 바로 나온다. → `[[Hat Matrix의 멱등성 및 대칭성]]`.
- **Type III는 대비코딩에 민감.** 요인 변수 + 상호작용 모형에서 default `contr.treatment`로 Type III를 읽으면 해석 불가. `contr.sum` 필요.
- **anova(model1, model2)** (두 모형 비교)는 부분 F검정 그 자체 = Type II/III의 일반화.

---

## 7. 연결 개념 (클러스터 참조)

- **Cluster B (이차형식)**: `[[ANOVA SS 분해]]` · `[[F-검정]]` · `[[이차형식의 분포와 독립성 (Cochran 정리)]]` — 이 노트의 모태 허브 `[[MOC_이차형식]]` 가지 ③.
- **Cluster E (투영·LSE)**: `[[Hat Matrix]]` 의 중첩 투영 차로 모든 SS가 표현됨.
- **Cluster A (추정효율성·일반선형가설)**: `[[일반선형가설의 F 통계량 도출]]` · `[[부분 F-검정과 전체 F-검정의 관계]]` (Ch5).

## 8. 참고 교재 페이지

- 김충락 회귀분석 **Ch3 중선형회귀** (book p.97–162 / PDF p.113–178) — 메인.
- 김충락 회귀분석 **Ch5 회귀모형의 선택** (book p.201–230 / PDF p.217–246) — 일반선형가설.
- Hogg 8판 §9.2 (SS 분해), §9.8–9.9 (Cochran).
- Fox & Weisberg, *An R Companion to Applied Regression* — `car::Anova` Type II/III.

---

## 🔁 이어가기 (세션 로그 — 최신이 위로)

## 🔁 이어가기 — 2026-06-18 세션
1. **대상**: `[[Type I·II·III 제곱합과 부분 F-검정]]` · 신규 자매노트 `[[Type II 제곱합 (정식화)]]` `[[Montgomery 불균형·공변량 ANOVA와 Type I·II·III]]` · 회귀 3·5장 / 실험설계 15장 · 트랙 A(유도)
2. **오늘 한 것**: 손계산 예제 설계(요인 A 3수준 + 연속형 $X_1,X_2$ + 교차항 $A{:}X_1$, $n=10$, $df_E=3$); Type I·II·III 표의 *형태*(어떤 모형끼리 빼는가)를 모형비교로 정식화; 교차항 유의 시 단순주효과 분해; 직교성 의미 정리.
3. **핵심 결과·미완 상태** ⭐: $SSE(1)=SST=38.40$. Type I 순서의존 수치예 — $R(A)=3.067$ vs $R(A\mid X1)=1.345$ (합은 37.655로 보존). Type II = 포함관계 격자로 정식화(`$SS_{II}(U)=\mathbf y'(P_{W(U)\cup U}-P_{W(U)})\mathbf y$`). 단순주효과 항등식 $\sum_j SS_{A\mid b_j}=SS_A+SS_{AB}$ 손증명+수치검증 완료. **미완**: 7-모수 모형의 8개 축소모형 SSE 숫자값은 R로 미산출(코드 보류).
4. **막힌 지점**: 없음 (개념 이해 도달).
5. **검증**: 손풀이 ✔ (crossover $2\times2$로 항등식 25=0+25 확인) · 코드 ✗ (다음 세션)
6. **다음 출발점** →: R로 8개 축소모형 SSE를 뽑아 Type I/II/III 분산분석표 **숫자**를 채운다 (`anova`=Type I, `car::Anova(type=2/3)`, 요인은 `contr.sum`으로 Type III 일치 확인).
7. **열린 질문**: Q1 효과코딩 $L$ vs 가변수코딩 $L$의 $A(X'X)^{-1}A'$ 차이? / Q2 직교조건 $n_{ij}-n_{i.}n_{.j}/n_{..}$ 의 연속형 일반화? / Q3 평균중심화 Type III = LS-means 동일성 검정?
8. **연결**: `[[Type II 제곱합 (정식화)]]` `[[Montgomery 불균형·공변량 ANOVA와 Type I·II·III]]` · `[[MOC_이차형식]]`
