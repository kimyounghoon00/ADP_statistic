---
subject: 수리통계학
chapter: Hogg 8판 §6.2 (Rao–Cramér 하한과 효율성)
concept: "[[크라메르-라오 하한 (CRLB)]]"
aliases: ["크라메르-라오 하한 (CRLB)", 크라메르-라오 하한, CRLB, "Fisher 정보량과 Cramér-Rao 하한", "Fisher 정보량과 Cramér-Rao 하한 (CRLB)", "Fisher 정보량과 Rao–Cramér 하한 (CRLB)", Cramer-Rao, 라오-크라메르 하한, Fisher 정보량]
cluster: [A]
cross_ref:
  - "Hogg, McKean & Craig 8판 §6.2 (Rao–Cramér Lower Bound and Efficiency)"
  - "[[Gauss-Markov 정리]] (선형·불편으로 제한했을 때의 대응물)"
  - "[[MOC_추정효율성]] 가지 ② 최소분산·효율성"
moc: ["[[MOC_추정효율성]]"]
tags: [수리통계학, 6장, CRLB, Fisher정보량, 효율성, MLE, ClusterA, stub]
date_created: 2026-08-21
status: stub (진술만 — 백지유도 대상)
---

# 크라메르-라오 하한 (CRLB)

> [!info] 📖 교재 위치 · 커리큘럼
> Hogg 8판 **§6.2**. **커리큘럼**: [[MOC_추정효율성]](Cluster A) 가지 ② — 커리큘럼 Cluster A 사슬의 **첫 고리**이자 [[Gauss-Markov 정리]]의 짝.

> [!theorem] 진술 (요지)
> 정칙조건(regularity) 하에서 $\theta$ 의 임의의 불편추정량 $\hat\theta$ 에 대해
> $$\operatorname{Var}(\hat\theta)\;\ge\;\frac{1}{n\,I(\theta)},\qquad I(\theta)=E\!\left[\Bigl(\frac{\partial}{\partial\theta}\log f(X;\theta)\Bigr)^{2}\right]=-E\!\left[\frac{\partial^2}{\partial\theta^2}\log f(X;\theta)\right]$$
> 등호를 달성하면 **효율추정량(efficient estimator)**.

## 백지유도 대상

1. Cauchy–Schwarz로 하한 유도 — 어디에 쓰이는지 이미 안다 → [[코시-슈바르츠 부등식]] Level 3.
2. 정보량의 두 표현($E[(\partial_\theta\ell)^2]=-E[\partial^2_\theta\ell]$)이 같은 이유. 어떤 정칙조건이 필요한가?
3. **정칙조건이 깨지는 예**(지지집합이 $\theta$ 에 의존: $U(0,\theta)$) — 왜 하한이 무너지는가.
4. 다모수 확장: Fisher 정보**행렬**과 $\operatorname{Var}(\hat{\boldsymbol\theta})\succeq I(\boldsymbol\theta)^{-1}$ → 행렬 부등식의 뜻은 [[양의 준정부호 순서(Löwner order)]].
5. **핵심 대비**: CRLB는 *모든* 불편추정량의 하한(분포 가정 필요), [[Gauss-Markov 정리]]는 *선형* 불편추정량 중 최적(정규성 불필요). 정규오차에서 LSE = MLE = UMVUE 가 일치하는 이유는?

## 연결
- 짝: [[Gauss-Markov 정리]] · [[Aitken 정리]] (`[[Aitken 정리]]` 열린 질문 Q2가 정확히 이 노트를 부르고 있다)
- 도구: [[코시-슈바르츠 부등식]] · [[양의 준정부호 순서(Löwner order)]]
- 허브: [[MOC_추정효율성]] 가지 ②

> [!note] stub
> 씨앗 노트다. 1~5를 직접 채울 것.
