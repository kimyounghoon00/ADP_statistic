---
aliases: [내생성, Endogeneity, 내생변수, 외생성, Exogeneity]
tags: [회귀분석, 3장, 내생성, 편의, 식별, stub, ClusterB]
subject: 회귀분석
chapter: ["김충락 Ch3 §3.1 고정설계"]
book_pages: "김충락 Ch3 p97–162"
moc: ["[[MOC_이차형식]]"]
cluster: [B]
date_created: 2026-08-22
status: stub
---

# 내생성 (Endogeneity)

> [!info] 📖 교재 위치 · 커리큘럼
> **본거지**: 김충락 §3.1 고정설계 가정의 **위배 형태**. 교재는 $X$ 비확률적을 가정하므로 내생성은 교재 외 확장 주제.
> **커리큘럼 연결**: [[MOC_이차형식]] (Cluster B) 가지 ⑥.

## 정의

설명변수가 오차항과 상관될 때 ($\operatorname{Cov}(X_j,\varepsilon)\ne 0$) 그 변수를 **내생적**이라 한다. 이때 OLS는 **불편성도 일치성도 잃는다**.

$$
\hat\beta \xrightarrow{p} \beta + \big(E[X^\top X]\big)^{-1}E[X^\top\varepsilon]
$$

## 발생 경로

| 경로 | 설명 | 노트 |
|---|---|---|
| **역인과** | $Y$ 가 $X$ 를 결정 | [[자기참조적 집단화와 F검정의 함정]] (극단 사례: $g=\mathbf 1\{\varepsilon>0\}$) |
| **누락변수** | 생략된 교란변수가 양쪽에 작용 | [[누락변수 편의와 유의성 반전]] |
| **측정오차** | $X$ 가 잡음과 함께 관측됨 | — |
| **표본선택** | 표본 포함 여부가 $Y$ 에 의존 | — |

> [!todo] 미작성
> 도구변수(IV)·2SLS·Hausman 검정. 다음 세션 후보.

## 연결
[[자기참조적 집단화와 F검정의 함정]] · [[무작위화 (Randomization)]] · [[누락변수 편의와 유의성 반전]] · [[Ch03_선형모형의 확률구조 — 고정설계·모수와 추정량·σ²I]] · [[MOC_이차형식]]
