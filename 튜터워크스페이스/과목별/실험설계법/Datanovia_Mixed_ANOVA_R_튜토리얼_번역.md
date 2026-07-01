---
aliases: [Mixed ANOVA 번역, 혼합 분산분석 R 튜토리얼, Datanovia Mixed ANOVA]
subject: 실험설계법
chapter: Ch14 반복측정 설계 (혼합설계 확장 참조자료)
concept: '[[반복측정 설계와 구형성 가정 (Mauchly 검정)]]'
tags:
- 반복측정
- 혼합설계
- MixedANOVA
- rstatix
- 삼원혼합설계
- 번역자료
- 실험설계법
source: "Datanovia — Mixed ANOVA in R: The Ultimate Guide (https://www.datanovia.com/en/lessons/mixed-anova-in-r/)"
related: '[[Ch14_반복측정ANOVA_구형성_정리노트]]'
date_created: "2026-06-14"
status: "참조 튜토리얼 (한국어 번역)"
---

> [!info] 참조 노트
> 이 문서는 외부 튜토리얼의 한국어 번역 **참조자료**입니다. 핵심 이론·ADP 풀이는 [[Ch14_반복측정ANOVA_구형성_정리노트]]에 정리되어 있습니다. 이 파일은 **이원 → 삼원 혼합설계**로의 확장(단순·단순단순 효과 분해 절차 포함)을 R(`rstatix`) 흐름으로 보여줍니다.

# R에서의 혼합 분산분석(Mixed ANOVA): 완벽 가이드

> 원문: Datanovia — [Mixed ANOVA in R: The Ultimate Guide](https://www.datanovia.com/en/lessons/mixed-anova-in-r/)
> 소요 시간: 약 25분

**혼합 분산분석(Mixed ANOVA)** 은 서로 다른 두 종류의 요인(factor) 변수에 의해 교차 분류된 집단들의 평균을 비교하는 데 사용됩니다. 두 종류의 요인은 다음과 같습니다.

- **개체 간 요인(between-subjects factors)**: 서로 독립적인 범주를 갖는 요인 (예: 성별 — 남/여)
- **개체 내 요인(within-subjects factors)**: 서로 관련된 범주를 갖는 요인으로, 반복측정(repeated measures)이라고도 함 (예: 시점 — 처치 전/후)

혼합 분산분석은 *혼합 설계 분산분석(mixed design ANOVA)* 또는 *혼합 측정 분산분석(mixed measures ANOVA)* 이라고도 불립니다.

이 장에서는 다음과 같은 여러 유형의 혼합 분산분석을 다룹니다.

- **이원 혼합 분산분석(two-way mixed ANOVA)**: 두 개의 독립적인 범주형 변수(개체 간 요인 1개 + 개체 내 요인 1개)로 교차 분류된 집단들의 평균을 비교할 때 사용
- **삼원 혼합 분산분석(three-way mixed ANOVA)**: 세 개의 독립변수(개체 간 요인과 개체 내 요인 포함) 사이에 삼원 상호작용이 있는지 평가할 때 사용. 삼원 혼합 분산분석에는 두 가지 설계가 가능합니다.
  1. 개체 간 요인 1개 + 개체 내 요인 2개
  2. 개체 간 요인 2개 + 개체 내 요인 1개

이 글에서 배우게 될 내용은 다음과 같습니다.

- R에서 다양한 혼합 분산분석을 **계산하고 해석**하는 법
- 혼합 분산분석의 **가정을 점검**하는 법
- **사후 검정(post-hoc tests)**, 즉 어떤 집단들이 서로 다른지 식별하기 위한 집단 간 다중 쌍별 비교를 수행하는 법
- 상자그림(box plot)으로 **데이터를 시각화**하고, 그림에 분산분석 및 쌍별 비교의 p-값을 추가하는 법

**목차**

- [가정](#가정)
- [사전 준비](#사전-준비)
- [이원 혼합 분산분석](#이원-혼합-분산분석)
- [삼원 혼합 분산분석: 개체 간 요인 2개 + 개체 내 요인 1개](#삼원-혼합-분산분석-개체-간-요인-2개--개체-내-요인-1개)
- [삼원 혼합 분산분석: 개체 간 요인 1개 + 개체 내 요인 2개](#삼원-혼합-분산분석-개체-간-요인-1개--개체-내-요인-2개)
- [요약](#요약)

---

## 가정

혼합 분산분석은 데이터에 대해 다음과 같은 가정을 합니다.

- **유의한 이상치(outlier)가 없을 것**: 설계의 어떤 셀(cell)에도 유의한 이상치가 없어야 합니다. 상자그림으로 데이터를 시각화하거나 `identify_outliers()` 함수[rstatix 패키지]로 확인할 수 있습니다.
- **정규성(Normality)**: 결과변수(종속변수)가 설계의 각 셀에서 근사적으로 정규분포를 따라야 합니다. **Shapiro-Wilk 정규성 검정**(`shapiro_test()` [rstatix])이나 **QQ 플롯**(`ggqqplot()` [ggpubr 패키지])을 통한 시각적 확인으로 점검할 수 있습니다.
- **분산의 동질성(Homogeneity of variances)**: 개체 간 요인의 집단들 사이에서 결과변수의 분산이 같아야 합니다. **Levene 등분산 검정**(`levene_test()` [rstatix])으로 평가할 수 있습니다.
- **구형성 가정(Assumption of sphericity)**: 개체 내 집단들 사이 차이값의 분산이 같아야 합니다. **Mauchly 구형성 검정**으로 점검하며, `anova_test()` 함수를 사용하면 자동으로 보고됩니다.
- **공분산의 동질성(Homogeneity of covariances)**: Box의 M 검정으로 검정합니다. 개체 간 요인이 형성하는 셀들 전반에서 공분산 행렬이 같아야 합니다.

혼합 분산분석을 계산하기 전에, 이러한 가정들이 충족되는지 확인하기 위한 몇 가지 예비 검정을 수행해야 합니다.

---

## 사전 준비

다음 R 패키지들이 설치되어 있는지 확인하세요.

- `tidyverse`: 데이터 조작 및 시각화
- `ggpubr`: 출판 수준의 그림을 손쉽게 작성
- `rstatix`: 파이프(pipe) 친화적인 통계 분석 함수 제공
- `datarium`: 이 장에 필요한 데이터셋 포함

다음 패키지들을 불러오는 것으로 시작합니다.

```r
library(tidyverse)
library(ggpubr)
library(rstatix)
```

**핵심 R 함수**

- `anova_test()` [rstatix 패키지]: 반복측정 분산분석을 쉽게 계산할 수 있도록 `car::Anova()`를 감싼 래퍼(wrapper) 함수. 반복측정 분산분석 수행 시 주요 인자는 다음과 같습니다.
  - `data`: 데이터 프레임
  - `dv`: (수치형) 종속변수(결과변수) 이름
  - `wid`: 사례/표본 식별자 변수 이름
  - `between`: 개체 간 요인(집단 변수)
  - `within`: 개체 내 요인(집단 변수)
- `get_anova_table()` [rstatix 패키지]: `anova_test()`의 출력으로부터 분산분석표를 추출합니다. 구형성 가정 위배 시 이를 자동으로 보정한 분산분석표를 반환합니다. 기본 동작은 구형성 가정을 위배한 개체 내 요인(즉 Mauchly 검정 p-값이 유의한 경우, p ≤ 0.05)에 대해서만 Greenhouse-Geisser 구형성 보정을 자동 적용하는 것입니다.

---

## 이원 혼합 분산분석

### 데이터 준비

`anxiety`(불안) 데이터셋[datarium 패키지]을 사용합니다. 이 데이터는 서로 다른 수준의 신체 운동을 하는 세 집단(grp1: 기본, grp2: 보통, grp3: 고강도)에 대해 세 시점(t1, t2, t3)에서 측정한 불안 점수를 담고 있습니다.

이원 혼합 분산분석은 불안 점수를 설명함에 있어 집단(group)과 시점(time) 사이에 상호작용이 있는지 평가하는 데 사용할 수 있습니다.

데이터를 불러오고 집단별로 임의의 한 행을 보여줍니다.

```r
# 넓은(wide) 형식
set.seed(123)
data("anxiety", package = "datarium")
anxiety %>% sample_n_by(group, size = 1)
```

```
## # A tibble: 3 x 5
##   id    group    t1    t2    t3
##   <fct> <fct> <dbl> <dbl> <dbl>
## 1 5     grp1   16.5  15.8  15.7
## 2 27    grp2   17.8  17.7  16.9
## 3 37    grp3   17.1  15.6  14.3
```

```r
# t1, t2, t3 열을 긴(long) 형식으로 모음
# id와 time을 요인형 변수로 변환
anxiety <- anxiety %>%
  gather(key = "time", value = "score", t1, t2, t3) %>%
  convert_as_factor(id, time)
# 집단별로 임의의 일부 행 확인
set.seed(123)
anxiety %>% sample_n_by(group, time, size = 1)
```

```
## # A tibble: 9 x 4
##   id    group time  score
##   <fct> <fct> <fct> <dbl>
## 1 5     grp1  t1     16.5
## 2 12    grp1  t2     17.7
## 3 7     grp1  t3     16.5
## 4 29    grp2  t1     18.4
## 5 30    grp2  t2     18.9
## 6 16    grp2  t3     12.7
## # … with 3 more rows
```

### 요약 통계량

데이터를 `time`과 `group`으로 묶은 뒤 `score` 변수의 요약 통계량(평균, 표준편차)을 계산합니다.

```r
anxiety %>%
  group_by(time, group) %>%
  get_summary_stats(score, type = "mean_sd")
```

```
## # A tibble: 9 x 6
##   group time  variable     n  mean    sd
##   <fct> <fct> <chr>    <dbl> <dbl> <dbl>
## 1 grp1  t1    score       15  17.1  1.63
## 2 grp2  t1    score       15  16.6  1.57
## 3 grp3  t1    score       15  17.0  1.32
## 4 grp1  t2    score       15  16.9  1.70
## 5 grp2  t2    score       15  16.5  1.70
## 6 grp3  t2    score       15  15.0  1.39
## # … with 3 more rows
```

### 시각화

상자그림을 생성합니다.

```r
bxp <- ggboxplot(
  anxiety, x = "time", y = "score",
  color = "group", palette = "jco"
  )
bxp
```

### 가정 점검

#### 이상치

이상치는 `identify_outliers()` 함수[rstatix 패키지]에 구현된 상자그림 방법으로 쉽게 식별할 수 있습니다.

```r
anxiety %>%
  group_by(time, group) %>%
  identify_outliers(score)
```

```
## [1] group      time       id         score      is.outlier is.extreme
## <0 rows> (or 0-length row.names)
```

극단적 이상치는 없었습니다.

극단적 이상치가 있는 경우, 그 원인은 1) 데이터 입력 오류, 측정 오류, 혹은 비정상적인 값일 수 있습니다.

결과가 실질적으로 영향을 받지 않으리라 판단되면 이상치를 분석에 포함해도 됩니다. 이는 이상치를 포함했을 때와 제외했을 때의 분산분석 결과를 비교하여 평가할 수 있습니다.

또한 이상치를 데이터에 그대로 두고 WRS2 패키지를 사용해 로버스트(robust) 분산분석을 수행하는 것도 가능합니다.

#### 정규성 가정

정규성 가정은 요인 수준의 각 조합에 대해 Shapiro-Wilk 검정을 계산하여 점검할 수 있습니다. 데이터가 정규분포를 따른다면 p-값은 0.05보다 커야 합니다.

```r
anxiety %>%
  group_by(time, group) %>%
  shapiro_test(score)
```

```
## # A tibble: 9 x 5
##   group time  variable statistic     p
##   <fct> <fct> <chr>        <dbl> <dbl>
## 1 grp1  t1    score        0.964 0.769
## 2 grp2  t1    score        0.977 0.949
## 3 grp3  t1    score        0.954 0.588
## 4 grp1  t2    score        0.956 0.624
## 5 grp2  t2    score        0.935 0.328
## 6 grp3  t2    score        0.952 0.558
## # … with 3 more rows
```

Shapiro-Wilk 정규성 검정 결과, 각 셀에서 점수는 정규분포를 따랐습니다(p > 0.05).

참고로, 표본 크기가 50보다 크면 정규 QQ 플롯을 선호하는 것이 좋습니다. 표본이 커질수록 Shapiro-Wilk 검정은 사소한 정규성 이탈에도 매우 민감해지기 때문입니다.

QQ 플롯은 주어진 데이터와 정규분포 사이의 상관을 그립니다.

```r
ggqqplot(anxiety, "score", ggtheme = theme_bw()) +
  facet_grid(time ~ group)
```

각 셀에서 모든 점이 대략 기준선을 따라 떨어집니다. 따라서 데이터의 정규성을 가정할 수 있습니다.

가정이 충족되지 않는 경우, 변환한 데이터로 이원 반복측정 분산분석을 수행하거나 WRS2 패키지로 로버스트 분산분석을 수행하는 것을 고려할 수 있습니다.

#### 분산의 동질성 가정

개체 간 요인(`group`)의 분산 동질성 가정은 Levene 검정으로 점검할 수 있습니다. 검정은 `time` 변수의 각 수준에서 수행됩니다.

```r
anxiety %>%
  group_by(time) %>%
  levene_test(score ~ group)
```

```
## # A tibble: 3 x 5
##   time    df1   df2 statistic     p
##   <fct> <int> <int>     <dbl> <dbl>
## 1 t1        2    42     0.176 0.839
## 2 t2        2    42     0.249 0.781
## 3 t3        2    42     0.335 0.717
```

Levene 검정 결과 분산의 동질성이 성립했습니다(p > 0.05).

분산의 동질성이 성립하지 않는 경우, 결과변수(종속변수)를 변환하여 불균등한 분산을 보정해 볼 수 있습니다. 또한 WRS2 패키지로 로버스트 분산분석을 수행하는 것도 가능합니다.

#### 공분산의 동질성 가정

개체 간 요인(`group`)의 공분산 동질성은 `rstatix` 패키지에 구현된 **Box의 M 검정**으로 평가할 수 있습니다. 이 검정이 통계적으로 유의하면(즉 p < 0.001) 공분산이 동일하지 않은 것이고, 유의하지 않으면(즉 p > 0.001) 공분산이 동일하여 공분산 동질성 가정을 위배하지 않은 것입니다.

참고로 Box의 M 검정은 매우 민감하므로, p < 0.001이면서 표본 크기가 불균등하지 않다면 무시해도 됩니다. 다만 유의하면서 표본 크기가 불균등하다면 이 검정은 로버스트하지 않습니다(Tabachnick & Fidell, 2001).

Box의 M 검정 계산:

```r
box_m(anxiety[, "score", drop = FALSE], anxiety$group)
```

```
## # A tibble: 1 x 4
##   statistic p.value parameter method  
##       <dbl>   <dbl>     <dbl> <chr>  
## 1      1.93   0.381         2 Box's M-test for Homogeneity of Covariance Matrices
```

Box의 공분산 행렬 동일성 검정 결과 공분산의 동질성이 성립했습니다(p > 0.001).

공분산의 동질성이 성립하지 않는 경우, 분석을 각 집단별 별도의 반복측정 분산분석으로 분리하는 것을 고려할 수 있습니다. 또는 상호작용 항의 해석을 생략할 수도 있습니다.

안타깝게도 이 가정의 위배를 바로잡기는 어렵습니다. 흔히 혼합 분산분석을 그대로 실행하되 위배 사실을 명시합니다.

#### 구형성 가정

앞 절들에서 언급했듯, 구형성 가정은 `anova_test()` 함수[rstatix 패키지]로 분산분석을 계산하는 과정에서 자동으로 점검됩니다. 내부적으로 Mauchly 검정이 사용되어 구형성 가정을 평가합니다.

`get_anova_table()` 함수[rstatix]로 분산분석표를 추출하면, 구형성 가정을 위배한 요인에 대해 Greenhouse-Geisser 구형성 보정이 자동으로 적용됩니다.

### 계산

```r
# 이원 혼합 분산분석
res.aov <- anova_test(
  data = anxiety, dv = score, wid = id,
  between = group, within = time
  )
get_anova_table(res.aov)
```

```
## ANOVA Table (type II tests)
##
##       Effect DFn DFd      F        p p<.05   ges
## 1      group   2  42   4.35 1.90e-02     * 0.168
## 2       time   2  84 394.91 1.91e-43     * 0.179
## 3 group:time   4  84 110.19 1.38e-32     * 0.108
```

위 출력에서, 불안 점수에 대한 집단(group)과 시점(time)의 이원 상호작용이 통계적으로 유의함을 알 수 있습니다, F(4, 84) = 110.18, p < 0.0001.

### 사후 검정

**유의한 이원 상호작용**은 한 요인이 결과변수에 미치는 영향이 다른 요인의 수준에 따라 달라짐(그 역도 성립)을 의미합니다. 따라서 유의한 이원 상호작용을 다음과 같이 분해할 수 있습니다.

- **단순 주효과(Simple main effect)**: 두 번째 변수(요인 B)의 각 수준에서 첫 번째 변수(요인 A)에 대한 일원 모형을 실행
- **단순 쌍별 비교(Simple pairwise comparisons)**: 단순 주효과가 유의하면, 어느 집단이 다른지 결정하기 위해 다중 쌍별 비교를 실행

**유의하지 않은 이원 상호작용**의 경우, 분산분석 출력에서 통계적으로 유의한 **주효과(main effects)** 가 있는지 판단해야 합니다.

#### 유의한 이원 상호작용에 대한 절차

**집단(group) 변수의 단순 주효과.** 이 예제에서는 각 `time` 시점에서 개체 간 요인 `group`이 불안 점수에 미치는 효과를 조사합니다.

```r
# 각 시점에서 group의 효과
one.way <- anxiety %>%
  group_by(time) %>%
  anova_test(dv = score, wid = id, between = group) %>%
  get_anova_table() %>%
  adjust_pvalue(method = "bonferroni")
one.way
```

```
## # A tibble: 3 x 9
##   time  Effect   DFn   DFd      F         p `p<.05`   ges     p.adj
##   <fct> <chr>  <dbl> <dbl>  <dbl>     <dbl> <chr>   <dbl>     <dbl>
## 1 t1    group      2    42  0.365 0.696     ""      0.017 1  
## 2 t2    group      2    42  5.84  0.006     *       0.218 0.018  
## 3 t3    group      2    42 13.8   0.0000248 *       0.396 0.0000744
```

```r
# group 수준 간 쌍별 비교
pwc <- anxiety %>%
  group_by(time) %>%
  pairwise_t_test(score ~ group, p.adjust.method = "bonferroni")
pwc
```

```
## # A tibble: 9 x 10
##   time  .y.   group1 group2    n1    n2       p p.signif   p.adj p.adj.signif
## * <fct> <chr> <chr>  <chr>  <int> <int>   <dbl> <chr>      <dbl> <chr>  
## 1 t1    score grp1   grp2      15    15 0.43    ns       1       ns  
## 2 t1    score grp1   grp3      15    15 0.895   ns       1       ns  
## 3 t1    score grp2   grp3      15    15 0.51    ns       1       ns  
## 4 t2    score grp1   grp2      15    15 0.435   ns       1       ns  
## 5 t2    score grp1   grp3      15    15 0.00212 **       0.00636 **  
## 6 t2    score grp2   grp3      15    15 0.0169  *        0.0507  ns  
## # … with 3 more rows
```

Bonferroni 보정 p-값(p.adj)을 고려하면, 집단의 단순 주효과는 t2(p = 0.018)와 t3(p < 0.0001)에서 유의했지만 t1(p = 1)에서는 유의하지 않았음을 알 수 있습니다.

쌍별 비교 결과, 평균 불안 점수는 t2에서 grp1 대 grp3 비교(p = 0.0063), t3에서 grp1 대 grp3(p < 0.0001) 및 grp2 대 grp3(p = 0.0013)에서 유의하게 달랐습니다.

**시점(time) 변수의 단순 주효과.** 다음 R 코드처럼 각 `group` 수준에서 개체 내 요인 `time`에 대해 동일한 분석을 수행할 수도 있습니다. 이 분석이 반드시 필요한 것은 아닙니다.

```r
# 각 운동 집단 수준에서 time의 효과
one.way2 <- anxiety %>%
  group_by(group) %>%
  anova_test(dv = score, wid = id, within = time) %>%
  get_anova_table() %>%
  adjust_pvalue(method = "bonferroni")
one.way2
```

```
## # A tibble: 3 x 9
##   group Effect   DFn   DFd     F        p `p<.05`   ges    p.adj
##   <fct> <chr>  <dbl> <dbl> <dbl>    <dbl> <chr>   <dbl>    <dbl>
## 1 grp1  time       2    28  14.8 4.05e- 5 *       0.024 1.21e- 4
## 2 grp2  time       2    28  77.5 3.88e-12 *       0.086 1.16e-11
## 3 grp3  time       2    28 490.  1.64e-22 *       0.531 4.92e-22
```

```r
# 각 group 수준에서 시점 간 쌍별 비교
# 시점에 따른 반복측정이므로 대응표본 t-검정 사용
pwc2 <- anxiety %>%
  group_by(group) %>%
  pairwise_t_test(
    score ~ time, paired = TRUE,
    p.adjust.method = "bonferroni"
    ) %>%
  select(-df, -statistic, -p) # 세부 정보 제거
pwc2
```

```
## # A tibble: 9 x 8
##   group .y.   group1 group2    n1    n2        p.adj p.adj.signif
## * <fct> <chr> <chr>  <chr>  <int> <int>        <dbl> <chr>  
## 1 grp1  score t1     t2        15    15 0.194        ns  
## 2 grp1  score t1     t3        15    15 0.002        **  
## 3 grp1  score t2     t3        15    15 0.006        **  
## 4 grp2  score t1     t2        15    15 0.268        ns  
## 5 grp2  score t1     t3        15    15 0.000000151  ****  
## 6 grp2  score t2     t3        15    15 0.0000000612 ****  
## # … with 3 more rows
```

세 집단 각각에서 시점이 불안 점수에 미치는 효과가 통계적으로 유의했습니다. 대응표본 쌍별 t-검정 결과, grp1과 grp2에서는 t1과 t2 시점 사이의 평균 불안 점수가 통계적으로 유의하게 다르지 않았습니다.

t1 대 t3, t2 대 t3 쌍별 비교는 모든 집단에서 통계적으로 유의하게 달랐습니다.

#### 유의하지 않은 이원 상호작용에 대한 절차

상호작용이 유의하지 않은 경우, 두 변수(`group`과 `time`) 각각의 주효과를 해석해야 합니다. 유의한 주효과는 쌍별 비교로 후속 분석할 수 있습니다.

이 예제에서는 불안 점수에 대해 집단(F(2, 42) = 4.35, p = 0.02)과 시점(F(2, 84) = 394.91, p < 0.0001)의 주효과가 통계적으로 유의했습니다.

집단을 무시하고 `time` 변수에 대해 다중 대응표본 t-검정을 수행합니다. p-값은 Bonferroni 다중검정 보정으로 조정됩니다.

```r
anxiety %>%
  pairwise_t_test(
    score ~ time, paired = TRUE,
    p.adjust.method = "bonferroni"
  )
```

모든 쌍별 비교가 유의합니다.

`group` 변수에 대해서도 유사한 분석을 수행할 수 있습니다.

```r
anxiety %>%
  pairwise_t_test(
    score ~ group,
    p.adjust.method = "bonferroni"
  )
```

grp1 대 grp2를 제외한 모든 쌍별 비교가 유의합니다.

### 보고

운동 집단과 시점 사이에 불안 점수를 설명하는 통계적으로 유의한 상호작용이 있었습니다, F(4, 84) = 110.19, p < 0.0001.

Bonferroni 보정 p-값을 고려하면, 운동 집단의 단순 주효과는 t2(p = 0.018)와 t3(p < 0.0001)에서 유의했지만 t1(p = 1)에서는 유의하지 않았습니다.

쌍별 비교 결과, 평균 불안 점수는 t2에서 grp1 대 grp3(p = 0.0063), t3에서 grp1 대 grp3(p < 0.0001) 및 grp2 대 grp3(p = 0.0013)에서 유의하게 달랐습니다.

아래 그림에서는 t2와 t3의 쌍별 비교 결과만 필요하고 t1은 필요 없습니다(이 시점에서는 운동 집단의 단순 주효과가 유의하지 않았기 때문). 그에 맞게 비교 결과를 필터링합니다.

```r
# 시각화: p-값을 포함한 상자그림
pwc <- pwc %>% add_xy_position(x = "time")
pwc.filtered <- pwc %>% filter(time != "t1")
bxp +
  stat_pvalue_manual(pwc.filtered, tip.length = 0, hide.ns = TRUE) +
  labs(
    subtitle = get_test_label(res.aov, detailed = TRUE),
    caption = get_pwc_label(pwc)
  )
```

---

## 삼원 혼합 분산분석: 개체 간 요인 2개 + 개체 내 요인 1개

이 절에서는 **개체 간 요인 2개와 개체 내 요인 1개** 가 있는 상황에서 R로 삼원 혼합 분산분석을 계산하는 법을 설명합니다.

이 설정은 두 개체 간 요인의 조합으로 형성된 집단들이 시간(즉 개체 내 요인)에 따라 보이는 집단 차이를 조사하기 위한 것입니다. 예를 들어, 성과 점수가 성별(남/여)과 스트레스(낮음, 보통, 높음)에 따라 시간(예: 0, 4, 8개월)에 걸쳐 어떻게 변하는지 알아보고 싶을 수 있습니다.

### 데이터 준비

두 시점에서 측정한 참가자들의 성과 점수를 담은 `performance` 데이터셋[datarium 패키지]을 사용합니다. 이 연구의 목적은 성별과 스트레스가 성과 점수에 미치는 효과를 평가하는 것입니다.

데이터는 다음 변수들을 포함합니다.

1. 두 시점 `t1`과 `t2`에서 측정한 성과 점수(결과변수, 종속변수)
2. 두 개의 개체 간 요인: `gender`(수준: male, female)와 `stress`(low, moderate, high)
3. 하나의 개체 내 요인 `time`: 두 시점 `t1`과 `t2`를 가짐

데이터를 불러오고 집단별로 임의의 한 행을 보여줍니다.

```r
# 데이터 불러오기 및 확인
# 넓은(wide) 형식
set.seed(123)
data("performance", package = "datarium")
performance %>% sample_n_by(gender, stress, size = 1)
```

```
## # A tibble: 6 x 5
##      id gender stress      t1    t2
##   <int> <fct>  <fct>    <dbl> <dbl>
## 1     3 male   low       5.63  5.47
## 2    18 male   moderate  5.57  5.78
## 3    25 male   high      5.48  5.74
## 4    39 female low       5.50  5.66
## 5    50 female moderate  5.96  5.32
## 6    51 female high      5.59  5.06
```

```r
# t1, t2 열을 긴(long) 형식으로 모음
# id와 time을 요인형 변수로 변환
performance <- performance %>%
  gather(key = "time", value = "score", t1, t2) %>%
  convert_as_factor(id, time)
# 집단별로 임의의 일부 행 확인
set.seed(123)
performance %>% sample_n_by(gender, stress, time, size = 1)
```

```
## # A tibble: 12 x 5
##   id    gender stress   time  score
##   <fct> <fct>  <fct>    <fct> <dbl>
## 1 3     male   low      t1     5.63
## 2 8     male   low      t2     5.92
## 3 15    male   moderate t1     5.96
## 4 19    male   moderate t2     5.76
## 5 30    male   high     t1     5.38
## 6 21    male   high     t2     5.64
## # … with 6 more rows
```

### 요약 통계량

데이터를 `gender`, `stress`, `time`으로 묶은 뒤 `score` 변수의 요약 통계량(평균, 표준편차)을 계산합니다.

```r
performance %>%
  group_by(gender, stress, time ) %>%
  get_summary_stats(score, type = "mean_sd")
```

```
## # A tibble: 12 x 7
##   gender stress   time  variable     n  mean    sd
##   <fct>  <fct>    <fct> <chr>    <dbl> <dbl> <dbl>
## 1 male   low      t1    score       10  5.72 0.19
## 2 male   low      t2    score       10  5.70 0.143
## 3 male   moderate t1    score       10  5.72 0.193
## 4 male   moderate t2    score       10  5.77 0.155
## 5 male   high     t1    score       10  5.48 0.121
## 6 male   high     t2    score       10  5.64 0.195
## # … with 6 more rows
```

### 시각화

`gender`별 성과 `score`의 상자그림을 `stress` 수준으로 색을 입히고 `time`으로 면 분할(facet)하여 생성합니다.

```r
bxp <- ggboxplot(
  performance, x = "gender", y = "score",
  color = "stress", palette = "jco",
  facet.by =  "time"
  )
bxp
```

### 가정 점검

#### 이상치

```r
performance %>%
  group_by(gender, stress, time) %>%
  identify_outliers(score)
```

```
## # A tibble: 1 x 7
##   gender stress time  id    score is.outlier is.extreme
##   <fct>  <fct>  <fct> <fct> <dbl> <lgl>      <lgl>  
## 1 female low    t2    36     6.15 TRUE       FALSE
```

극단적 이상치는 없었습니다.

#### 정규성 가정

요인 수준의 각 조합에 대해 Shapiro-Wilk 검정을 계산합니다.

```r
performance %>%
  group_by(gender, stress, time ) %>%
  shapiro_test(score)
```

```
## # A tibble: 12 x 6
##   gender stress   time  variable statistic      p
##   <fct>  <fct>    <fct> <chr>        <dbl>  <dbl>
## 1 male   low      t1    score        0.942 0.574
## 2 male   low      t2    score        0.966 0.849
## 3 male   moderate t1    score        0.848 0.0547
## 4 male   moderate t2    score        0.958 0.761
## 5 male   high     t1    score        0.915 0.319
## 6 male   high     t2    score        0.925 0.403
## # … with 6 more rows
```

Shapiro-Wilk 정규성 검정 결과, 각 셀에서 점수는 정규분포를 따랐습니다(p > 0.05).

설계의 각 셀에 대해 QQ 플롯을 생성합니다.

```r
ggqqplot(performance, "score", ggtheme = theme_bw()) +
  facet_grid(time ~ stress, labeller = "label_both")
```

각 셀에서 모든 점이 대략 기준선을 따라 떨어집니다. 따라서 데이터의 정규성을 가정할 수 있습니다.

#### 분산의 동질성 가정

개체 내 요인(여기서는 `time` 변수)의 각 수준에서 Levene 검정을 계산합니다.

```r
performance %>%
  group_by(time) %>%
  levene_test(score ~ gender*stress)
```

```
## # A tibble: 2 x 5
##   time    df1   df2 statistic     p
##   <fct> <int> <int>     <dbl> <dbl>
## 1 t1        5    54     0.974 0.442
## 2 t2        5    54     0.722 0.610
```

Levene 등분산 검정 결과 분산의 동질성이 성립했습니다(p > .05).

#### 구형성 가정

이원 혼합 분산분석 절에서 언급했듯, Mauchly 구형성 검정과 구형성 보정은 `anova_test()` 및 `get_anova_table()` 함수[rstatix 패키지] 내부에서 자동으로 수행됩니다.

### 계산

```r
res.aov <- anova_test(
  data = performance, dv = score, wid = id,
  within = time, between = c(gender, stress)
  )
get_anova_table(res.aov)
```

```
## ANOVA Table (type II tests)
##
##               Effect DFn DFd      F        p p<.05      ges
## 1             gender   1  54  2.406 1.27e-01       0.023000
## 2             stress   2  54 21.166 1.63e-07     * 0.288000
## 3               time   1  54  0.063 8.03e-01       0.000564
## 4      gender:stress   2  54  1.554 2.21e-01       0.029000
## 5        gender:time   1  54  4.730 3.40e-02     * 0.041000
## 6        stress:time   2  54  1.821 1.72e-01       0.032000
## 7 gender:stress:time   2  54  6.101 4.00e-03     * 0.098000
```

시점, 성별, 스트레스 사이에 통계적으로 유의한 삼원 상호작용이 있었습니다, F(2, 54) = 6.10, p = 0.004.

### 사후 검정

**유의한 삼원 상호작용 효과가 있는 경우**, 다음과 같이 분해할 수 있습니다.

- **단순 이원 상호작용(Simple two-way interaction)**: 세 번째 변수의 각 수준에서 이원 상호작용을 실행
- **단순 단순 주효과(Simple simple main effect)**: 두 번째 변수의 각 수준에서 일원 모형을 실행
- **단순 단순 쌍별 비교(simple simple pairwise comparisons)**: 필요 시 쌍별 또는 기타 사후 비교를 실행

**통계적으로 유의한 삼원 상호작용이 없는 경우**, 분산분석 출력에서 통계적으로 유의한 이원 상호작용이 있는지 판단해야 합니다. 유의한 이원 상호작용은 단순 주효과 분석으로, 그것이 유의하면 단순 쌍별 비교로 후속 분석할 수 있습니다.

이 절에서는 유의한 삼원 상호작용에 대한 절차를 설명합니다.

#### 단순 이원 상호작용 계산

어떤 두 변수가 단순 이원 상호작용을 형성하고 어떤 변수가 세 번째 변수 역할을 할지는 자유롭게 정할 수 있습니다.

다음 R 코드에서는 각 `time` 수준에서 `gender*stress`의 단순 이원 상호작용을 고려했습니다.

데이터를 `time`(개체 내 요인)으로 묶고, 개체 간 요인인 `gender`와 `stress` 사이의 단순 이원 상호작용을 분석합니다.

```r
# 각 time 수준에서의 이원 상호작용
two.way <- performance %>%
  group_by(time) %>%
  anova_test(dv = score, wid = id, between = c(gender, stress))
two.way
```

```
## # A tibble: 6 x 8
##   time  Effect          DFn   DFd      F          p `p<.05`   ges
##   <fct> <chr>         <dbl> <dbl>  <dbl>      <dbl> <chr>   <dbl>
## 1 t1    gender            1    54  0.186 0.668      ""      0.003
## 2 t1    stress            2    54 14.9   0.00000723 *       0.355
## 3 t1    gender:stress     2    54  2.12  0.131      ""      0.073
## 4 t2    gender            1    54  5.97  0.018      *       0.1  
## 5 t2    stress            2    54  9.60  0.000271   *       0.262
## 6 t2    gender:stress     2    54  4.95  0.011      *       0.155
```

t2에서 성별과 스트레스의 단순 이원 상호작용이 통계적으로 유의했지만(F(2, 54) = 4.95, p = 0.011), t1에서는 유의하지 않았습니다(F(2, 54) = 2.12, p = 0.13).

참고로, 단순 이원 상호작용의 통계적 유의성은 Bonferroni 보정 유의수준 0.025에서 판정했습니다. 이는 현재 유의성을 선언하는 수준(즉 p < 0.05)을 계산하는 단순 이원 상호작용의 개수(즉 2)로 나눈 값입니다.

#### 단순 단순 주효과 계산

통계적으로 유의한 단순 이원 상호작용은 **단순 단순 주효과** 로 후속 분석할 수 있습니다.

이 예제에서는 `gender`의 각 수준에서 `stress`가 성과 점수에 미치는 효과를 조사하거나, `stress`의 각 수준에서 `gender`의 효과를 조사할 수 있습니다.

참고로, 단순 이원 상호작용이 유의했던 유일한 경우는 "t2"였으므로 이에 대해서만 분석하면 됩니다.

데이터를 `time`과 `gender`로 묶고, `stress`가 성과 점수에 미치는 단순 주효과를 분석합니다.

```r
stress.effect <- performance %>%
  group_by(time, gender) %>%
  anova_test(dv = score, wid = id, between = stress)
stress.effect %>% filter(time == "t2")
```

```
## # A tibble: 2 x 9
##   gender time  Effect   DFn   DFd     F        p `p<.05`   ges
##   <fct>  <fct> <chr>  <dbl> <dbl> <dbl>    <dbl> <chr>   <dbl>
## 1 male   t2    stress     2    27  1.57 0.227    ""      0.104
## 2 female t2    stress     2    27 10.5  0.000416 *       0.438
```

위 표에서 `time = t2`의 결과만 필요합니다. 단순 단순 주효과의 통계적 유의성은 Bonferroni 보정 유의수준 0.025에서 판정했습니다. 즉 0.05를 계산하는 단순 단순 주효과의 개수(즉 2)로 나눈 값입니다.

t2 시점에서 여성에 대해서는 스트레스가 성과 점수에 미치는 단순 단순 주효과가 통계적으로 유의했지만(F(2, 27) = 10.5, p = 0.0004), 남성에 대해서는 유의하지 않았습니다(F(2, 27) = 1.57, p = 0.23).

#### 단순 단순 비교 계산

통계적으로 유의한 단순 단순 주효과는 **다중 쌍별 비교** 로 후속 분석하여 어느 집단 평균이 다른지 결정할 수 있습니다.

앞 절에서 스트레스의 효과가 여성에 대해서만 유의했으므로, 여성의 쌍별 비교 결과에만 집중하면 됩니다.

데이터를 `time`과 `gender`로 묶고, Bonferroni 보정으로 `stress` 수준 간 쌍별 비교를 수행합니다.

```r
# 쌍별 비교 적합
pwc <- performance %>%
  group_by(time, gender) %>%
  pairwise_t_test(score ~ stress, p.adjust.method = "bonferroni") %>%
  select(-p, -p.signif) # 세부 정보 제거
# t2에서 "female"의 결과에 집중
pwc %>% filter(time == "t2", gender == "female")
```

```
## # A tibble: 3 x 9
##   gender time  .y.   group1   group2      n1    n2    p.adj p.adj.signif
##   <fct>  <fct> <chr> <chr>    <chr>    <int> <int>    <dbl> <chr>  
## 1 female t2    score low      moderate    10    10 0.323    ns  
## 2 female t2    score low      high        10    10 0.000318 ***  
## 3 female t2    score moderate high        10    10 0.0235   *
```

여성의 경우, 평균 성과 점수는 낮은 스트레스와 높은 스트레스 수준 사이(p < 0.001), 그리고 보통 스트레스와 높은 스트레스 수준 사이(p = 0.023)에서 통계적으로 유의하게 달랐습니다.

낮은 스트레스와 보통 스트레스 집단 사이에는 유의한 차이가 없었습니다(p = 0.32).

### 보고

성별, 스트레스, 시점이 성과 점수에 미치는 효과를 평가하기 위해 삼원 혼합 분산분석을 수행했습니다.

상자그림 방법으로 평가한 결과 극단적 이상치는 없었습니다. Shapiro-Wilk 정규성 검정 결과 데이터는 정규분포를 따랐습니다(p > 0.05). Levene 등분산 검정 결과 분산의 동질성이 성립했습니다(p > 0.05).

성별, 스트레스, 시점 사이에 통계적으로 유의한 삼원 상호작용이 있었습니다, F(2, 54) = 6.10, p = 0.004.

단순 이원 상호작용과 단순 단순 주효과에 대해서는 Bonferroni 보정을 적용하여 p < 0.025 수준에서 통계적 유의성을 판정했습니다.

t2 시점에서 성별과 스트레스 사이에 통계적으로 유의한 단순 이원 상호작용이 있었지만(F(2, 54) = 4.95, p = 0.011), t1에서는 없었습니다(F(2, 54) = 2.12, p = 0.13).

t2 시점에서 여성에 대해 스트레스가 성과 점수에 미치는 단순 단순 주효과가 통계적으로 유의했지만(F(2, 27) = 10.5, p = 0.0004), 남성에 대해서는 그렇지 않았습니다(F(2, 27) = 1.57, p = 0.23).

t2 시점 여성에 대해 서로 다른 스트레스 집단 간 모든 단순 단순 쌍별 비교를 실행했으며, Bonferroni 보정을 적용했습니다.

평균 성과 점수는 낮은 스트레스와 높은 스트레스 수준 사이(p < 0.001), 그리고 보통 스트레스와 높은 스트레스 수준 사이(p = 0.024)에서 통계적으로 유의하게 달랐습니다. 낮은 스트레스와 보통 스트레스 집단 사이에는 유의한 차이가 없었습니다(p = 0.32).

```r
# 시각화: p-값을 포함한 상자그림
pwc <- pwc %>% add_xy_position(x = "gender")
pwc.filtered <- pwc %>% filter(time == "t2", gender == "female")
bxp +
  stat_pvalue_manual(pwc.filtered, tip.length = 0, hide.ns = TRUE) +
  labs(
    subtitle = get_test_label(res.aov, detailed = TRUE),
    caption = get_pwc_label(pwc)
  )
```

---

## 삼원 혼합 분산분석: 개체 간 요인 1개 + 개체 내 요인 2개

이 절에서는 **개체 간 요인 1개와 개체 내 요인 2개** 가 있는 상황에서 R로 삼원 혼합 분산분석을 계산하는 법을 설명합니다. 예를 들어, 참가자의 식이요법(`diet:no`, `diet:yes`)에 따라, 운동을 하는 사람과 하지 않는 사람의 체중감량 점수가 세 시점(t1, t2, t3)에 걸쳐 어떻게 다른지 알아보고 싶을 수 있습니다.

### 데이터 준비

datarium 패키지의 `weightloss` 데이터셋을 사용합니다. 이 데이터셋은 원래 삼원 반복측정 분산분석을 위해 만들어졌습니다. 다만 이 글의 예제에서는 삼원 혼합 설계에 맞도록 데이터를 약간 수정합니다.

한 연구자가 `exercises`(운동) 프로그램과 `diet`(식이요법)에 따라 `time`(시점)이 체중감량 점수에 미치는 효과를 평가하고자 했습니다.

체중감량 점수는 두 집단에서 측정되었습니다. 운동을 하는 참가자 집단(`exercises:yes`)과 운동을 하지 않는 또 다른 집단(`exercises:no`)입니다.

각 참가자는 또한 두 가지 시행(trial)에 참여했습니다. (1) 식이요법 없음, (2) 식이요법. 시행 순서는 균형을 맞추었고(counterbalanced), 이전 시행의 효과가 사라지도록 시행 간 충분한 시간을 두었습니다.

각 시행은 9주간 지속되었으며, 체중감량 점수는 각 시행의 시작(t1), 중간(t2), 끝(t3)에서 측정되었습니다.

이 연구 설계에서는 24명을 모집했습니다. 이 중 12명은 `exercises:no` 집단, 12명은 `exercises:yes` 집단에 속합니다. 24명은 두 차례의 연속된 시행(`diet:no`와 `diet:yes`)에 참여했고, 체중감량 `score`는 세 시점에서 반복 측정되었습니다.

이 설정에서는 다음과 같습니다.

- 종속변수(결과변수) 1개: `score`
- 개체 간 요인 1개: `exercises`
- 개체 내 요인 2개: `diet`와 `time`

삼원 혼합 분산분석을 수행하여 식이요법, 운동, 시점 사이에 체중감량 점수에 대한 유의한 상호작용이 있는지 판단할 수 있습니다.

데이터를 불러오고 집단별로 임의의 일부 행을 확인합니다.

```r
# 원본 데이터 불러오기
# 넓은(wide) 형식
data("weightloss", package = "datarium")
# 삼원 혼합 설계가 되도록 수정
weightloss <- weightloss %>%
  mutate(id = rep(1:24, 2)) # 두 차례의 시행
# 집단별로 임의의 한 행 표시
set.seed(123)
weightloss %>% sample_n_by(diet, exercises, size = 1)
```

```
## # A tibble: 4 x 6
##      id diet  exercises    t1    t2    t3
##   <int> <fct> <fct>     <dbl> <dbl> <dbl>
## 1     4 no    no         11.1   9.5  11.1
## 2    22 no    yes        10.2  11.8  17.4
## 3     5 yes   no         11.6  13.4  13.9
## 4    23 yes   yes        12.7  12.7  15.1
```

```r
# t1, t2, t3 열을 긴(long) 형식으로 모음
# id와 time을 요인형 변수로 변환
weightloss <- weightloss %>%
  gather(key = "time", value = "score", t1, t2, t3) %>%
  convert_as_factor(id, time)
# 집단별로 임의의 일부 행 확인
set.seed(123)
weightloss %>% sample_n_by(diet, exercises, time, size = 1)
```

```
## # A tibble: 12 x 5
##   id    diet  exercises time  score
##   <fct> <fct> <fct>     <fct> <dbl>
## 1 4     no    no        t1     11.1
## 2 10    no    no        t2     10.7
## 3 5     no    no        t3     12.3
## 4 23    no    yes       t1     10.2
## 5 24    no    yes       t2     13.2
## 6 13    no    yes       t3     15.8
## # … with 6 more rows
```

### 요약 통계량

데이터를 `exercises`, `diet`, `time`으로 묶은 뒤 `score` 변수의 요약 통계량(평균, 표준편차)을 계산합니다.

```r
weightloss %>%
  group_by(exercises, diet, time) %>%
  get_summary_stats(score, type = "mean_sd")
```

```
## # A tibble: 12 x 7
##   diet  exercises time  variable     n  mean    sd
##   <fct> <fct>     <fct> <chr>    <dbl> <dbl> <dbl>
## 1 no    no        t1    score       12  10.9 0.868
## 2 no    no        t2    score       12  11.6 1.30
## 3 no    no        t3    score       12  11.4 0.935
## 4 yes   no        t1    score       12  11.7 0.938
## 5 yes   no        t2    score       12  12.4 1.42
## 6 yes   no        t3    score       12  13.8 1.43
## # … with 6 more rows
```

### 시각화

`exercises` 집단별 체중감량 `score`의 상자그림을 `time`으로 색을 입히고 `diet` 시행으로 면 분할(facet)하여 생성합니다.

```r
bxp <- ggboxplot(
  weightloss, x = "exercises", y = "score",
  color = "time", palette = "jco",
  facet.by = "diet", short.panel.labs = FALSE
  )
bxp
```

### 가정 점검

#### 이상치

```r
weightloss %>%
  group_by(diet, exercises, time) %>%
  identify_outliers(score)
```

```
## # A tibble: 5 x 7
##   diet  exercises time  id    score is.outlier is.extreme
##   <fct> <fct>     <fct> <fct> <dbl> <lgl>      <lgl>  
## 1 no    no        t3    2      13.2 TRUE       FALSE  
## 2 yes   no        t1    1      10.2 TRUE       FALSE  
## 3 yes   no        t1    3      13.2 TRUE       FALSE  
## 4 yes   no        t1    4      10.2 TRUE       FALSE  
## 5 yes   no        t2    10     15.3 TRUE       FALSE
```

극단적 이상치는 없었습니다.

#### 정규성 가정

요인 수준의 각 조합에 대해 Shapiro-Wilk 검정을 계산합니다.

```r
weightloss %>%
  group_by(diet, exercises, time) %>%
  shapiro_test(score)
```

```
## # A tibble: 12 x 6
##   diet  exercises time  variable statistic     p
##   <fct> <fct>     <fct> <chr>        <dbl> <dbl>
## 1 no    no        t1    score        0.917 0.264
## 2 no    no        t2    score        0.957 0.743
## 3 no    no        t3    score        0.965 0.851
## 4 no    yes       t1    score        0.922 0.306
## 5 no    yes       t2    score        0.912 0.229
## 6 no    yes       t3    score        0.953 0.674
## # … with 6 more rows
```

Shapiro-Wilk 정규성 검정 결과 체중감량 점수는 정규분포를 따랐습니다(p > 0.05).

설계의 각 셀에 대해 QQ 플롯을 생성합니다.

```r
ggqqplot(weightloss, "score", ggtheme = theme_bw()) +
  facet_grid(diet + exercises ~ time, labeller = "label_both")
```

위 그림에서 모든 점이 대략 기준선을 따라 떨어지므로 정규성을 가정할 수 있습니다.

#### 분산의 동질성 가정

데이터를 `diet`와 `time` 범주로 묶은 뒤 Levene 검정을 계산합니다.

```r
weightloss %>%
  group_by(diet, time) %>%
  levene_test(score ~ exercises)
```

```
## # A tibble: 6 x 6
##   diet  time    df1   df2 statistic      p
##   <fct> <fct> <int> <int>     <dbl>  <dbl>
## 1 no    t1        1    22    2.44   0.132
## 2 no    t2        1    22    0.691  0.415
## 3 no    t3        1    22    2.87   0.105
## 4 yes   t1        1    22    0.376  0.546
## 5 yes   t2        1    22    0.0574 0.813
## 6 yes   t3        1    22    5.14   0.0336
```

Levene 등분산 검정 결과, diet:yes & time:t3 조건(p = 0.034)을 제외한 모든 셀에서 분산의 동질성이 성립했습니다(p > 0.05).

분산의 동질성이 성립하지 않는 경우, 결과변수(종속변수)를 변환하여 불균등한 분산을 보정해 볼 수 있습니다.

집단 표본 크기가 (근사적으로) 같다면, 이러한 상황에서 삼원 혼합 분산분석은 분산의 이질성에 다소 로버스트하므로 그대로 실행해도 됩니다.

또한 WRS2 패키지로 로버스트 분산분석을 수행하는 것도 가능합니다.

#### 구형성 가정

이원 혼합 분산분석 절에서 언급했듯, Mauchly 구형성 검정과 구형성 보정은 `anova_test()` 및 `get_anova_table()` 함수[rstatix 패키지] 내부에서 자동으로 수행됩니다.

### 계산

```r
res.aov <- anova_test(
  data = weightloss, dv = score, wid = id,
  between = exercises, within = c(diet, time)
  )
get_anova_table(res.aov)
```

```
## ANOVA Table (type II tests)
##
##                Effect DFn DFd      F        p p<.05   ges
## 1           exercises   1  22 38.771 2.88e-06     * 0.284
## 2                diet   1  22  7.912 1.00e-02     * 0.028
## 3                time   2  44 82.199 1.38e-15     * 0.541
## 4      exercises:diet   1  22 51.698 3.31e-07     * 0.157
## 5      exercises:time   2  44 26.222 3.18e-08     * 0.274
## 6           diet:time   2  44  0.784 4.63e-01       0.013
## 7 exercises:diet:time   2  44  9.966 2.69e-04     * 0.147
```

위 출력에서 운동, 식이요법, 시점 사이에 통계적으로 유의한 삼원 상호작용이 있음을 알 수 있습니다, F(2, 44) = 9.96, p = 0.00027.

참고로, 삼원 상호작용이 통계적으로 유의하지 않은 경우에는 출력의 이원 상호작용을 참고해야 합니다.

이 예제에서는 통계적으로 유의한 이원 exercises*diet 상호작용(p < 0.0001)과 이원 exercises*time 상호작용(p < 0.0001)이 있었습니다. 이원 diet*time 상호작용은 통계적으로 유의하지 않았습니다(p = 0.46).

### 사후 검정

**유의한 삼원 상호작용 효과가 있는 경우**, 다음과 같이 분해할 수 있습니다.

- **단순 이원 상호작용(Simple two-way interaction)**: 세 번째 변수의 각 수준에서 이원 상호작용을 실행
- **단순 단순 주효과(Simple simple main effect)**: 두 번째 변수의 각 수준에서 일원 모형을 실행
- **단순 단순 쌍별 비교(simple simple pairwise comparisons)**: 필요 시 쌍별 또는 기타 사후 비교를 실행

**통계적으로 유의한 삼원 상호작용이 없는 경우**, 분산분석 출력에서 통계적으로 유의한 이원 상호작용이 있는지 판단해야 합니다. 유의한 이원 상호작용은 단순 주효과 분석으로, 필요 시 집단 간 쌍별 비교로 후속 분석할 수 있습니다.

이 절에서는 유의한 삼원 상호작용에 대한 절차를 설명합니다.

#### 단순 이원 상호작용 계산

이 예제에서는 각 `exercises` 수준에서 `diet*time` 상호작용을 고려합니다. 데이터를 `exercises`로 묶고 `diet`와 `time` 사이의 단순 이원 상호작용을 분석합니다.

```r
# 각 exercises 집단 수준에서의 이원 분산분석
two.way <- weightloss %>%
  group_by(exercises) %>%
  anova_test(dv = score, wid = id, within = c(diet, time))
two.way
```

```
## # A tibble: 2 x 2
##   exercises anova  
##   <fct>     <list>  
## 1 no        <anov_tst>
## 2 yes       <anov_tst>
```

```r
# 분산분석표 추출
get_anova_table(two.way)
```

```
## # A tibble: 6 x 8
##   exercises Effect      DFn   DFd      F        p `p<.05`   ges
##   <fct>     <chr>     <dbl> <dbl>  <dbl>    <dbl> <chr>   <dbl>
## 1 no        diet          1    11  56.4  1.18e- 5 *       0.262
## 2 no        time          2    22   5.90 9.00e- 3 *       0.181
## 3 no        diet:time     2    22   2.91 7.60e- 2 ""      0.09
## 4 yes       diet          1    11   8.60 1.40e- 2 *       0.066
## 5 yes       time          2    22 148.   1.73e-13 *       0.746
## 6 yes       diet:time     2    22   7.81 3.00e- 3 *       0.216
```

exercises:yes 집단에서는 식이요법과 시점 사이에 통계적으로 유의한 단순 이원 상호작용이 있었지만(F(2, 22) = 7.81, p = 0.0027), exercises:no 집단에서는 없었습니다(F(2, 22) = 2.91, p = 0.075).

참고로, 단순 이원 상호작용의 통계적 유의성은 Bonferroni 보정 유의수준 0.025에서 판정했습니다. 이는 현재 유의성을 선언하는 수준(즉 p < 0.05)을 계산하는 단순 이원 상호작용의 개수(즉 2)로 나눈 값입니다.

#### 단순 단순 주효과 계산

통계적으로 유의한 단순 이원 상호작용은 **단순 단순 주효과** 로 후속 분석할 수 있습니다.

이 예제에서는 `diet`의 각 수준에서 `time`이 체중감량 점수에 미치는 효과를 조사하거나, `time`의 각 수준에서 `diet`의 효과를 조사할 수 있습니다.

참고로, 단순 이원 상호작용이 유의했던 유일한 집단은 "exercises:yes"였으므로 이에 대해서만 분석하면 됩니다.

데이터를 `exercises`와 `diet`로 묶고, `time`의 단순 주효과를 분석합니다.

```r
time.effect <- weightloss %>%
  group_by(exercises, diet) %>%
  anova_test(dv = score, wid = id, within = time) %>%
  get_anova_table()
time.effect %>% filter(exercises == "yes")
```

```
## # A tibble: 2 x 9
##   diet  exercises Effect   DFn   DFd     F        p `p<.05`   ges
##   <fct> <fct>     <chr>  <dbl> <dbl> <dbl>    <dbl> <chr>   <dbl>
## 1 no    yes       time       2    22  78.8 9.30e-11 *       0.801
## 2 yes   yes       time       2    22  30.9 4.06e- 7 *       0.655
```

위 표에서 `exercises = yes`의 결과만 필요합니다. 단순 단순 주효과의 통계적 유의성은 Bonferroni 보정 유의수준 0.025에서 판정했습니다. 즉 0.05를 계산하는 단순 단순 주효과의 개수(즉 2)로 나눈 값입니다.

운동 조건 하에서 시점이 체중감량 점수에 미치는 단순 단순 주효과는 diet:no(F(2,22) = 78.81, p < 0.0001)와 diet:yes(F(2, 22) = 30.92, p < 0.0001) 집단 모두에서 통계적으로 유의했습니다.

#### 단순 단순 비교 계산

통계적으로 유의한 단순 단순 주효과는 **다중 쌍별 비교** 로 후속 분석하여 어느 집단 평균이 다른지 결정할 수 있습니다.

exercises:yes의 쌍별 비교 결과에만 집중하면 된다는 점을 기억하세요.

데이터를 `exercises`와 `diet`로 묶고, Bonferroni 보정으로 `time` 시점 간 쌍별 비교를 수행합니다. 대응표본 t-검정을 사용합니다.

```r
# 쌍별 비교 계산
pwc <- weightloss %>%
  group_by(exercises, diet) %>%
  pairwise_t_test(
    score ~ time, paired = TRUE,
    p.adjust.method = "bonferroni"
    ) %>%
  select(-statistic, -df) # 세부 정보 제거
# exercises:yes 집단의 결과에 집중
pwc %>% filter(exercises == "yes") %>%
  select(-p)    # p 열 제거
```

```
## # A tibble: 6 x 9
##   diet  exercises .y.   group1 group2    n1    n2        p.adj p.adj.signif
##   <fct> <fct>     <chr> <chr>  <chr>  <int> <int>        <dbl> <chr>  
## 1 no    yes       score t1     t2        12    12 0.000741     ***  
## 2 no    yes       score t1     t3        12    12 0.0000000121 ****  
## 3 no    yes       score t2     t3        12    12 0.000257     ***  
## 4 yes   yes       score t1     t2        12    12 0.01         **  
## 5 yes   yes       score t1     t3        12    12 0.00000124   ****  
## 6 yes   yes       score t2     t3        12    12 0.02         *
```

운동 조건(즉 exercises:yes) 하에서 diet:no 및 diet:yes 시행에 대해 서로 다른 시점 간 모든 단순 단순 쌍별 비교를 실행했으며, Bonferroni 보정을 적용했습니다.

운동을 수행했을 때 평균 체중감량 점수는 모든 시점 비교에서 유의하게 달랐습니다(p < 0.05).

### 보고

식이요법, 운동, 시점이 체중감량에 미치는 효과를 평가하기 위해 삼원 혼합 분산분석을 수행했습니다.

상자그림 방법으로 평가한 결과 극단적 이상치는 없었습니다. Shapiro-Wilk 정규성 검정 결과 데이터는 정규분포를 따랐습니다(p > 0.05). Levene 등분산 검정 결과 분산의 동질성이 성립했습니다(p > 0.05). 삼원 상호작용 효과에 대해 Mauchly 구형성 검정 결과 구형성 가정이 충족됨을 보였습니다(p > 0.05).

운동, 식이요법, 시점 사이에 통계적으로 유의한 삼원 상호작용이 있었습니다, F(2, 44) = 9.96, p < 0.001.

단순 이원 상호작용과 단순 단순 주효과에 대해서는 Bonferroni 보정을 적용하여 p < 0.025 수준에서 통계적 유의성을 판정했습니다.

exercises:yes 집단에서는 식이요법과 시점 사이에 통계적으로 유의한 단순 이원 상호작용이 있었지만(F(2, 22) = 7.81, p = 0.0027), exercises:no 집단에서는 없었습니다(F(2, 22) = 2.91, p = 0.075).

운동 조건 하에서 시점이 체중감량 점수에 미치는 단순 단순 주효과는 diet:no(F(2,22) = 78.81, p < 0.0001)와 diet:yes(F(2, 22) = 30.92, p < 0.0001) 집단 모두에서 통계적으로 유의했습니다.

운동 조건(즉 exercises:yes) 하에서 diet:no 및 diet:yes 시행에 대해 서로 다른 시점 간 모든 단순 단순 쌍별 비교를 실행했으며, Bonferroni 보정을 적용했습니다. 운동을 수행했을 때 평균 체중감량 점수는 모든 시점 비교에서 유의하게 달랐습니다(p < 0.05).

```r
# 시각화: p-값을 포함한 상자그림
pwc <- pwc %>% add_xy_position(x = "exercises")
pwc.filtered <- pwc %>% filter(exercises == "yes")
bxp +
  stat_pvalue_manual(pwc.filtered, tip.length = 0, hide.ns = TRUE) +
  labs(
    subtitle = get_test_label(res.aov, detailed = TRUE),
    caption = get_pwc_label(pwc)
  )
```

---

## 요약

이 글에서는 R에서 혼합 분산분석을 계산하고 해석하는 법을 설명했습니다. 또한 혼합 분산분석이 하는 가정들을 설명하고, 검정 가정이 충족되는지 점검하는 실용적인 R 코드 예제를 제공했습니다.
