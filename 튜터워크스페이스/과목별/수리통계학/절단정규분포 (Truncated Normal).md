---
aliases: [절단정규분포, Truncated Normal, 절단정규, 역밀즈비, Inverse Mills Ratio, 반정규분포]
tags: [수리통계, 3장, 절단정규, 조건부기댓값, 역밀즈비, stub, ClusterB]
subject: 수리통계학
chapter: ["Hogg Ch3 특수분포"]
book_pages: "Hogg 8th §3.4"
moc: ["[[MOC_이차형식]]"]
cluster: [B]
date_created: 2026-08-22
status: stub
---

# 절단정규분포 (Truncated Normal)

> [!info] 📖 교재 위치 · 커리큘럼
> **본거지**: Hogg §3.4 주변. 조건부 기댓값을 정규분포에서 명시적으로 계산할 때 등장.
> **등장 맥락**: [[자기참조적 집단화와 F검정의 함정]] — 평균에서 자른 두 조각이 각각 절단정규.

## 핵심 공식 (하방 절단)

$X\sim N(\mu,\sigma^2)$, $\alpha=(a-\mu)/\sigma$ 일 때

$$
E[X\mid X>a]=\mu+\sigma\cdot\underbrace{\frac{\phi(\alpha)}{1-\Phi(\alpha)}}_{\text{역밀즈비}\ \lambda(\alpha)},
\qquad
\operatorname{Var}(X\mid X>a)=\sigma^2\big[1+\alpha\lambda(\alpha)-\lambda(\alpha)^2\big]
$$

## 평균에서 자른 특수경우 ($a=\mu$, $\alpha=0$)

$\phi(0)=1/\sqrt{2\pi}$, $\Phi(0)=1/2$ 이므로

$$
E[X\mid X>\mu]=\mu+\sigma\sqrt{\tfrac2\pi}\approx\mu+0.7979\,\sigma,\qquad
\operatorname{Var}(X\mid X>\mu)=\sigma^2\Big(1-\tfrac2\pi\Big)\approx0.3634\,\sigma^2
$$

> [!note] 유용한 부산물
> - 두 조각의 평균 간격: $2\sigma\sqrt{2/\pi}\approx1.596\,\sigma$
> - 두 조각의 분산은 **서로 같다** (대칭 절단) ⟹ [[등분산성(homoscedasticity)]]이 성립
> - 각 조각의 왜도 $\approx0.995$ ⟹ 비정규
> - 이분화가 만드는 $R^2=2/\pi\approx0.6366$

핵심 적분: $\phi'(z)=-z\phi(z)\ \Rightarrow\ \int_0^\infty z\phi(z)\,dz=[-\phi(z)]_0^\infty=\phi(0)$.

> [!todo] 미작성
> 양방향 절단, Tobit 모형, 절단 vs 중도절단(censoring) 구분.

## 연결
[[자기참조적 집단화와 F검정의 함정]] · [[표본분포 (Sampling Distribution)]] · [[등분산성(homoscedasticity)]] · [[MOC_이차형식]]
