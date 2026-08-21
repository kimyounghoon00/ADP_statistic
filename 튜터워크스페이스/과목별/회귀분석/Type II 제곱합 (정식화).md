---
aliases: [Type II SS, Type 2 제곱합, 부분제곱합 II, partial SS II]
tags: [회귀분석, 분산분석, TypeII, 제곱합, 주변성원리]
cluster: [B, E]
subject: 회귀분석
chapter: "Ch3 중선형회귀 (추가제곱합) + Ch5 일반선형가설 / Montgomery §15.2"
concept: "[[Type II 제곱합 (정식화)]]"
cross_ref: ["Searle, Linear Models (추가제곱합·추정가능함수)","Nelder (1977) marginality","SAS PROC GLM / car::Anova (containment)"]
date_created: 2026-06-18
moc: ["[[MOC_이차형식]]"]
date_modified: 2026-08-21
---
 
# Type II 제곱합 — 엄밀한 정식화

> 직관: "자기를 포함하는 상위항만 빼고 나머지 전부에 조정한다."
> 이 노트는 그 직관을 **사영행렬과 포함관계 격자(lattice)** 로 형식화한다.

---

## 1. 행렬·사영 표현 (공통 기반)

모형 $\mathbf{y}=X\boldsymbol\beta+\boldsymbol\varepsilon,\ \boldsymbol\varepsilon\sim N(\mathbf 0,\sigma^2 I)$.

항들의 집합 $S$(절편 포함)에 대응하는 설계열들이 만드는 열공간으로의 **직교사영행렬**을

$$P_S = X_S(X_S'X_S)^{-}X_S', \qquad SSE(S)=\mathbf y'(I-P_S)\mathbf y$$

로 둔다. 한 항 $U$를 집합 $S$ 위에 추가했을 때의 `[[추가제곱합(extra sum of squares)]]`은

$$R(U\mid S)=SSE(S)-SSE(S\cup U)=\mathbf y'\,(P_{S\cup U}-P_S)\,\mathbf y .$$

여기서 $P_{S\cup U}-P_S$ 는 **$\mathrm{col}(S)$에 직교하는 $U$의 성분**으로의 사영이며, 대칭·멱등이고

$$\operatorname{rank}(P_{S\cup U}-P_S)=\operatorname{rank}(S\cup U)-\operatorname{rank}(S)=df_U .$$

> **"$S$에 조정한다"** = $S$가 만든 공간을 먼저 제거한 뒤 남은 직교성분에서 $U$의 기여를 측정한다는 사영의 언어.

---

## 2. 포함관계(containment)의 형식적 정의

항 $U$가 항 $V$에 **포함된다**($U \prec V$)는 것은 다음을 만족함을 말한다.

1. $U$와 $V$가 동일한 연속형 공변량을 같은 차수로 포함하고,
2. $U$의 인자(factor) 집합이 $V$의 인자 집합의 **진부분집합**이다.

이 관계는 항들의 집합에 **반순서(partial order)** 를 부여한다 (포함관계 격자).

예제 모형 $\{A,\ X_1,\ X_2,\ A{:}X_1\}$ 에서:

$$A \prec A{:}X_1,\qquad X_1 \prec A{:}X_1,\qquad X_2 \not\prec (\text{어떤 항도}),\qquad A{:}X_1=\text{최대원소}.$$

---

## 3. Type II 제곱합의 정의 (사영 형태)

항 $U$에 대해 **$U$를 포함하지 않는 모든 항**(절편 포함)의 집합을

$$W(U)=\{\,V\ne U:\ U \not\prec V\,\}$$

로 정의한다. 그러면

$$\boxed{\,SS_{\mathrm{II}}(U)=\mathbf y'\,\big(P_{W(U)\cup U}-P_{W(U)}\big)\,\mathbf y = SSE\big(W(U)\big)-SSE\big(W(U)\cup U\big)\,}$$

자유도는 $df_U=\operatorname{rank}(W(U)\cup U)-\operatorname{rank}(W(U))$.

**예제 적용:**

| 항 $U$ | $U$를 포함하는 항(제외) | $W(U)$ | $SS_{\mathrm{II}}(U)$ |
|---|---|---|---|
| $A$ | $A{:}X_1$ | $\{1,X_1,X_2\}$ | $SSE(X_1,X_2)-SSE(A,X_1,X_2)$ |
| $X_1$ | $A{:}X_1$ | $\{1,A,X_2\}$ | $SSE(A,X_2)-SSE(A,X_1,X_2)$ |
| $X_2$ | (없음) | $\{1,A,X_1,A{:}X_1\}$ | $SSE(A,X_1,A{:}X_1)-SSE(\text{full})$ |
| $A{:}X_1$ | (없음) | $\{1,A,X_1,X_2\}$ | $SSE(A,X_1,X_2)-SSE(\text{full})$ |

---

## 4. 핵심 특성 (정리와 증명 개요)

### 정리 1 (순서 무관성)
$SS_{\mathrm{II}}(U)$ 는 항을 나열한 **순서에 의존하지 않는다.**

*증명.* $W(U)$ 는 오직 포함관계 반순서로만 정의되며 어떤 나열 순서도 참조하지 않는다. 반면 `[[Type I 제곱합]]`의 조정집합은 $k$번째 항에 대해 $\{1,\dots,k-1\}$ 로 **순서에 의존**한다. ∎

### 정리 2 (주변성 특성화)
$W(U)\cup U$ 는 "$U$ 위에 있는 항을 모두 뺀 최대 부분모형"이며, 그 안에서 $U$는 **최대원소(maximal)** 이다. 즉 **Type II는 $U$가 최고차항이 되는 가장 큰 부분모형 안에서 $U$를 검정**한다. 이것이 `[[주변성 원리(marginality)]]`의 형식적 의미다.

### 정리 3 ($X_2$형 항: Type II = Type III)
어떤 교차항에도 포함되지 않는 항 $U$($X_2$ 등)에 대해 $SS_{\mathrm{II}}(U)=SS_{\mathrm{III}}(U)$.

*증명.* Type III의 조정집합은 항상 "$U$를 제외한 다른 모든 항"이다. $U$를 포함하는 항이 하나도 없으면 $W(U)=$ "$U$ 제외 전부" 가 되어 Type III의 조정집합과 **집합으로서 일치**한다. 동일 사영 → 동일 이차형식. ∎

### 정리 4 (교차항 없는 모형: 모든 항 II = III)
모형에 교차항이 전혀 없으면, 어떤 두 항도 포함관계가 없으므로 모든 $U$에서 $W(U)=$ "$U$ 제외 전부". 따라서 모든 항에서 Type II = Type III. (이때가 가장 검정력 높은 부분검정.)

---

## 5. 검정가설과 $F$-분포

$SS_{\mathrm{II}}(U)$ 는 부분모형 $W(U)\cup U$ 안에서 $H_0:$ "$U$의 모수 $=\mathbf 0$" 에 대한 **가능도비(=추가제곱합) 검정통계량**이다. 동치로 어떤 추정가능함수 $L'\boldsymbol\beta=\mathbf 0$ 의 검정이다.

분모 $SSE(\text{full})=\mathbf y'(I-H)\mathbf y,\ H=P_{\text{full}}$ 와의 **독립성**: $\mathrm{col}(W(U)\cup U)\subseteq\mathrm{col}(\text{full})$ 이므로

$$\big(P_{W(U)\cup U}-P_{W(U)}\big)(I-H)=0 .$$

따라서 `[[Cochran 정리]]` / `[[이차형식의 독립성]]` 에 의해 $H_0$ 하에서

$$F=\frac{SS_{\mathrm{II}}(U)/df_U}{SSE(\text{full})/df_E}\ \sim\ F_{\,df_U,\ df_E}.$$

(예제: $df_E=n-7=3$.)

---

## 6. 세 타입 한눈 비교 — 항 $A$ 기준

| 타입 | $A$의 조정집합 | 조정행렬 형태 | 성질 |
|---|---|---|---|
| Type I (A 먼저) | $\varnothing$ | $P_{1,A}-P_1$ | 순서 의존, $\sum SS=SSR$ |
| Type II | $\{X_1,X_2\}$ | $P_{1,A,X_1,X_2}-P_{1,X_1,X_2}$ | 순서 무관, **상위교차항 무시** |
| Type III | $\{X_1,X_2,A{:}X_1\}$ | $P_{\text{full}}-P_{\text{full}\setminus A}$ | 상위교차항까지 조정, **코딩 의존(효과코딩 필요)** |

**해석 지침:** $A{:}X_1$ 이 유의하지 않으면 Type II가 합리적·고검정력. 유의하면 주효과 $A$의 II/III 단독해석은 피하고 교차항 구조를 본다.

---

## 7. 참고 (출처)
- Searle, *Linear Models*, 추가제곱합·추정가능함수 장
- Nelder (1977), McCullagh & Nelder, *marginality* 원리
- SAS/`car::Anova` 의 Type II/III 정의 (containment 기준)
