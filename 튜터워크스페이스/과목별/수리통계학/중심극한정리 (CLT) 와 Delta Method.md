---
subject: 수리통계학
chapter: Hogg 8판 §5.3 (CLT) · §5.2.2 (Δ-method, Thm 5.2.9)
concept: "[[중심극한정리 (CLT) 와 Delta Method]]"
aliases: ["중심극한정리 (CLT) 와 Delta Method", "중심극한정리와 Delta Method", "중심극한정리 (CLT)", "중심극한정리(CLT)", CLT, 중심극한정리, "델타방법(Delta Method)", "델타방법 (Delta Method)", Delta Method, "CLT·Delta"]
cluster: [F]
cross_ref:
  - "Hogg 8판 §5.3 (CLT), §5.2.2 Thm 5.2.9 (Δ-method), Def 5.2.2 (Op)"
  - "[[점근 표기법 (Big-O, little-o, Op, op)]] §7.3 — Δ-method 유도가 이미 여기 있다"
moc: []
tags: [수리통계학, 5장, CLT, 델타방법, 점근이론, ClusterF, 공통도구, stub]
date_created: 2026-08-21
status: stub (진술만 — 유도 본체는 [[점근 표기법 (Big-O, little-o, Op, op)]] §7.3)
---

# 중심극한정리 (CLT) 와 Delta Method

> [!info] 📖 교재 위치 · 커리큘럼
> Hogg 8판 §5.3(CLT) · §5.2.2(Δ-method). **커리큘럼**: Cluster F(점근이론)의 뿌리.
> ⚠️ 이 개념은 그동안 **6가지 이름**으로 흩어져 있었다(2026-08-21 무결성 검토 F-02). 이 파일이 정규 노트이며 옛 표기는 `aliases` 로 흡수했다.

> [!theorem] 진술
> **CLT**: $X_1,\dots,X_n$ iid, $E X=\mu$, $\operatorname{Var}X=\sigma^2<\infty$ 이면
> $$\sqrt n(\bar X_n-\mu)\ \xrightarrow{d}\ N(0,\sigma^2).$$
> **Δ-method**: $g$ 가 $\mu$ 에서 미분가능하고 $g'(\mu)\ne0$ 이면
> $$\sqrt n\bigl(g(\bar X_n)-g(\mu)\bigr)\ \xrightarrow{d}\ N\!\bigl(0,\ \sigma^2[g'(\mu)]^2\bigr).$$

> [!important] 유도는 이미 통과했다
> Δ-method의 테일러+$o_p$ 유도와 손풀이 예제($g(x)=x^2$)는 **[[점근 표기법 (Big-O, little-o, Op, op)]] §7.3–7.4** 에 완결돼 있다. 이 노트는 그 결과를 CLT 쪽에서 부를 때 쓰는 정규 진입점이다.

## 백지유도 대상 (아직 남은 것)

1. CLT 자체의 증명(MGF/특성함수 수렴) — Hogg §5.3.
2. Lindeberg–Feller(비iid)로의 확장이 필요한 자리는 어디인가 (회귀의 $\hat\beta$ 점근정규성).
3. **CLT가 통하지 않는 예외**: 단위근 검정의 Dickey–Fuller 분포 → 커리큘럼 Cluster F 학습순서 5번.
4. 다변량 Δ-method: $\sqrt n(g(\bar{\mathbf X})-g(\boldsymbol\mu))\xrightarrow{d}N(0,\nabla g^\top\Sigma\nabla g)$.

## 연결
- 도구: [[점근 표기법 (Big-O, little-o, Op, op)]] (본체) · [[코시-슈바르츠 부등식]]
- 쓰임: [[Durbin-Watson 검정]]·[[Breusch-Pagan 검정]]·[[Breusch-Godfrey 검정]] 의 점근 $\chi^2$ 근거, [[Ch14_반복측정ANOVA_구형성_정리노트]] 의 F검정 강건성 논의

> [!note] stub
> 씨앗 노트다. 위 1~4가 남은 과제다.
