---
subject: 비모수통계
chapter: "Kvam & Vidakovic, Nonparametric Statistics... Ch8 Designed Experiments — §8.1 Kruskal-Wallis Test, §8.2 Friedman Test"
concept: "[[Kruskal-Wallis·Friedman 검정]]"
aliases: [Kruskal-Wallis test, KW test, Kruskal-Wallis 검정, 크루스칼-왈리스 검정, Friedman test, Friedman 검정, 프리드먼 검정, 순위 ANOVA]
cross_ref:
  - "Kvam, P.H. & Vidakovic, B. (2007), *Nonparametric Statistics with Applications to Science and Engineering*, Wiley, §8.1–8.2 — 책 p.141–149 (PDF p.152–160, offset 11)"
  - "Kruskal, W.H. & Wallis, W.A. (1952), '\''Use of Ranks in One-Criterion Variance Analysis,'\'' JASA 47, 583–621"
  - "Friedman, M. (1937), '\''The Use of Ranks to Avoid the Assumption of Normality Implicit in the Analysis of Variance,'\'' JASA 32, 675–701"
tags: [비모수통계, KruskalWallis, Friedman, 순위검정, ANOVA, RCBD, ClusterG]
date_created: 2026-08-20
status: 완료
---

# [[Kruskal-Wallis·Friedman 검정]] — 순위로 재현하는 일원·이원 ANOVA

> **목표**: 정규성 가정을 내려놓고, "$k$개 집단(또는 처리)의 위치가 같은가"라는 one-way ANOVA(→ Kruskal-Wallis)와
> randomized block design·RCBD(→ Friedman)의 질문을, **원자료 대신 순위**로 재현되는 $\chi^2$ 검정으로 답한다.

## 핵심 아이디어 — 한 줄 사슬

$$
\text{원자료}\ \xrightarrow{\text{전체(또는 블록 내) 순위화}}\ \text{순위}
\;\to\; \text{순위에 one-way(또는 RCBD) ANOVA SS 분해 적용}
\;\to\; H=(N-1)R^2_{\text{rank}}\ \big(\text{또는 } S\big)\ \sim\ \chi^2_{k-1}
$$

**Kruskal-Wallis = 순위 위에서 재현한 [[일원 ANOVA 제곱합 분해 — Hogg §9.2]]**, **Friedman = 순위 위에서 재현한 RCBD 이원 ANOVA**. 순위로 바꾸는 순간 분포 가정이 사라지고, ANOVA의 SS 분해 논리만 남는다.

## 설정 — 왜 F-검정을 못 쓰는가

$k$개 독립표본 $X_{i1},\dots,X_{i,n_i}$ ($i=1,\dots,k$), $N=\sum n_i$. one-way ANOVA는 각 모집단이 **독립·정규·등분산**이라는 가정 위에 서 있다. Kruskal-Wallis는
$$
H_0: F_1=\cdots=F_k \quad\text{(모든 분포함수가 동일)}
$$
을, 정규성 없이 **위치(중앙값) 이동 대립가설**에 대해 검정한다.

## 유도 과정 — Kruskal-Wallis

### 1. 전체 순위화와 순위합
$N$개 관측치를 전부 합쳐 $1,\dots,N$으로 순위 매김(동점은 평균순위). $R_i=\sum_j r(X_{ij})$ = 집단 $i$의 순위합. $H_0$ 하에서
$$
E(R_i)=\frac{n_i(N+1)}{2},\qquad \operatorname{Var}(R_i)=\frac{n_i(N+1)(N-n_i)}{12}
$$

### 2. 검정통계량
$$
H=\frac{12}{N(N+1)}\sum_{i=1}^k \frac{R_i^2}{n_i}-3(N+1)\ \xrightarrow{d}\ \chi^2_{k-1}
$$
자유도가 $k-1$인 이유: 순위합의 총합 $\sum R_i=N(N+1)/2$가 **고정된 선형 제약**이라 $k$개 $R_i$ 중 자유로운 것은 $k-1$개뿐 — one-way ANOVA의 처리 자유도와 정확히 같은 논리.

**동점 보정**: 동점 그룹 $j$의 크기를 $t_j$라 하면
$$
H_c=\frac{H}{1-\dfrac{\sum_j (t_j^3-t_j)}{N^3-N}}
$$

### 3. 왜 이게 "순위 위의 ANOVA $R^2$"인가 — 엄밀한 항등식
순위 전체의 총제곱합(그랜드평균 $(N+1)/2$ 기준)은 동점이 없으면 **데이터와 무관한 상수**:
$$
SST_{\text{rank}}=\sum(\text{rank}-\tfrac{N+1}2)^2=\frac{N(N^2-1)}{12}
$$
집단간 제곱합은
$$
SSB_{\text{rank}}=\sum_i n_i\Big(\bar R_i-\tfrac{N+1}2\Big)^2=\sum_i\frac{R_i^2}{n_i}-\frac{N(N+1)^2}{4}
$$
대입하면 $H=\dfrac{12}{N(N+1)}SSB_{\text{rank}}$, 그리고
$$
\boxed{\,H=(N-1)\,R^2_{\text{rank}}\,},\qquad R^2_{\text{rank}}=\frac{SSB_{\text{rank}}}{SST_{\text{rank}}}
$$
**Kruskal-Wallis $H$는 순위를 반응변수로 쓴 one-way ANOVA의 결정계수 $R^2$에 $(N-1)$을 곱한 것과 정확히 같다.** → [[MOC_이차형식]] Cluster B가 말하는 "순위 세계에서 ANOVA SS 분해가 재현된다"는 문장의 대수적 실체.

### 4. $k=2$ 특수 케이스
$k=2$이면 $H$는 [[순위 검정 — 부호·Wilcoxon·Mann-Whitney]]의 정규근사 $Z$의 제곱 $H=Z^2$과 일치 ($\chi^2_1=Z^2$). Kruskal-Wallis는 Wilcoxon-Mann-Whitney의 $k$-표본 확장.

### 5. 다중비교 (Conover–Iman)
전체 검정이 기각되면, $s^2=N(N+1)/12$ (동점 없을 때)라 하고
$$
\Big|\bar R_i-\bar R_j\Big| > t_{1-\alpha/2,\,N-k}\ \sqrt{\ s^2\,\frac{N-1-H}{N-k}\left(\frac1{n_i}+\frac1{n_j}\right)}
$$
이면 집단 $i,j$가 다르다고 판정. **이것은 순위-ANOVA의 잔차분산 $\dfrac{SST_{\text{rank}}-SSB_{\text{rank}}}{N-k}$를 쓰는 Fisher LSD**와 동일한 구조 — $H$가 곧 $R^2\times(N-1)$이므로 $(N-1-H)$가 잔차 제곱합의 몫을 담당한다.

## 유도 과정 — Friedman

### 1. 설정과 블록 내 순위화
$b$개 블록(개체) $\times$ $k$개 처리, RCBD. $X_{ij}$ = 블록 $i$·처리 $j$의 관측치. **각 행(블록) 안에서만** $1,\dots,k$로 순위 매김. 처리 $j$의 순위합 $R_j=\sum_i r(X_{ij})$.

**핵심 구조적 사실**: 동점이 있어도 한 행의 순위 합은 항상 $1+\cdots+k=k(k+1)/2$로 고정 → **모든 블록의 행평균이 항등적으로 $(k+1)/2$** → 블록간 제곱합 $SS_{\text{blocks,rank}}\equiv 0$. 블록 효과가 "없어서"가 아니라, **행 내부 재순위화가 블록 위치를 구조적으로 지워버리기 때문**이다. RCBD의 블록 통제 논리를 순위가 자동으로 수행한다.

### 2. 검정통계량
$$
S=\frac{12}{bk(k+1)}\sum_{j=1}^k R_j^2-3b(k+1)\ \xrightarrow{d}\ \chi^2_{k-1}
$$
**동점 보정**: $C=\dfrac{bk(k+1)^2}{4}$, $R^{*}=\sum_i\sum_j r(X_{ij})^2$ 라 하면
$$
S'=\frac{(k-1)\big(\sum_j R_j^2-bC\big)}{R^{*}-C}\ \sim\ \chi^2_{k-1}
$$
(동점 없으면 $R^*-C=bk(k^2-1)/12$로 상수가 되어 $S'=S$.)

### 3. Iman–Davenport $F$ 변환
$\chi^2$ 근사보다 표본크기가 작을 때 더 정확한
$$
F=\frac{(b-1)S}{b(k-1)-S}\ \sim\ F_{k-1,\,(b-1)(k-1)}
$$
이 쓰인다. 분모 자유도 $(b-1)(k-1)$은 총자유도 $(bk-1)$에서 처리($k-1$)와 블록($b-1$)을 뺀 값 — 블록 SS가 항등적으로 0이어도 **자유도는 여전히 소모된다**는 점이 함정(아래 참고).

### 4. 다중비교 (Conover–Iman)
$$
\big|R_i-R_j\big| > t_{1-\alpha/2,\,(b-1)(k-1)}\ \sqrt{\ \frac{2\big(bR^{*}-\sum_j R_j^2\big)}{(b-1)(k-1)}\ }
$$
이 식은 순위표(블록$\times$처리)에 이원 ANOVA를 적용했을 때의 **잔차제곱합** $\dfrac{bR^*-\sum R_j^2}{b}$에서 나온 Fisher LSD와 정확히 같다(아래 예제에서 직접 검증).

## 예제 1 — 작물 수확량 4처리 (K&V Example 8.1–8.2, 책 p.143–144)

4개 처리, $n=34$($n_i=10,9,8,7$). $H=20.3371$, $\text{df}=3$, $p=1.45\times10^{-4}$ → $H_0$ 기각.

다중비교($t_{30,0.975}=2.042$, 검정통계량 $\bigl|\bar R_i-\bar R_j\bigr|/\sqrt{\cdots}$):

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | — | 1.856 | 1.859 | **5.169** |
| **2** | 1.856 | — | **3.570** | **3.363** |
| **3** | 1.859 | **3.570** | — | **6.626** |
| **4** | **5.169** | **3.363** | **6.626** | — |

(굵게 표시 = $>2.042$, 유의) → 처리 3이 최상이지만 처리 1과는 유의하게 다르지 않고(1.859), 처리 2(3위)는 1과는 다르지 않지만 3·4와는 유의하게 다르다.

## 예제 2 — 자동차 3종 평가, 운전자 6명 (K&V Example 8.3–8.4, 책 p.146–147) — 자체 검증 완료

| 운전자 | A | B | C |
|---|---|---|---|
| I | 7 | 8 | 9 |
| II | 6 | 10 | 7 |
| III | 6 | 8 | 8 |
| IV | 7 | 9 | 8 |
| V | 7 | 10 | 9 |
| VI | 8 | 8 | 9 |

행별 순위(동점 평균순위) 후 열합: $R_A=6.5,\ R_B=15,\ R_C=14.5$ ($b=6,\ k=3$).

동점 보정: $C=72,\ R^{*}=83$ → $S'=\dfrac{2(477.5-6\cdot72)}{11}=8.2727\ (\chi^2_2,\ p=0.0160)$,
$F=\dfrac{5\times8.2727}{6\times2-8.2727}=11.098\ (F_{2,10},\ p=0.0029)$ — **K&V 원문 값과 정확히 일치**.

다중비교($\alpha=0.01$, $t_{10,0.995}=3.169$, 임계값 $=t\sqrt{2(bR^*-\sum R_j^2)/((b-1)(k-1))}=6.42$):
$|R_A-R_B|=8.5>6.42$ (유의), $|R_A-R_C|=8.0>6.42$ (유의), $|R_B-R_C|=0.5<6.42$ (비유의).
→ **차 A가 B, C보다 유의하게 낮게 평가, B와 C는 차이 없음** — K&V 결론과 정확히 일치. (직접 계산으로 위 공식을 검증.)

## 막혔던 포인트 & 함정

- **자유도 $k-1$의 의미**: $\chi^2$ 근사가 $k$가 아니라 $k-1$인 것은 "$k-1$개 처리만 비교해서"가 아니라, **순위합의 총합이 고정된 선형제약**이기 때문 — one-way ANOVA 처리 자유도와 완전히 같은 근원.
- **Friedman의 블록 SS $\equiv 0$ 역설**: 블록 효과가 "존재하지 않는다"는 뜻이 아니다. RCBD를 쓰는 이유(개체차를 통제) 자체가 **행 내부 순위화로 이미 수행됐기** 때문에 SS로 다시 안 잡히는 것. 그런데도 F검정 분모자유도는 $(b-1)(k-1)$로, 마치 블록을 추정한 것처럼 자유도를 뺀다 — 순위화가 "블록 추정을 대신했다"고 보는 것이 정확한 해석.
- **ARE**: 정규 대립가설 하 Kruskal-Wallis의 one-way F-검정 대비 점근상대효율(Pitman ARE)은 $3/\pi\approx0.955$로, $k$에 무관하며 [[순위 검정 — 부호·Wilcoxon·Mann-Whitney]]의 Wilcoxon-Mann-Whitney vs t-검정 ARE와 **동일한 값**. (KW가 WMW의 직계 확장이라는 사실의 점근이론적 반영.)
- **동점 보정은 항상 방향이 같지 않다**: 예제 2에서 동점 미보정 $S=7.583$인데 보정 후 $S'=8.273$으로 **오히려 커진다** — 분모 $R^*-C=11$이 무동점 상수 $bk(k^2-1)/12=12$보다 작아지므로. 동점이 분산을 깎는 만큼 통계량을 키워 검정력을 보존하는 방향으로 작동한다.
- **Quade 검정**: Friedman의 대안으로 Wilcoxon signed-rank를 확장한 Quade(1966) 검정이 있으나 일반적으로 Friedman과 성능이 비슷하고 $k=3$에서만 약간 우세 — K&V는 언급만 하고 다루지 않음.

## 연결 개념
- [[일원 ANOVA 제곱합 분해 — Hogg §9.2]] — Kruskal-Wallis가 순위 위에서 재현하는 원본 SS 분해. → 🗺️ [[MOC_이차형식]] Cluster B.
- [[순위 검정 — 부호·Wilcoxon·Mann-Whitney]] — $k=2$일 때 $H=Z^2$으로 정확히 합류하는 뿌리.
- [[반복측정 설계와 구형성 가정 (Mauchly 검정)]] — RCBD·반복측정 ANOVA가 정규성 못 버틸 때의 비모수 대안으로 교차 언급 (Ch14_반복측정ANOVA_구형성_정리노트).
- [[McNemar 검정]] — 분포 가정을 순위·부호로 대체하는 같은 계보의 분포무관 검정.
- Kendall의 일치도 계수 $W=S/(b(k-1))$ — Friedman 통계량을 "$b$명 평가자 간 평균 순위상관"으로 재해석하는 관점 (K&V는 별도로 다루지 않음, Conover 1999 참고).

## 참고 교재 페이지
- Kvam & Vidakovic, *Nonparametric Statistics with Applications to Science and Engineering* (Wiley, 2007), **§8.1–8.2, 책 p.141–149** (PDF p.152–160, offset 11).
- Kruskal, W.H. & Wallis, W.A. (1952). "Use of Ranks in One-Criterion Variance Analysis." *JASA* 47, 583–621.
- Friedman, M. (1937). "The Use of Ranks to Avoid the Assumption of Normality Implicit in the Analysis of Variance." *JASA* 32, 675–701.
- Iman, R.L. & Davenport, J.M. (1980). "Approximations of the Critical Region of the Friedman Statistic." *Comm. Stat. A* 9, 571–595.
