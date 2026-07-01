---
aliases: [Aitken 정리, Aitken theorem, 에이트킨 정리, GLS BLUE, 일반화 가우스-마코프, 일반화 Gauss-Markov]
subject: 회귀분석
chapter: "교재 외(고전 결과) — 교재상 관련 절은 §6.3 가중최소제곱법(WLS, 제6장 변환)"
book_pages: "교재 미수록(Aitken·일반 GLS). 관련: WLS p253-254, Gauss-Markov p55"
concept: '[[Aitken 정리]]'
cluster: [추정법, 효율성, BLUE]
tags: [회귀분석, GLS, BLUE, Aitken, 효율성, 일반화최소제곱, 진행중]
moc: ["[[MOC_추정효율성]]"]
status: "완료 — L·U·B 전부 통과, GLS=BLUE(유일성까지) 증명 완결 (2026-06-29)"
date_created: "2026-06-29"
date_modified: "2026-06-29"
---

# Aitken 정리 — GLS가 BLUE임을 보이는 정리

> [!info] 📖 교재 위치 · 커리큘럼 (2026-06-29 PDF 대조 수정)
> **교재 수록 여부**: 김충락·강근석 『회귀분석』 2판에는 **Aitken 정리·일반 GLS가 수록돼 있지 않다.** (색인 대조: "generalized least squares"·"Aitken" 항목 없음. Ch3 중선형회귀모형은 전 구간 $\text{Cov}(\boldsymbol\varepsilon)=\sigma^2 I$ 가정.) 본 노트는 **교재를 넘어선 고전 결과**.
> **교재상 가장 가까운 본문**: §6.3 **가중최소제곱법(WLS)** — 책 253–254쪽(제6장 선형회귀모형의 변환). WLS는 본 정리의 **대각 특수경우**($V$ 대각). 앞 이분산성(heteroscedasticity) p252, 뒤 박스-칵스 §6.4. → [[가중최소제곱(WLS)]]
> **위치**: [[Gauss-Markov 정리]](교재 Ch2, 책 55쪽)가 $\text{Cov}(\boldsymbol\varepsilon)=\sigma^2 I$ 에서 LSE=BLUE 라면, **Aitken 정리는 그 일반화** — $\text{Cov}(\boldsymbol\varepsilon)=\sigma^2 V$ ($V\neq I$) 에서 GLS=BLUE.
> **커리큘럼**: [[MOC_추정효율성]] (Cluster A) 가지 ② 최소분산·효율성. 직전 흐름 [[일반화최소제곱(GLS)]] → 본 노트(효율성 증명).

> [!theorem] 명제 (Aitken)
> 선형모형 $\mathbf y=X\boldsymbol\beta+\boldsymbol\varepsilon$ 에서 $X$ 고정·완전계수, $E[\boldsymbol\varepsilon]=\mathbf 0$, $\text{Cov}(\boldsymbol\varepsilon)=\sigma^2 V$ ($V$ 대칭 양정치)일 때,
> $$\hat{\boldsymbol\beta}_{GLS}=(X'V^{-1}X)^{-1}X'V^{-1}\mathbf y$$
> 는 **BLUE** — 모든 *선형 불편* 추정량 중 분산(공분산행렬)이 최소이다. $V=I$ 면 [[Gauss-Markov 정리]]로 환원.

---

## 진행 상태 (2026-06-29)

증명은 약자 **B·L·U·E** 를 글자별 조건으로 쪼개 진행한다.

| 글자 | 조건 | 상태 |
|---|---|---|
| **L** (Linear) | $\hat{\boldsymbol\beta}=C\mathbf y$ 꼴인가 | ✅ 통과 (구성상) |
| **U** (Unbiased) | $E[\hat{\boldsymbol\beta}]=\boldsymbol\beta$, 즉 $CX=I_p$ | ✅ 통과 |
| **B** (Best) | $\mathcal C$ 안 모든 경쟁자보다 분산 최소 | ✅ 통과 (유일성까지) |
| ~~E~~ (Estimator) | (조건 아님 — 단순 명칭) | — |

---

## 1. L — 선형성 (Linear)

$\hat{\boldsymbol\beta}_{GLS}=\underbrace{(X'V^{-1}X)^{-1}X'V^{-1}}_{=:\,C_{GLS}}\,\mathbf y = C_{GLS}\,\mathbf y.$

$C_{GLS}$ 는 상수행렬이므로 GLS 추정량은 $\mathbf y$ 의 **선형결합** — 구성상 자명히 선형. $\square$

---

## 2. U — 불편성 (Unbiased) 과 경쟁자 집합

**임의의 선형추정량** $\tilde{\boldsymbol\beta}=C\mathbf y$ ($C$ 는 $p\times n$ 상수행렬)에 곧장 기댓값을 취한다 *(주의: $\hat\beta$ 를 $\mathbf y$ 에 다시 대입하지 말 것 — 식이 꼬인다)*:

$$E[\tilde{\boldsymbol\beta}]=E[C\mathbf y]=C\,E[\mathbf y]=C(X\boldsymbol\beta)=(CX)\boldsymbol\beta.$$

*모든* $\boldsymbol\beta$ 에 대해 $(CX)\boldsymbol\beta=\boldsymbol\beta$ 이려면:

$$\boxed{\,CX=I_p\,}\quad(\text{불편성 조건}).$$

따라서 공정한 비교 대상 = **선형 불편 추정량 집합**:

$$\mathcal C=\{\,\tilde{\boldsymbol\beta}=C\mathbf y \;:\; CX=I_p\,\}.$$

**후보의 소속 확인**: $C_{GLS}X=(X'V^{-1}X)^{-1}\underbrace{X'V^{-1}X}_{}=I_p$ ✅ → $\hat{\boldsymbol\beta}_{GLS}\in\mathcal C$.

> [!warning] $CX=I$ 이지 $XC=I$ 가 아니다 (오늘 교정한 실수)
> $C$ 는 $p\times n$, $X$ 는 $n\times p$.
> - $CX$ 는 $p\times p$ → $I_p$ 가능 (가역일 수 있음).
> - $XC$ 는 $n\times n$ 인데 $\operatorname{rank}(XC)\le \operatorname{rank}(X)\le p<n$ → **항상 특이(singular)** → 가역행렬 $I_n$ 이 될 수 없음.
>
> 직관: $XC$ 의 각 열은 "$X\times$무언가" = **$X$ 열들의 조합**이라 폭 $p$ 의 좁은 통로에 갇힌다. 미니예제 $X=\binom11,\,C=(a\ b)$: $XC=\begin{psmallmatrix}a&b\\a&b\end{psmallmatrix}$ (두 행 동일, rank 1, $\ne I_2$) vs $CX=a+b$ ($=1$ 가능). → [[행렬 곱의 계수 부등식]]

---

## 3. B — 최소분산 (Best) ✅ 완결

> [!goal] 보일 것
> $\text{Var}(\tilde{\boldsymbol\beta})\succeq\text{Var}(\hat{\boldsymbol\beta}_{GLS})$ ([[양의 준정부호 순서(Löwner order)]]) — 즉 차이 $\text{Var}(\tilde{\boldsymbol\beta})-\text{Var}(\hat{\boldsymbol\beta}_{GLS})$ 가 PSD.

### 출발: 두 분산

$\text{Var}(\mathbf y)=\text{Cov}(X\boldsymbol\beta+\boldsymbol\varepsilon)=\sigma^2 V$ 이므로, 임의 경쟁자 $\tilde{\boldsymbol\beta}=C\mathbf y\in\mathcal C$ 와 후보:
$$\text{Var}(\tilde{\boldsymbol\beta})=\sigma^2\,CVC',\qquad \text{Var}(\hat{\boldsymbol\beta}_{GLS})=\sigma^2(X'V^{-1}X)^{-1}.$$

### ① 분해 — 아는 점 $C_{GLS}$ 를 기준으로

임의의 $C$ 는 막막하지만, 우리가 완전히 아는 경쟁자 $C_{GLS}$ 에서 *얼마나 벗어났는지* 로 적는다:
$$C=C_{GLS}+D,\qquad D:=C-C_{GLS}\ (p\times n).$$

### ② 불편성 → $DX=0$ (마스터키)

$C,\,C_{GLS}$ 둘 다 $\mathcal C$ 의 원소 ($CX=I_p,\ C_{GLS}X=I_p$):
$$(C_{GLS}+D)X=I_p\ \Rightarrow\ I_p+DX=I_p\ \Rightarrow\ \boxed{DX=0}.$$

### ③ 전개 + 교차항 소거

$$\text{Var}(\tilde{\boldsymbol\beta})=\sigma^2(C_{GLS}+D)V(C_{GLS}+D)'=\sigma^2\big[\underbrace{C_{GLS}VC_{GLS}'+DVD'}_{\text{순수}}+\underbrace{C_{GLS}VD'+DVC_{GLS}'}_{\text{교차}}\big].$$

핵심 계산 $C_{GLS}V=(X'V^{-1}X)^{-1}X'V^{-1}\,V=(X'V^{-1}X)^{-1}X'$ ($V^{-1}V=I$ 로 소거) 이므로
$$C_{GLS}VD'=(X'V^{-1}X)^{-1}\,X'D'=(X'V^{-1}X)^{-1}(DX)'=0.$$
나머지 교차항 $DVC_{GLS}'$ 은 그 전치 ($V$ 대칭)라 **동시에 0** → 교차항 증발.

### ④ 첫 항의 정체 = $\text{Var}(\hat{\boldsymbol\beta}_{GLS})$

$X'C_{GLS}'=(C_{GLS}X)'=I_p$ 이므로
$$\sigma^2 C_{GLS}VC_{GLS}'=\sigma^2(X'V^{-1}X)^{-1}\,X'C_{GLS}'=\sigma^2(X'V^{-1}X)^{-1}=\text{Var}(\hat{\boldsymbol\beta}_{GLS}).$$

### ⑤ 결론 — 분해 항등식 + PSD

$$\boxed{\ \text{Var}(\tilde{\boldsymbol\beta})=\text{Var}(\hat{\boldsymbol\beta}_{GLS})+\sigma^2\,DVD'\ }$$

$V$ 양정치 → 임의 $\mathbf v$ 에 대해 $\mathbf v'(DVD')\mathbf v=(D'\mathbf v)'V(D'\mathbf v)=\mathbf w'V\mathbf w\ge 0$ ($\mathbf w:=D'\mathbf v$). 즉 $\sigma^2 DVD'\succeq 0$, 따라서
$$\text{Var}(\tilde{\boldsymbol\beta})\succeq\text{Var}(\hat{\boldsymbol\beta}_{GLS})\qquad\forall\,\tilde{\boldsymbol\beta}\in\mathcal C.$$

### ⑥ 유일성 (등호 조건)

$V$ 양정치라 $\mathbf w'V\mathbf w=0\iff\mathbf w=0$. 등호가 *모든* $\mathbf v$ 에서 성립 $\iff D'\mathbf v=0\ \forall\mathbf v\iff D=0\iff C=C_{GLS}$.
→ **$\hat{\boldsymbol\beta}_{GLS}$ 가 유일한 BLUE.** $\blacksquare$

> [!note] 직관
> $\sigma^2 DVD'$ 는 "GLS에서 벗어난 대가(penalty)" — 항상 $\succeq 0$ 이라, GLS를 떠나는 순간 분산은 늘 수밖에 없다. $V=I$ 면 $C_{GLS}=(X'X)^{-1}X'$ 로 [[Gauss-Markov 정리]] 환원.

---

## 4. 오늘 교정한 실수 (다음에 또 헷갈릴 곳)

1. **`E`(Estimator)를 증명할 조건으로 착각** ❌ → 실질 조건은 **L·U·B 셋**뿐. E는 명칭.
2. **`XC=I` 로 씀** ❌ → 차원·계수 검산으로 **`CX=I`** 가 정답. ([[행렬 곱의 계수 부등식]])
3. **$\hat\beta=C\mathbf y$ 를 다시 $\mathbf y$ 에 대입** ❌ → 그냥 $\tilde{\boldsymbol\beta}=C\mathbf y$ 에 곧장 $E[\cdot]$.
4. **"Best=최소제곱이 최소"로 혼동** ❌ → 최소화 대상은 *추정량의 분산* $\text{Var}(\hat\beta)$(공분산행렬), '최소제곱'은 추정 *방법*의 이름.

---

## 5. 연결 (Links)

- 직전 흐름: [[일반화최소제곱(GLS)]] (표백변환·공식 유도) → 본 노트(효율성 증명)
- 뿌리·특수경우: [[Gauss-Markov 정리]] ($V=I$ → LSE=BLUE)
- 도구: [[행렬 곱의 계수 부등식]] · [[양의 준정부호 순서(Löwner order)]]
- 분산 공식: [[회귀계수의 분산 유도]] (샌드위치 vs $\sigma^2(X'V^{-1}X)^{-1}$)
- 허브: [[MOC_추정효율성]] (Cluster A) 가지 ②

---

## 🔁 이어가기 — 2026-06-29 세션 (B단계 완결)
1. **대상**: `[[Aitken 정리]]` B단계(최소분산) · 교재 외 고전결과(관련: §6.3 WLS) · 트랙 A(백지유도)
2. **오늘 한 것**: B단계 6스텝 완주 — $C=C_{GLS}+D$ 분해 → 불편성으로 $DX=0$ → 전개 후 $C_{GLS}V=(X'V^{-1}X)^{-1}X'$ 로 교차항 소거 → 첫 항이 $\text{Var}(\hat\beta_{GLS})$ 임을 $X'C_{GLS}'=(C_{GLS}X)'=I$ 로 확인 → $\text{Var}(\tilde\beta)=\text{Var}(\hat\beta_{GLS})+\sigma^2 DVD'\succeq\text{Var}(\hat\beta_{GLS})$. **유일성**($\iff D=0$)까지.
3. **핵심 결과·상태** ⭐: **증명 완결.** status "완료"로 갱신. L·U·B 표 전부 ✅.
4. **막힌 지점**: (교정) $C=X^{-1}$ 로 적음 → $X$ 가 $n\times p$ 비정사각 → 양쪽 역행렬 없음; $CX=I_p$ 는 *왼쪽 역행렬*이고 무수히 많음(=경쟁자 집합). "$V$ 양정치 가정"의 위치도 질문 → 명제 가정 ③ 확인.
5. **검증**: 차원·전치·계수 논증으로 자체 검증 ✅. 수치(R/Python) 검산은 미실시 — 원하면 다음에 $V$ 임의 양정치로 $\text{Var}(\tilde\beta)\succeq\text{Var}(\hat\beta_{GLS})$ 고윳값≥0 확인 가능.
6. **다음 출발점** →: 효율성 가지 확장 — `[[가중최소제곱(WLS)]]`(GLS 대각 특수경우 $w_i=1/\sigma_i^2$) 또는 `[[Gauss-Markov 정리]]` 본문을 Aitken의 $V=I$ 특수경우로 역방향 정리.
7. **열린 질문**: Q1 등호조건 $DVD'=0\Rightarrow D=0$ 을 Cholesky $V=LL'$ 로 한 줄 보강? / Q2 `[[크라메르-라오 하한 (CRLB)]]` 과 BLUE의 관계(정규성 추가 시 효율성)?
8. **연결**: `[[일반화최소제곱(GLS)]]` · `[[Gauss-Markov 정리]]` · `[[양의 준정부호 순서(Löwner order)]]` · `[[행렬 곱의 계수 부등식]]` · `[[MOC_추정효율성]]`
