---
aliases: [가우스-마코프 정리, Gauss-Markov theorem, BLUE]
tags: [회귀분석, 3장, 추정, 정리, stub]
chapter: ["제3장 중선형회귀모형"]
book_pages: "97-162"
moc: ["[[MOC_추정효율성]]"]
---

# Gauss-Markov 정리

> [!info] 📖 교재 위치 · 커리큘럼
> 제3장 중선형회귀모형 (책 97–162쪽). 5·7장에서도 호출됨. 커리큘럼: [[MOC_추정효율성]] 가지 ② 최소분산·효율성.

> [!theorem] 진술 (개요)
> 선형모형 $\mathbf{y}=X\beta+\varepsilon$ 에서 $X$ 가 고정(비확률)이고 $E(\varepsilon)=\mathbf 0$, $\text{Cov}(\varepsilon)=\sigma^2 I$ 일 때, 최소제곱추정량 $\hat{\beta}=(X^\top X)^{-1}X^\top\mathbf{y}$ 는 **BLUE**(Best Linear Unbiased Estimator) — 모든 선형 불편추정량 중 분산이 최소이다.

## 전제 가정 (가우스-마코프 가정)

1. 선형성: $E(\mathbf{y})=X\beta$
2. $X$ 의 비확률성(고정 설계) 및 $\text{rank}(X)=p$ (완전계수)
3. 등분산성 + 무상관: $\text{Cov}(\varepsilon)=\sigma^2 I$ → [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]] 참고
4. (정규성은 **필요 없음** — 검정·구간추정에서만 추가로 요구)

## 핵심 결과

$$
E(\hat{\beta})=\beta \quad(\text{불편성}), \qquad
\text{Cov}(\hat{\beta})=\sigma^2 (X^\top X)^{-1}
$$

$X$ 가 고정이므로 $(X^\top X)^{-1}X^\top$ 를 상수 행렬로 밖에 꺼낼 수 있다는 점이 유도의 핵심.

## 관련 노트
- [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]]
- [[일반화최소제곱(GLS)]]
- [[다중공선성]]

> [!note] stub
> 씨앗(stub)입니다. BLUE 증명(임의의 선형 불편추정량 $C\mathbf y$ 와의 분산 비교), 등분산 가정이 깨질 때 GLS로의 확장 등을 채워 넣으세요.
