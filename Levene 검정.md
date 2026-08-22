---
aliases: [Levene 검정, Levene's test, 르빈 검정, Brown-Forsythe 검정, 등분산 검정]
tags: [실험설계, 회귀분석, 등분산성, ANOVA가정, 가설검정, 회귀진단, ClusterB, ClusterC]
subject: 실험설계법
chapter: ["Montgomery Ch3 §3.4 잔차분석", "김충락 Ch4 회귀진단"]
book_pages: "Montgomery 8th §3.4.3"
moc: ["[[MOC_이차형식]]"]
cluster: [B, C]
cross_ref: ["Montgomery §3.4.3", "김충락 Ch4"]
date_created: 2026-08-22
---

# Levene 검정

> [!info] 📖 교재 위치 · 커리큘럼
> **본거지**: Montgomery 8판 §3.4.3 — 일원 ANOVA의 [[등분산성(homoscedasticity)]] 가정 점검.
> **커리큘럼 연결**: [[MOC_이차형식]] (Cluster B) 가지 ⑤. 회귀 맥락의 대응물은 [[Breusch-Pagan 검정]].

## 1. 아이디어

$$
H_0:\ \sigma_1^2=\sigma_2^2=\cdots=\sigma_k^2
$$

**절대편차를 새로운 반응변수로 삼아 그 위에서 ANOVA를 돌린다.**

$$
Z_{ij}=\big|\,y_{ij}-\tilde y_{i\cdot}\,\big|
\qquad\Longrightarrow\qquad
W=\frac{(N-k)}{(k-1)}\cdot\frac{\sum_i n_i(\bar Z_{i\cdot}-\bar Z_{\cdot\cdot})^2}{\sum_i\sum_j (Z_{ij}-\bar Z_{i\cdot})^2}\ \sim\ F(k-1,\ N-k)
$$

**중심 $\tilde y_{i\cdot}$ 의 선택**이 변종을 가른다:

| 중심 | 이름 | 특성 |
|---|---|---|
| 집단 **중앙값** | **Brown–Forsythe** (R `center="median"`, 기본 권장) | 비정규·이상치에 강건 |
| 집단 **평균** | 원래 Levene | 정규일 때 검정력 약간 우위 |
| 10% 절사평균 | trimmed | 두꺼운 꼬리 대응 |

> [!note] 왜 이 구조가 아름다운가
> 등분산 검정이 **또 하나의 ANOVA**다. 분산의 차이를 위치(평균)의 차이로 **번역**해 놓고 같은 [[F-검정]] 엔진을 재사용한다. 이차형식 비(ratio of quadratic forms)라는 골격이 여기서도 반복된다 → [[이차형식]]

## 2. Bartlett과의 비교

| | Levene / Brown–Forsythe | Bartlett |
|---|---|---|
| 정규성 의존 | **낮음** (강건) | **매우 높음** — 비정규 시 등분산이어도 기각 |
| 정규일 때 검정력 | 약간 낮음 | 높음 |
| 실무 권장 | ✅ 기본 선택 | 정규성이 확인된 경우에만 |

## 3. R

```r
library(car)
leveneTest(y ~ group, data = df)                 # 기본 center = median (Brown-Forsythe)
leveneTest(y ~ group, data = df, center = mean)  # 원래 Levene
bartlett.test(y ~ group, data = df)              # 정규성 확인 후에만
```

ANOVA 3대 가정 점검 세트: Shapiro–Wilk(정규성) · **Levene**(등분산성) · Durbin–Watson([[Durbin-Watson 검정]], 독립성).

## 4. 한계 — 통과가 타당성을 뜻하지 않는다

> [!danger] 2026-08-22 세션 실증
> $N(50,100)$ 을 평균에서 잘라 만든 가짜 두 집단([[자기참조적 집단화와 F검정의 함정]])에 대해 3,000회 반복:
>
> ```
> Levene  기각률 = 5.17%   ← 명목 5%. 완벽 통과
> Shapiro 기각률 = 39.5%   ← 60%는 통과
> 그럼에도 F검정 기각률 = 100%  (존재하지 않는 효과)
> ```
>
> 대칭 절단이라 두 조각의 분산이 **진짜로 같기** 때문에 Levene은 잡을 것이 없다. 가정검정은 **모형 내부의 조건**만 본다 — 집단이 어떻게 만들어졌는지는 데이터 안에 없다. → [[데이터 누출 (Data Leakage)]] · [[무작위화 (Randomization)]]

> [!tip] 실무 판단
> 표본이 크면 사소한 이분산도 기각되고, 작으면 심한 이분산도 놓친다. **$p$값보다 분산비의 크기**를 보라 — 최대/최소 분산비가 3 미만이고 집단크기가 균형이면 ANOVA는 상당히 강건하다. 위배 시 Welch ANOVA 또는 [[가중최소제곱(WLS)]].

## 5. 연결

[[등분산성(homoscedasticity)]] · [[Breusch-Pagan 검정]] · [[F-검정]] · [[ANOVA SS 분해]] · [[자기참조적 집단화와 F검정의 함정]] · [[Ch04_잔차가정검정_백지유도]] · [[Ch14_반복측정ANOVA_구형성_정리노트]] · [[MOC_이차형식]]
