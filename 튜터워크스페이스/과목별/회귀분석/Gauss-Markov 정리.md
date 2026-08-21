---
subject: 회귀분석
chapter: "Ch2 p.55 (BLUE 진술) / Ch3 중선형회귀모형 (행렬형) — ⚠️ 확인 필요"
concept: "[[Gauss-Markov 정리]]"
aliases: [가우스-마코프 정리, Gauss-Markov theorem, BLUE, 가우스마코프]
cluster: [A]
cross_ref:
  - "김충락·강근석 『회귀분석』 2판 — Ch2 p.55 (2026-06-29 색인 대조) / 제3장 97–162 (행렬형)"
  - "[[Aitken 정리]] (V≠I 로의 일반화)"
  - "Hogg 8판 §6.2 (CRLB — 제한 없는 불편추정량의 하한) → [[크라메르-라오 하한 (CRLB)]]"
book_pages: "55 (Ch2) / 97-162 (Ch3) — 아래 ⚠️ 참조"
moc: ["[[MOC_추정효율성]]"]
tags: [회귀분석, 2장, 3장, 추정, 정리, BLUE, ClusterA, stub]
date_created: 2026-06-29
status: stub (진술만 — BLUE 증명은 백지유도 대상)
date_modified: 2026-08-21
---

# Gauss-Markov 정리

> [!info] 📖 교재 위치 · 커리큘럼
> 커리큘럼: [[MOC_추정효율성]] 가지 ② 최소분산·효율성. 5·7장에서도 호출됨.

> [!warning] ⚠️ 교재 위치가 두 갈래로 기록돼 있다 — 다음 세션에 한 줄로 확정할 것
> | 주장 | 출처 |
> |---|---|
> | **Ch2, 책 55쪽** | 2026-06-29 PDF 색인 대조 세션 — [[Aitken 정리]], [[일반화최소제곱(GLS)]], [[_세션핸드오프_2026-06-29_Aitken_B완결]], 대시보드 세션로그 |
> | **제3장 97–162쪽** | 이 노트의 기존 frontmatter (근거 미기록) |
> | **김충락 Ch3** | [[01_Concept_Connection_Curriculum]] Cluster A, [[00_Hub_Orchestrator_Brief]] 챕터표 |
>
> 단순회귀판(Ch2)과 행렬형(Ch3)이 **둘 다 있을 가능성이 높다.** 교재를 펴서 "Ch2 p.55 = 스칼라 진술 / Ch3 §__ = 행렬형 증명"인지 확인한 뒤, 이 박스를 확정 문장으로 바꾸고 커리큘럼·허브 챕터표도 함께 고칠 것. (2026-08-21 무결성 검토 F-05b)

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
