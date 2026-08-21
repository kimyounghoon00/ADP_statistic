---
subject: 회귀분석
chapter: Ch2 단순선형회귀모형 (스칼라형) · Ch3 중선형회귀모형 (행렬형)
concept: "[[최소제곱추정량(LSE)]]"
aliases: ["최소제곱추정량(LSE)", 최소제곱추정량, LSE, OLS, 정규방정식, "정규방정식과 LSE 유도", "단순회귀모형의 LSE 유도", "다중회귀모형의 LSE 행렬 유도", 최소제곱법]
cluster: [E, A]
cross_ref:
  - "김충락·강근석 『회귀분석』 2판 제2장 단순선형회귀모형 (책 39–96)"
  - "김충락·강근석 『회귀분석』 2판 제3장 중선형회귀모형 (책 97–162)"
  - "Hogg 8판 §2.3 (조건부 기댓값 — LSE의 수학적 뿌리)"
moc: ["[[MOC_추정효율성]]"]
book_pages: "39-96 (Ch2), 97-162 (Ch3)"
tags: [회귀분석, 2장, 3장, LSE, 정규방정식, 최소제곱법, ClusterE, ClusterA, stub]
date_created: 2026-08-21
status: stub (진술만 — 백지유도 대상)
---

# 최소제곱추정량 (LSE)

> [!info] 📖 교재 위치 · 커리큘럼
> 스칼라형은 제2장(책 39–96), 행렬형은 제3장(책 97–162).
> **커리큘럼**: [[MOC_추정효율성]](Cluster A) 가지 ①②의 출발점이자 Cluster E(투영)의 뿌리.

> [!definition] 정의
> $S(\boldsymbol\beta)=\lVert\mathbf y-X\boldsymbol\beta\rVert^2$ 를 최소화하는 $\hat{\boldsymbol\beta}$. 1계 조건이 **정규방정식**
> $$X^\top X\hat{\boldsymbol\beta}=X^\top\mathbf y\;\Longrightarrow\;\hat{\boldsymbol\beta}=(X^\top X)^{-1}X^\top\mathbf y\quad(\operatorname{rank}X=p)$$

## 백지유도 대상

1. 스칼라형 $\hat\beta_1=S_{xy}/S_{xx}$, $\hat\beta_0=\bar y-\hat\beta_1\bar x$ 를 정규방정식에서.
2. 행렬형: $S(\boldsymbol\beta)$ 전개 → 미분 → 정규방정식. $X^\top X$ 가역성이 필요한 지점은 정확히 어디인가?
3. **기하 해석**: 정규방정식 $X^\top(\mathbf y-X\hat{\boldsymbol\beta})=X^\top\mathbf e=0$ = "잔차가 $\mathrm{col}(X)$ 와 직교" → [[Hat Matrix]] 로 인계.
4. 최소성이 **최소제곱**(목적함수)이지 **최소분산**(추정량의 분산)이 아님을 구분 → 후자는 [[Gauss-Markov 정리]].

> ⚠️ 4번은 `[[Aitken 정리]]` §4 에 "오늘 교정한 실수"로 이미 기록돼 있다. 같은 혼동을 반복하지 말 것.

## 이미 통과한 조각 (역참조)

| 조각 | 위치 |
|---|---|
| $\mathrm{Var}(\hat\beta_1)=\sigma^2/S_{xx}$, $\mathrm{Var}(\hat\beta_0)$ 유도 | `주차별/01주차_단순회귀LSE/08_정리노트.md` |
| $\hat\beta$ 가 확률변수이고 $\beta$ 는 모수라는 구분 | [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]] |
| $V\neq I$ 에서 LSE에 무슨 일이 생기나 (불편성 생존·분산 붕괴) | [[일반화최소제곱(GLS)]] §2 |
| 잔차 $\mathbf e=(I-H)\mathbf y$ 의 성질 | [[Ch04_잔차가정검정_백지유도]] §0 |

## 연결
- 다음: [[Hat Matrix]] · [[회귀계수의 불편성 증명]] · [[Gauss-Markov 정리]]
- 일반화: [[일반화최소제곱(GLS)]] ($V=I$ 특수경우가 LSE)
- 허브: [[MOC_추정효율성]]

> [!note] stub
> 씨앗 노트다. 1~4를 직접 유도해 채울 것.
