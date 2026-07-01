---
aliases: [점근표기법, 란다우 표기법, Big-O, little-o, Op, op, 확률적 차수]
subject: 수리통계학 (점근이론 — 공통 도구)
concept: '[[점근 표기법(Big-O)]]'
cluster:
- 점근이론
- 공통수학도구
tags:
- 수리통계학
- 점근이론
- BigO
- littleo
- 확률수렴
- 일치성
- 공통도구
cross_ref:
- '[[Durbin-Watson 검정]] (끝점 항 $O(1/n)\to0$)'
- '[[Breusch-Pagan 검정]]'
- '[[대수의 법칙(LLN)]] / [[중심극한정리(CLT)]]'
- '[[델타방법(Delta Method)]] (Hogg §5.2.2, Thm 5.2.9)'
- 'Hogg 『Math Stat』 8th §5.2.2 (테일러+o_p)'
date_created: "2026-06-28"
date_modified: "2026-06-28"
status: "공통 도구 노트 — 여러 과목 교차 사용"
note_분류근거: "회귀분석 고유 개념 아님. 시계열·수리통계·비모수 공통. 그래서 회귀분석 폴더가 아니라 수리통계학(점근이론)에 둠."
---

# [[점근 표기법(Big-O)]] — 극한에서의 '크기'를 재는 도구

> **한 줄 핵심**: $O$ 는 "상수배 이내로 같은 속도이거나 더 느림", $o$ 는 "비교 대상에 비해 무시할 만큼 작음". 둘 다 $n\to\infty$ (또는 $x\to0$) **극한에서의 행동**만 본다.

---

## 1. 직관 — 두 단어로

- **$a_n = O(b_n)$** : "$a_n$ 은 $b_n$ 을 (상수배 빼고) **추월하지 못한다**." 같은 속도이거나 더 느리다.
- **$a_n = o(b_n)$** : "$a_n$ 은 $b_n$ 옆에서 **사라진다**." 비율이 0으로 간다.

비유: 자동차 $a_n$ 과 기준차 $b_n$ 이 무한히 달릴 때 —
$O$ 는 "내 차가 기준차보다 더 빨라지진 않는다(추월 금지, 동급 허용)", $o$ 는 "거리가 무한히 벌어져 백미러에서 사라진다".

---

## 2. 정의 (결정론적 버전)

$$a_n = O(b_n) \iff \exists\,C>0,\ \exists\,N:\quad |a_n|\le C\,|b_n|\quad(\forall\,n\ge N)$$

$$a_n = o(b_n) \iff \lim_{n\to\infty}\frac{a_n}{b_n}=0$$

- 특수기호 $O(1)$ = "유계(bounded)", $o(1)$ = "0으로 수렴".
- 포함관계: $a_n=o(b_n)\ \Rightarrow\ a_n=O(b_n)$ (역은 거짓). 즉 $o$ 가 $O$ 보다 강한 진술.
- 연산: $O(n)+O(n^2)=O(n^2)$ (큰 쪽이 흡수), $C\cdot O(b_n)=O(b_n)$ (상수 무시).

---

## 3. 두 가지 용법 — 헷갈리지 말 것

| | (A) 점근 분석 (우리가 쓴 것) | (B) 알고리즘 복잡도 |
|---|---|---|
| 극한 | $n\to\infty$ 또는 $x\to0$ | 입력크기 $n\to\infty$ |
| 분야 | 해석학·통계학 | 전산학 |
| 예 | $\frac{e_1^2}{\sum e_t^2}=O(1/n)$ | 정렬 $O(n\log n)$ |

정의는 **완전히 동일**하다. 통계에서 쓰는 건 (A): "표본이 커질 때 어떤 오차/잔여항이 얼마나 빨리 사라지는가".

---

## 4. ⭐ 확률 버전 — $O_p,\ o_p$ (교수 수준, 통계의 진짜 도구)

통계에서 다루는 양은 대개 **확률변수**다. 잔차 $e_t$ 도 랜덤. 그래서 결정론적 $O,o$ 를 그대로 쓰면 엄밀하지 않고, **확률적 차수(stochastic order)**를 쓴다.

- **$X_n = o_p(1)$** : $X_n \xrightarrow{p} 0$ (확률수렴). "확률적으로 무시할 만함."
- **$X_n = O_p(1)$** : $X_n$ 이 **확률적으로 유계(tight)**. 즉 $\forall\varepsilon>0,\ \exists M:\ P(|X_n|>M)<\varepsilon\ (\forall n)$. "터지지 않고 묶여 있음."
- **$X_n = o_p(a_n)$** : $X_n/a_n \xrightarrow{p}0$.

관계: $o_p(1)\Rightarrow O_p(1)$ (수렴하면 유계). $\xrightarrow{d}$ 하는 양(예: $\sqrt n(\bar X-\mu)$)은 $O_p(1)$.

---

## 5. 우리가 쓴 자리 — [[Durbin-Watson 검정]] 엄밀화

DW 유도에서 "$n$ 개 중 끝 항 하나는 무시"라고 한 것을 엄밀히 쓰면:

- 유한분산 가정 하에 $e_t^2 = O_p(1)$ (개별 항은 확률적으로 유계).
- [[대수의 법칙(LLN)]]: $\dfrac1n\sum e_t^2 \xrightarrow{p}\sigma^2>0$, 즉 $\sum e_t^2 = O_p(n)$.
- 따라서

$$\frac{e_1^2}{\sum_{t=1}^n e_t^2}=\frac{O_p(1)}{O_p(n)}=O_p\!\left(\tfrac1n\right)=o_p(1)\ \xrightarrow{p}\ 0$$

→ 끝점 항을 빼도 비는 1로 수렴 ⇒ $\sum_{t=2}^n e_t^2 \approx \sum_{t=1}^n e_t^2$ 가 정당. 이게 $d\approx2(1-\hat\rho)$ 근사의 숨은 엔진.

---

## 6. 통계 전반에서의 쓰임 (왜 이 노트가 교차-과목인가)

- **일치성**: $\hat\theta_n - \theta = o_p(1)$ ⟺ $\hat\theta_n$ 이 $\theta$ 의 일치추정량.
- **수렴속도**: $\hat\theta_n-\theta = O_p(n^{-1/2})$ (모수적 표준속도), 비모수는 $O_p(n^{-2/5})$ 등 더 느림.
- **테일러 전개·델타방법**: 잔여항을 $o_p$ 로 통제해 [[중심극한정리(CLT)]] 적용.
- **시계열·비모수**: 대역폭 $h\to0$, $nh\to\infty$ 같은 조건이 전부 이 표기로 기술됨.

---

## 7. 예시 모음 — 테일러 급수에서 만나는 $O,\ o$

### 7.1 테일러 정리의 두 가지 나머지항 = $O$ 와 $o$ 의 원산지

테일러 정리를 쓰는 순간 빅오·리틀오가 **나머지항(remainder)**으로 자동으로 등장한다. 같은 전개를 두 방식으로 적을 수 있다.

**(a) 페아노(Peano) 나머지 — little-o 형태** ($x\to a$):
$$f(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k + o\big((x-a)^n\big)$$
"나머지는 $(x-a)^n$ 보다 더 빨리 0으로 간다"는 **질적** 진술.

**(b) 라그랑주(Lagrange) 나머지 — big-O 형태** ($f$ 가 $C^{n+1}$):
$$f(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k + \underbrace{\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}}_{=\,O\big((x-a)^{n+1}\big)}$$
"나머지가 $(x-a)^{n+1}$ 규모로 유계"라는 **양적** 진술.

### 7.2 $a=0$ 에서의 표준 전개 (외워둘 것)

$x\to0$ 일 때:
$$e^x = 1 + x + \tfrac{x^2}{2} + o(x^2) = 1 + x + O(x^2)$$
$$\log(1+x) = x - \tfrac{x^2}{2} + o(x^2)$$
$$(1+x)^{\alpha} = 1 + \alpha x + o(x)$$
$$\sin x = x + o(x^2),\qquad \cos x = 1 - \tfrac{x^2}{2} + o(x^3)$$

> 활용 예: $\dfrac{e^x-1}{x}=\dfrac{x+O(x^2)}{x}=1+O(x)\to1$. 극한 계산이 한 줄로 끝난다.

### 7.3 ⭐ 수리통계학 연결 — 델타방법 (Hogg §5.2.2, Thm 5.2.9)

통계에서 테일러+$o_p$ 가 빛나는 대표 장면. **변수가 확률적이라 $o$ 가 $o_p$ 로 바뀐다.**

미분가능한 $g$ 에 대해 영 정리(Young) 형태 (Hogg 식 5.2.9):
$$g(X_n) = g(\theta) + g'(\theta)(X_n-\theta) + o_p(|X_n-\theta|)$$

여기에 $\sqrt n(X_n-\theta)\xrightarrow{d}N(0,\sigma^2)$ 를 곱해 정리하면 (Hogg 식 5.2.15):
$$\sqrt n\big(g(X_n)-g(\theta)\big) = g'(\theta)\sqrt n(X_n-\theta) + \underbrace{o_p\big(\sqrt n|X_n-\theta|\big)}_{\xrightarrow{p}\,0}$$

$\sqrt n|X_n-\theta|$ 가 $O_p(1)$ (확률유계)이므로 나머지항은 $o_p(1)\to0$. 따라서 **델타방법 (Theorem 5.2.9)**:
$$\boxed{\ \sqrt n\big(g(X_n)-g(\theta)\big)\ \xrightarrow{d}\ N\!\big(0,\ \sigma^2\,[g'(\theta)]^2\big)\ }$$

리틀오($o$)가 확률버전($o_p$)으로 갈아입으면서 "테일러 나머지 무시"가 그대로 "점근분포 유도"가 된다. — 이게 너가 말한 "테일러에 빅오·리틀오가 나오는" 정확한 자리다.

### 7.4 손으로 푸는 델타방법 예시

$X_1,\dots,X_n$ 가 평균 $\mu(\neq0)$, 분산 $\sigma^2$. $\sqrt n(\bar X-\mu)\xrightarrow{d}N(0,\sigma^2)$ 는 [[중심극한정리(CLT)]]로 안다. 그럼 $\bar X^2$ 의 점근분포는?

$g(x)=x^2,\ g'(x)=2x,\ g'(\mu)=2\mu$. 델타방법 대입:
$$\sqrt n\big(\bar X^2-\mu^2\big)\xrightarrow{d}N\!\big(0,\ \sigma^2\cdot(2\mu)^2\big)=N(0,\ 4\mu^2\sigma^2)$$

뒤에서 일어난 일: $g(\bar X)=\mu^2+2\mu(\bar X-\mu)+o_p(|\bar X-\mu|)$ 로 전개 → 1차항만 $\sqrt n$ 스케일에서 살아남고 $o_p$ 는 소멸. (Hogg Example 5.2.8과 같은 구조; 베르누이 분산 $g(\theta)=\theta(1-\theta)$ 예시는 Hogg p.336·§7.6.)

---

## 📖 교재 참조 (수리통계학)
- **Hogg et al., *Introduction to Mathematical Statistics* 8th — §5.2.2 Δ-Method (pp.334–336)**, PDF 본문 확인:
  - 식 (5.2.9): 테일러/영 정리 $g(y)=g(x)+g'(x)(y-x)+o(|y-x|)$, $o$ 정의 포함.
  - 식 (5.2.10)–(5.2.11): $o_p,\ O_p$ 정의.
  - **Definition 5.2.2** (Bounded in Probability = $O_p(1)$, p.333), **Theorem 5.2.6/5.2.8** (보조정리), **Theorem 5.2.9** (델타방법 본정리), **Example 5.2.8** (적용).

---
*분류 메모: 이 노트는 `회귀분석`이 아니라 `수리통계학`에 둔다 — 회귀·시계열·비모수가 공유하는 점근이론의 기본 어휘이기 때문. 사용처(DW·BP 등)에서 이 노트로 링크한다.*
