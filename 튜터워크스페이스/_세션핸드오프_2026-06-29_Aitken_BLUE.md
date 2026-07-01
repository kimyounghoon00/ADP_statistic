---
type: session-handoff
aliases: [이어가기, 2026-06-29 세션, Aitken BLUE]
tags: [Handoff, 회귀분석, Aitken, BLUE, GLS, 효율성, Hub]
date: "2026-06-29"
---

# 🔖 이어가기 — 2026-06-29 세션 (Aitken 정리: GLS가 BLUE)

> 6/28 핸드오프 1순위 "GLS가 BLUE임을 증명"을 착수. **L·U는 통과, B(최소분산)는 출발 식만 세우고 중단**.

## 1. 대상 (What)
- 핵심 위키링크: `[[Aitken 정리]]` · `[[일반화최소제곱(GLS)]]` · `[[Gauss-Markov 정리]]`
- 과목·챕터: 회귀분석 Ch3 확장 (오차가정 위반의 처방)
- 트랙: A(백지유도) · Cluster A([[MOC_추정효율성]]) 가지 ②

## 2. 오늘 한 것 (Done)
- BLUE 를 **B·L·U·E** 글자별 조건으로 분해. (E=Estimator는 조건 아님 — 명칭일 뿐)
- **L**: $\hat\beta_{GLS}=C_{GLS}\mathbf y$, $C_{GLS}=(X'V^{-1}X)^{-1}X'V^{-1}$ → 선형 자명.
- **U**: $E[\tilde\beta]=(CX)\beta$ → 모든 $\beta$ 에 **$CX=I_p$**. 경쟁자 집합 $\mathcal C=\{C\mathbf y:CX=I_p\}$ 확정, $C_{GLS}X=I$ 로 후보 소속 확인.
- 파생 stub 2개: `[[행렬 곱의 계수 부등식]]`, `[[양의 준정부호 순서(Löwner order)]]`.

## 3. 핵심 결과 · 도달 상태 (State) ⭐
- 경쟁자 분산: $\text{Var}(\tilde\beta)=\sigma^2 CVC'$ (∵ $\text{Var}(\mathbf y)=\sigma^2 V$).
- 후보 분산: $\text{Var}(\hat\beta_{GLS})=\sigma^2(X'V^{-1}X)^{-1}$.
- **여기서 멈춤** — 둘의 비교(최소분산 증명)는 미착수.

## 4. 막힌 지점 / 교정한 실수 (Stuck→Fixed)
- `XC=I` 로 씀 → **`CX=I`** (차원 $C_{p\times n},X_{n\times p}$ + 계수 $\operatorname{rank}(XC)\le p<n$ 검산). 학생이 직접 잡음.
- `E`(Estimator)를 증명조건으로 착각 → L·U·B 셋만.
- $\hat\beta=C\mathbf y$ 를 $\mathbf y$ 에 재대입해 식 꼬임 → $\tilde\beta=C\mathbf y$ 에 곧장 $E[\cdot]$.
- "Best=최소제곱이 최소" 혼동 → 최소화 대상은 *분산* $\text{Var}(\hat\beta)$.

## 5. 검증 (Check)
- 수식 차원·계수 논증으로 자체 검증. (수치 R/Python 검산은 B단계 완료 후 한꺼번에 예정)

## 6. 다음 출발점 (Next) — 명령형
- → **`[[Aitken 정리]]` §3 "B 단계"부터**: $C=C_{GLS}+D$ 분해 → 불편성에서 $DX=0$ → 교차항($X'D'=0$로) 소거 → $\text{Var}(\tilde\beta)=\text{Var}(\hat\beta_{GLS})+\sigma^2 DVD'\succeq\text{Var}(\hat\beta_{GLS})$. 등호 $\iff D=0$.
- 그 전에 `[[양의 준정부호 순서(Löwner order)]]` 로 "$\succeq$"의 뜻부터 못 박기.

## 7. 다음 세션 주제 리스트 (우선순위)

### A. Aitken 마무리 (직전 흐름 직결) ⭐추천
- [ ] `[[Aitken 정리]]` B 단계 완결 (위 6번)
- [ ] 완료 후 status를 "백지유도 통과"로 갱신, MOC 이어가기 한 줄 추가

### B. 효율성 가지 확장
- [ ] `[[가중최소제곱(WLS)]]` — 이분산 처방, GLS 대각 특수경우 ($w_i=1/\sigma_i^2$)
- [ ] `[[FGLS]]` 2단계 + Cochrane–Orcutt / Prais–Winsten (AR(1), DW 연결)

### C. 보조개념 stub 본문 채우기
- [ ] `[[Gauss-Markov 정리]]` 본문(BLUE 증명) — Aitken의 $V=I$ 특수경우로 역방향 정리
- [ ] `[[회귀계수의 분산 유도]]`, `[[다중공선성]]`, `[[분산팽창인자(VIF)]]` (6/29 오전 stub)

## 8. 연결 (Links)
- 본체: `[[Aitken 정리]]` ← `[[일반화최소제곱(GLS)]]` ← `[[Gauss-Markov 정리]]`
- 도구: `[[행렬 곱의 계수 부등식]]` · `[[양의 준정부호 순서(Löwner order)]]`
- 허브: `[[MOC_추정효율성]]` (Cluster A 가지 ②)
