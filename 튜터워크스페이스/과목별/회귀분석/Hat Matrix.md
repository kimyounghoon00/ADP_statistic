---
subject: 회귀분석
chapter: Ch3 중선형회귀모형 (모자행렬·적합값의 분포)
concept: "[[Hat Matrix]]"
aliases: [Hat Matrix, "Hat Matrix의 멱등성 및 대칭성", 모자행렬, 햇행렬, H 행렬, 투영행렬, projection matrix]
cluster: [B, E]
cross_ref:
  - "김충락·강근석 『회귀분석』 2판 제3장 중선형회귀모형 (책 97–162), §3.4.2 적합값의 분포"
  - "김충락·강근석 『회귀분석』 2판 §4.3 지렛값(레버리지)"
  - "Hogg 8판 §9.8–9.9 (멱등 이차형식의 분포)"
moc: ["[[MOC_이차형식]]"]
book_pages: "97-162 (Ch3), §4.3 지렛값 (Ch4)"
tags: [회귀분석, 3장, 4장, HatMatrix, 멱등, 투영, 레버리지, ClusterB, ClusterE, stub]
date_created: 2026-08-21
status: stub (진술만 — 백지유도 대상)
---

# Hat Matrix ($H$)

> [!info] 📖 교재 위치 · 커리큘럼
> 제3장 중선형회귀모형(책 97–162). 레버리지 $h_{ii}$ 는 §4.3 지렛값.
> **커리큘럼**: [[MOC_이차형식]](Cluster B) 가지 ② · Cluster E(투영·LSE)의 공유 노드. 이 볼트에서 **가장 많이 참조되는 개념**(15회)이다.

> [!definition] 정의
> $$H=X(X^\top X)^{-1}X^\top,\qquad \hat{\mathbf y}=H\mathbf y,\qquad \mathbf e=(I-H)\mathbf y$$
> $\mathbf y$ 를 $\mathrm{col}(X)$ 위로 내리는 **직교사영행렬**. "모자($\hat{}$)를 씌운다"에서 이름이 왔다.

## 백지유도 대상

1. **대칭** $H^\top=H$, **멱등** $H^2=H$ 를 정의에서 직접 확인. $(I-H)$ 도 같은 성질을 갖는가?
2. $\operatorname{tr}(H)=p$ 를 $\operatorname{tr}$ 순환성으로. 왜 이것이 곧 $\operatorname{rank}(H)=p$ (자유도)인가?
3. $HX=X$, $(I-H)X=0$ → $X^\top\mathbf e=0$ (정규방정식과 같은 말) → $\hat{\mathbf y}^\top\mathbf e=0$.
4. $h_{ii}=\mathbf x_i^\top(X^\top X)^{-1}\mathbf x_i$, $0\le h_{ii}\le 1$, $\sum_i h_{ii}=p$.

> ⭐ 4번의 "이중 붕괴"(단위벡터가 $X$ 에 흡수되는 구조)는 이미 [[Ch04_잔차가정검정_백지유도]] §0에서 통과했다. 그 결과를 여기로 옮겨 적으면 이 노트의 절반이 채워진다.

## 이 개념이 이미 쓰인 자리 (역참조)

| 쓰임 | 노트 |
|---|---|
| $\mathrm{Var}(\mathbf e)=\sigma^2(I-H)$ → 잔차는 비등분산·비독립 | [[Ch04_잔차가정검정_백지유도]] §0 |
| $\hat y^\top e=0$ vs $y^\top e=SSE$ → 진단그림 가로축 | [[잔차의 직교성과 진단 그림의 가로축]] |
| $d=\varepsilon^\top MAM\varepsilon/\varepsilon^\top M\varepsilon$ ($M=I-H$) | [[Durbin-Watson 검정]] §8 |
| 중첩 투영의 차 $P_{큰}-P_{작}$ 이 다시 멱등 | [[Type I·II·III 제곱합과 부분 F-검정]] |
| 편의항 $\boldsymbol\mu^\top(I-H)\boldsymbol\mu$ | [[누락변수 편의와 유의성 반전]] |

## 연결
- 뿌리: [[이차형식]] → [[이차형식과 Cochran 정리]]
- 이웃: [[최소제곱추정량(LSE)]] · [[Gauss-Markov 정리]]
- 허브: [[MOC_이차형식]] 가지 ②

> [!note] stub
> 씨앗 노트다. 위 4단계 중 4번은 이미 통과했으니 1~3을 직접 유도해 채울 것.
