---
subject: 수리통계학 (정규선형모형 — 여러 과목 공통 도구)
chapter: Hogg 8판 §9.8–9.9 (이차형식의 분포와 독립성)
concept: "[[이차형식과 Cochran 정리]]"
aliases: ["이차형식과 Cochran 정리", "Cochran 정리", "이차형식의 분포와 독립성 (Cochran 정리)", "이차형식의 분포와 독립성 (Cochran 정리) — Hogg §9.8–9.9", "이차형식과 Cochran 정리 — 회귀분석 맥락", "이차형식의 독립성", Cochran theorem, 코크란 정리]
cluster: [B]
cross_ref:
  - "Hogg, McKean & Craig 8판 §9.8–9.9 (이차형식의 분포·독립성)"
  - "김충락·강근석 『회귀분석』 2판 §3.4 (제곱합의 이차형식) → [[이차형식]]"
  - "Montgomery 8판 §3 (일원 ANOVA SS 분해)"
moc: ["[[MOC_이차형식]]"]
tags: [수리통계학, 9장, 이차형식, Cochran, 카이제곱, 독립성, ANOVA, ClusterB, 공통도구, stub]
date_created: 2026-08-21
status: stub (진술만 — 백지유도 대상)
note_분류근거: "회귀분석 고유 개념이 아니라 정규선형모형 공통 정리(Hogg §9.8–9.9). 회귀·실험설계·다변량이 함께 쓰므로 수리통계학에 둔다 — [[점근 표기법 (Big-O, little-o, Op, op)]] 와 같은 원칙."
---

# 이차형식과 Cochran 정리

> [!info] 📖 교재 위치 · 커리큘럼
> **본거지**: Hogg 8판 §9.8–9.9. 회귀 쪽 대응 절은 김충락 §3.4(책 114–119).
> **커리큘럼**: [[MOC_이차형식]](Cluster B) 가지 ① — "왜 SS가 $\chi^2$ 이고 왜 F검정이 성립하는가"의 심장.
> ⚠️ 이 개념은 그동안 **6가지 이름**으로 흩어져 있었다(2026-08-21 무결성 검토 F-02). 이 파일이 정규 노트이며 옛 표기는 전부 `aliases` 로 흡수했다.

> [!theorem] 진술 (요지)
> $\mathbf Z\sim N_n(\mathbf 0,\sigma^2 I)$ 이고 $A$ 가 대칭일 때
> $$\frac{\mathbf Z^\top A\mathbf Z}{\sigma^2}\sim\chi^2_{r}\iff A\ \text{멱등},\quad r=\operatorname{rank}(A)=\operatorname{tr}(A)$$
> 두 이차형식 $\mathbf Z^\top A\mathbf Z$, $\mathbf Z^\top B\mathbf Z$ 의 **독립** 조건은 $AB=0$.
> **Cochran**: $\sum_{i=1}^k A_i=I$ 이고 $\sum_i\operatorname{rank}(A_i)=n$ 이면, 각 $\mathbf Z^\top A_i\mathbf Z/\sigma^2$ 는 **서로 독립인** $\chi^2_{\operatorname{rank}(A_i)}$.

## 백지유도 대상

1. 스펙트럼 분해로 멱등 $\Rightarrow$ 고윳값이 0/1뿐 $\Rightarrow$ $\chi^2$ 임을 보이기.
2. 왜 $\operatorname{rank}=\operatorname{tr}$ 인가 (멱등행렬 한정).
3. $AB=0$ 이 왜 독립을 주는가 (동시 대각화).
4. 회귀 적용: $SSE/\sigma^2=\mathbf y^\top(I-H)\mathbf y/\sigma^2\sim\chi^2_{n-p}$, 그리고 $SSR\perp SSE$ → $F$ 검정 성립.
5. 비중심(noncentral) 확장: $\boldsymbol\mu\ne\mathbf 0$ 이면 비중심모수 $\lambda=\boldsymbol\mu^\top A\boldsymbol\mu/\sigma^2$ → 검정력 계산의 토대.

## 이 정리가 이미 호출된 자리 (역참조)

| 쓰임 | 노트 |
|---|---|
| $SSE/\sigma^2\sim\chi^2_{n-p}$ | [[Ch04_잔차가정검정_백지유도]] · [[Durbin-Watson 검정]] §8 |
| Type I·II·III SS의 $\chi^2$·독립성 | [[Type I·II·III 제곱합과 부분 F-검정]] · [[Type II 제곱합 (정식화)]] §5 |
| 반복측정 잔차 자유도 $(n-1)(k-1)$ | [[Ch14_반복측정ANOVA_구형성_정리노트]] |
| DW가 **왜 $F$ 가 아닌가**(멱등 아님 + 비독립) | [[Durbin-Watson 검정]] §8 (3) |
| 일반선형가설 F의 분자·분모 | [[일반선형가설의 F 통계량 도출]] |

## 연결
- 뿌리: [[이차형식]] · [[Hat Matrix]]
- 다음: [[일반선형가설의 F 통계량 도출]]
- 허브: [[MOC_이차형식]] 가지 ①

> [!note] stub
> 씨앗 노트다. 1~5를 직접 유도해 채울 것 — 답을 여기 적어두지 않았다.
