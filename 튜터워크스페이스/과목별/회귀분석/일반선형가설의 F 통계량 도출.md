---
subject: 회귀분석
chapter: Ch5 회귀모형의 선택 (일반선형가설)
concept: "[[일반선형가설의 F 통계량 도출]]"
cluster: [A, B]
cross_ref:
  - "김충락 회귀분석 Ch5 (book p.201–230 / PDF p.217–246) — 일반선형가설, 부분 F검정"
  - "Hogg 8판 §9.8–9.9 (이차형식 분포·Cochran)"
related:
  - "[[Type I·II·III 제곱합과 부분 F-검정]]"
  - "[[부분 F-검정과 전체 F-검정의 관계]]"
  - "[[이차형식의 분포와 독립성 (Cochran 정리)]]"
tags: [일반선형가설, 부분F검정, F통계량, ClusterA, ClusterB, 회귀분석, stub]
date_created: 2026-06-15
status: stub (골격만 — 백지유도 대상. 30분 규칙 적용)
aliases: ["일반선형가설의 F 통계량 도출", 일반선형가설, "부분 F-검정과 전체 F-검정의 관계", "H0: Abeta=c"]
date_modified: 2026-08-21
---

# [[일반선형가설의 F 통계량 도출]]  ·  *stub*

> **이 노트의 역할**: 백지유도 대상. 아래 골격을 보고 *스스로* 빈칸을 채운 뒤, 막히면 튜터와 대화한다. 답은 여기 적혀 있지 않다 (프로젝트 헌법 §1, 30분 규칙).

## 🎯 목표 (유도할 최종 결과)

선형모형 $\mathbf{Y}=X\beta+\boldsymbol\varepsilon,\ \boldsymbol\varepsilon\sim N(\mathbf0,\sigma^2 I)$ 에서, 일반선형가설

$$
H_0:\ A\beta = c \qquad (A:\ q\times p,\ \text{rank } q)
$$

에 대한 검정통계량이

$$
F=\frac{(A\hat\beta-c)^\top\,[A(X^\top X)^{-1}A^\top]^{-1}\,(A\hat\beta-c)\,/\,q}{\hat\sigma^2}\ \sim\ F_{q,\,n-p}\quad(H_0\text{ 하)}
$$

이고, 이것이 **부분 F (제약/완전 모형 비교)** 와 동일함을 보인다.

## 🧩 유도 골격 (각 단계는 스스로 채울 것)

1. **추정량의 분포**: $\hat\beta=(X^\top X)^{-1}X^\top\mathbf Y$ 의 분포는? → $A\hat\beta-c$ 의 평균·공분산은?
   - (힌트 위치) 어떤 가정이 정규성을 주는가?
2. **분자의 이차형식화**: $A\hat\beta-c$ 를 표준화하면 어떤 이차형식이 $\chi^2_q$ 가 되는가?
   - 연결: `[[이차형식의 분포와 독립성 (Cochran 정리)]]` — 멱등·대칭 조건.
3. **분모의 분포**: $(n-p)\hat\sigma^2/\sigma^2 \sim \chi^2_{n-p}$ 는 왜인가?
4. **분자·분모의 독립성**: 무엇이 독립을 보장하는가? (Cochran / 직교분해)
5. **F의 정의로 결합**: 두 독립 $\chi^2$의 비 → $F_{q,\,n-p}$.
6. **부분 F와의 동치**: 제약최소제곱 $SSE_{H_0}-SSE \ \overset{?}{=}\ (A\hat\beta-c)^\top[\dots]^{-1}(A\hat\beta-c)$ 보이기.

## 🔗 연결 개념 (클러스터 참조)

- **Cluster A (추정효율성·일반선형가설)**: 이 노트가 허브. → `[[부분 F-검정과 전체 F-검정의 관계]]`
- **Cluster B (이차형식)**: 분자·분모가 모두 이차형식 → `[[F-검정]]`, `[[이차형식의 분포와 독립성 (Cochran 정리)]]`, `[[MOC_이차형식]]`
- **적용/응용**: `[[Type I·II·III 제곱합과 부분 F-검정]]` — Type I·II·III·전체 F·계수 t검정이 전부 이 $H_0:A\beta=c$의 특수형.
  - 예: 변수 하나 제거(Type III, $q=1$) → $A$ 는 그 계수 자리만 1인 행벡터.
  - 예: 전체 F → $A=[\,\mathbf0\ \vert\ I_k\,]$ (절편 제외 전 기울기).

## 📌 막혔던 포인트 (학습 후 기록)

-

## 📚 참고 교재 페이지

- 김충락 회귀분석 Ch5 (book p.201–230 / PDF p.217–246).
- Hogg 8판 §9.8–9.9.
