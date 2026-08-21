---
aliases: [모수와 추정량, β와 β̂ 구분, 무작위성의 발원지, 두 종류의 공분산, X 비확률성, "모수 β와 추정량 β̂ — 두 종류의 공분산", 선형모형의 확률구조]
tags: [회귀분석, 3장, 1장, 중선형회귀모형, 가정, 모수와추정량, 확률구조, 공분산]
chapter: ["제3장 중선형회귀모형", "제1장 기초통계이론"]
book_pages: "97-162 (Ch3), 1-38 (Ch1)"
moc: ["[[MOC_추정효율성]]"]
cluster: [A]
subject: 회귀분석
concept: "[[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]]"
cross_ref: ["김충락·강근석 『회귀분석』 2판 제3장 (책 97–162) · 제1장 (책 1–38)"]
date_created: 2026-06-29
date_modified: 2026-08-21
---

# Ch03 선형모형의 확률구조 — 고정설계·모수와 추정량·$\sigma^2 I$

> [!info] 📖 교재 위치 (김충락·강근석 『회귀분석』 2판)
> **본거지**: 제3장 중선형회귀모형 (책 97–162쪽) — 행렬형 모형 $\mathbf y = X\beta+\varepsilon$, 가정, $\text{Cov}(\hat\beta)=\sigma^2(X^\top X)^{-1}$.
> **뿌리 개념**: 제1장 기초통계이론 (책 1–38쪽) — 확률변수·기댓값·공분산의 정의.
> **커리큘럼 연결**: [[MOC_추정효율성]] (Cluster A) 가지 ⓪ 기초. 이 노트는 불편성·분산·[[Gauss-Markov 정리]] 가지의 **전제(prerequisite)**.

> [!question] 출발 의문
> 다중 선형 회귀에서 설명변수 $X$를 **상수(비확률)** 로 가정하는데, 그렇다면 변수들 사이에 "공분산"은 왜 존재하는가? 그리고 $X\beta$는 왜 상수 인자인가?

---

## 1. 한 단어, 두 정체 — "공분산"

같은 "공분산"이라는 말이 서로 다른 두 자리에 쓰인다.

| 구분 | 표본공분산 (설명변수 사이) | 확률적 공분산 $\text{Cov}(\cdot)$ |
|---|---|---|
| 정의 | $s_{jk}=\dfrac{1}{n-1}\sum_i (x_{ij}-\bar{x}_j)(x_{ik}-\bar{x}_k)$ | $\text{Cov}(X,Y)=E[(X-EX)(Y-EY)]$ |
| 필요한 것 | 고정된 숫자 $n$쌍만 있으면 됨 | **기댓값 $E[\cdot]$** → 분포가 있어야 함 |
| 성격 | **결정론적 함수** | 확률변수에만 정당하게 붙음 |
| 회귀에서의 위치 | $X^\top X$ 의 **비대각 원소** | $\varepsilon$, $\mathbf{y}$, $\hat{\beta}$ 의 몫 |

핵심: 설명변수 "사이의 공분산"은 확률과 무관한 **기술통계량**이다. 그러므로 $X$를 고정상수로 두어도 모순이 전혀 없다. 이것이 [[다중공선성]]과 [[분산팽창인자(VIF)]]가 실제로 가리키는 대상 — 고정행렬 $X^\top X$ 의 성질 — 이다.

---

## 2. [[확률변수]]란 무엇인가

> **확률변수** $X:\Omega\to\mathbb{R}$ : 무작위 실험의 표본공간 $\Omega$의 각 결과 $\omega$에 실수 하나를 대응시키는 함수.

- 손에 쥔 숫자 $x_{ij}=173.2$ → **이미 멈춘 눈금** (실현값, realized value)
- 확률변수 → **던지기 전의 주사위** (분포를 동반한 메커니즘)

확률적 공분산에는 $E[\cdot]$ 가 들어 있고, $E$는 분포가 있어야 정의된다. 이미 적힌 숫자 더미에는 $E$를 붙일 자리가 없고, 그 자리는 산술평균 $\bar{x}$로 대체될 뿐이다.

---

## 3. 모형 속 세 대상의 분류 — $\mathbf{y}=X\beta+\varepsilon$

| 대상 | 정체 | 이유 |
|---|---|---|
| $X$ | 고정상수 | 비확률 설계행렬 가정 |
| $\beta$ (모형 안) | **고정 미지의 상수** | 데이터 이전에 자연이 정해 둔 참값 = **모수** |
| $\varepsilon$ | **확률변수** | 분포 $\varepsilon\sim(\mathbf 0,\sigma^2 I)$ 를 가짐 |
| $\mathbf{y}$ | **확률변수** | 고정 $X\beta$ + 확률변수 $\varepsilon$ |
| $\hat{\beta}=(X^\top X)^{-1}X^\top\mathbf{y}$ | **확률변수** | $\mathbf{y}$의 선형결합 = **추정량** |

> [!important] 결정적 구분: $\beta$ vs $\hat{\beta}$
> - **모형 안의 $\beta$** = 모수(parameter), 고정 미지의 상수. → $X$도 고정이므로 $X\beta$ 는 **상수 인자**. (출발 의문 해소)
> - **$\hat{\beta}$** = 추정량(estimator), 확률변수.
> - "$\beta$가 $\mathbf y$의 선형결합"이라는 직관은 사실 $\beta$가 아니라 $\hat{\beta}$ 에 대한 것이었다.

### 무작위성의 발원지

$$
\varepsilon \;\longrightarrow\; \mathbf{y}=X\beta+\varepsilon \;\longrightarrow\; \hat{\beta}=(X^\top X)^{-1}X^\top\mathbf{y}
$$

무작위성은 오직 $\varepsilon$ 에서 발원하여, $\mathbf{y}$를 거쳐 선형변환 $(X^\top X)^{-1}X^\top$ 를 타고 $\hat{\beta}$ 로 흘러든다.

---

## 4. $\mathbf{y}$ 의 공분산

분산-공분산 연산자의 성질: 상수 벡터를 더해도 공분산은 불변, $\text{Cov}(\mathbf a+\mathbf z)=\text{Cov}(\mathbf z)$ ($\mathbf a$ 고정).

$$
\text{Cov}(\mathbf{y})=\text{Cov}(X\beta+\varepsilon)=\text{Cov}(\varepsilon)=\sigma^2 I
$$

고정된 $X\beta$ 는 위치만 옮길 뿐 산포에는 손대지 못하므로 통째로 빠진다.

---

## 5. 오차 공분산 행렬 $\sigma^2 I$ 의 구조

오차는 $\varepsilon_1,\dots,\varepsilon_n$ 로 $n$개 → $\boldsymbol{\varepsilon}$ 는 $n\times 1$ 벡터.
공분산 행렬의 $(i,j)$ 원소는 $\text{Cov}(\varepsilon_i,\varepsilon_j)$ 이고, $i,j$ 가 각각 $1\dots n$ 을 도므로 행렬 크기는 **$n\times n$** (= 관측치 개수).

일반형:

$$
\text{Cov}(\boldsymbol{\varepsilon})=
\begin{pmatrix}
\text{Var}(\varepsilon_1) & \text{Cov}(\varepsilon_1,\varepsilon_2) & \cdots & \text{Cov}(\varepsilon_1,\varepsilon_n)\\
\text{Cov}(\varepsilon_2,\varepsilon_1) & \text{Var}(\varepsilon_2) & \cdots & \vdots\\
\vdots & & \ddots & \vdots\\
\text{Cov}(\varepsilon_n,\varepsilon_1) & \cdots & \cdots & \text{Var}(\varepsilon_n)
\end{pmatrix}
$$

이것이 $\sigma^2 I_n$ 으로 납작하게 줄어든다는 가정의 의미:

$$
\text{Cov}(\boldsymbol{\varepsilon})=\sigma^2 I_n \;\Longleftrightarrow\;
\underbrace{\text{Var}(\varepsilon_i)=\sigma^2\ \forall i}_{\text{대각: 등분산성}}
\;\text{이고}\;
\underbrace{\text{Cov}(\varepsilon_i,\varepsilon_j)=0\ (i\neq j)}_{\text{비대각: 무상관}}
$$

| 부분 | 값 | 가정 이름 | 의미 |
|---|---|---|---|
| 대각 원소 | 모두 $\sigma^2$ | **등분산성(homoscedasticity)** | 모든 관측치의 오차 산포가 일정 |
| 비대각 원소 | 모두 $0$ | **무상관(uncorrelated)** | 서로 다른 오차끼리 선형 연관 없음 |

> [!warning] 무상관 ≠ 독립
> 비대각 $0$ 이 보장하는 것은 **무상관**이지 독립이 아니다.
> - 독립 $\Rightarrow$ 공분산 $0$ : 항상 성립
> - 공분산 $0 \Rightarrow$ 독립 : **일반적으로 성립하지 않음**
> - 단, 오차벡터가 **(결합)정규분포**를 따를 때에 한해 무상관과 독립이 일치한다.
>
> 그래서 [[Gauss-Markov 정리]]는 약한 가정(무상관)만으로 세우고, 정규성은 검정·구간추정 단계에서 따로 얹는다.

---

## 6. [[Gauss-Markov 정리]]로 가는 길

$X$ 고정 가정 덕분에 $(X^\top X)^{-1}X^\top$ 를 **상수 행렬**로 꺼낼 수 있고, 같은 논리로:

$$
E(\hat{\beta})=\beta \quad(\text{불편성}), \qquad
\text{Cov}(\hat{\beta})=\sigma^2 (X^\top X)^{-1}
$$

상수는 $E$ 밖으로 / 공분산에서 빠지고, 무작위 부분만 남아 깔끔하게 떨어진다. 이것이 [[Gauss-Markov 정리]] 의 골격이다.

---

## 7. 1장 한 장의 지도

- 설명변수 "사이 공분산" 의문 → $X^\top X$ 비대각 (결정론적) → [[다중공선성]], [[분산팽창인자(VIF)]]
- $X\beta$ 가 상수인 이유 → $X$ 고정 + $\beta$(모수) 고정
- 확률성이 사는 곳 → $\varepsilon \to \mathbf{y} \to \hat{\beta}$ → 불편성·공분산 유도 → [[Gauss-Markov 정리]]

> [!summary] 한 줄 요약
> 같은 이름·같은 기호라도 **모수/추정량**, **결정론적 공분산/확률적 공분산**은 정체가 다르다. 회귀의 모든 확률성은 오차항 한 곳에서 발원한다.
