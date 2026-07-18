---
aliases: [Cp 통계량, Mallows' Cp]
tags: [회귀분석, 5장, 모형선택, 예측오차, stub]
chapter: ["제5장 회귀모형의 선택"]
book_pages: "201-215 (Fig 5.5 p.215)"
moc: ["[[MOC_추정효율성]]"]
---

# Mallows Cp

> [!info] 📖 교재 위치 · 커리큘럼
> 김충락 제5장 회귀모형의 선택 §5.1–5.2 (책 201–215쪽). 커리큘럼: [[MOC_추정효율성]] 가지 ④ (편의-분산).

> [!definition] 정의
> 총 MSE 척도 $\Gamma_p = p + \dfrac{\boldsymbol\mu^\top(I-H)\boldsymbol\mu}{\sigma^2}$ 의 추정량
> $$C_p = \frac{SSE_p}{s^2} - (n-2p)$$
> ($s^2$ 은 최대모형 하의 $\hat\sigma^2$). 좋은 모형이면 $C_p \approx p$.

## 핵심 구조

- $\Gamma_p$ = 분산항 $p$ + **편의항** $\boldsymbol\mu^\top(I-H)\boldsymbol\mu/\sigma^2$ — 중요 변수 누락 시 편의항이 커진다 → [[누락변수 편의와 유의성 반전]].
- $C_p$ = 적합도($SSE_p/s^2$, 변수 늘수록 감소) + 벌점($2p-n$, 변수 늘수록 증가) — 벌점화 기준(penalized criterion).
- 최대모형에서는 $C_p = p$ 가 항등적으로 성립.

## 관련 노트
- [[누락변수 편의와 유의성 반전]] — 편의항의 기원
- [[다중공선성]] — 과대적합 쪽의 분산 문제

> [!note] stub
> 씨앗(stub)입니다. $E(SSE_p)$ 유도, $C_p$–AIC 관계, PRESS와의 비교를 채워 넣으세요.
