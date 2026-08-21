---
aliases: [양의 준정부호 순서, Löwner order, Loewner 순서, 행렬 순서, 행렬 부등식, PSD 순서]
subject: 선형대수
tags: [선형대수, 행렬, 양정치, PSD, 순서, 도구, stub]
moc: ["[[MOC_추정효율성]]"]
date_created: "2026-06-29"
date_modified: 2026-08-21
cluster: []
cluster_note: "도구 노트 — Cluster A(BLUE 정의)에서 호출"
chapter: "교재 외 선형대수 도구 (김충락 부록 A.5 이차형식·양정치)"
concept: "[[양의 준정부호 순서(Löwner order)]]"
cross_ref: ["[[Aitken 정리]] B단계 · [[Gauss-Markov 정리]] 의 '최소분산' 정의"]
---

# 양의 준정부호 순서 (Löwner order)

> [!info] 📖 위치 · 쓰임
> "추정량의 분산(공분산행렬)이 더 작다"의 정의. [[Aitken 정리]]·[[Gauss-Markov 정리]] 의 BLUE("최소분산")가 스칼라가 아니라 **행렬**이라 필요한 순서.

> [!definition] 정의
> 대칭행렬 $A,B$ 에 대해
> $$A\preceq B \iff B-A \text{ 가 양의 준정부호(PSD)}\iff \mathbf v'(B-A)\mathbf v\ge 0\ \ \forall\mathbf v.$$

## 왜 필요한가
공분산행렬 $\text{Var}(\hat{\boldsymbol\beta})$ 는 행렬이므로 "더 작다"가 자명하지 않다. Löwner 순서로 정의하면:
$$\text{Var}(\hat{\boldsymbol\beta}_{GLS})\preceq\text{Var}(\tilde{\boldsymbol\beta})\quad\forall\,\tilde{\boldsymbol\beta}\in\mathcal C$$
가 곧 BLUE 의 정확한 뜻.

## 유용한 귀결
- $A\preceq B \Rightarrow$ 모든 $\mathbf c$ 에 대해 $\mathbf c'A\mathbf c\le\mathbf c'B\mathbf c$ → **임의의 선형결합 $\mathbf c'\hat{\boldsymbol\beta}$ 의 (스칼라)분산도 최소**.
- 대각 성분 비교 → 개별 계수 $\hat\beta_j$ 의 분산도 최소.
- $A\preceq B \Rightarrow \operatorname{tr}(A)\le\operatorname{tr}(B),\ \det$ 단조 등.

## 연결
- [[Aitken 정리]] (B 단계: $\text{Var}(\tilde\beta)=\text{Var}(\hat\beta_{GLS})+\sigma^2 DVD'$, $DVD'\succeq0$)
- [[Gauss-Markov 정리]] · [[이차형식]]

> [!note] stub
> 씨앗 노트. PSD 동치조건(고윳값≥0, Cholesky 존재 등), 부분순서(전순서 아님) 성질 보강 여지.
