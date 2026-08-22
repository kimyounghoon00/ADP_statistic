# -*- coding: utf-8 -*-
"""
자기참조적 집단화와 F검정의 함정 — 재현 스크립트
================================================
세션: 2026-08-22  ANOVA를 새로운 관점에서
노트: [[자기참조적 집단화와 F검정의 함정]] · [[무작위화 (Randomization)]]

설정
----
모집단은 N(50, 100) '하나'뿐이다. 처리효과도, 성별이라는 실체도 없다.
그런데 반응변수 X 자체로 집단을 만들면(X>50 → '남'), 존재하지 않는 효과가
100% 검출된다. 이 스크립트는 그 사실과 원인을 수치로 확인한다.

비교 케이스
-----------
A. 자기참조 : g = 1{X > 50}          설명변수 = 오차항의 부호        ← 학습자의 구성
B. 무작위화 : g = 동전던지기          X와 독립                        ← 올바른 설계
C. 진짜효과 : g 먼저, 그 다음 Y = 50 + 3g + ε                        ← 참조군
D. 탐색     : 절단점을 F 최대가 되게 고름                             ← data snooping 극단

실행: python3 self_referential_anova.py
필요: numpy, scipy, matplotlib
"""
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

SEED, MU, SIGMA, N, B = 20260822, 50.0, 10.0, 100, 50_000
rng = np.random.default_rng(SEED)
HERE = Path(__file__).resolve().parent


# ─────────────────────────────────────────────────────────────────────
# 2군 일원 ANOVA (= 2표본 t검정, F = t²) 를 B개 반복에 대해 한 번에 계산
# ─────────────────────────────────────────────────────────────────────
def anova2(Y, G):
    """Y, G: (B, n) 배열. 반환 (F, p, R², β̂₁)"""
    n = Y.shape[1]
    n1 = G.sum(axis=1)
    n0 = n - n1
    m1 = (Y * G).sum(axis=1) / n1              # 집단 1 평균
    m0 = (Y * (1 - G)).sum(axis=1) / n0        # 집단 0 평균
    gm = Y.mean(axis=1)                        # 전체 평균
    SStr = n1 * (m1 - gm) ** 2 + n0 * (m0 - gm) ** 2   # 처리제곱합 (df=1)
    SST = ((Y - gm[:, None]) ** 2).sum(axis=1)
    SSe = SST - SStr                                    # 오차제곱합 (df=n-2)
    F = (SStr / 1) / (SSe / (n - 2))
    return F, stats.f.sf(F, 1, n - 2), SStr / SST, m1 - m0


def banner(t, w=74):
    print("\n" + "=" * w + f"\n{t}\n" + "=" * w)


# ═════════════════════════════════════════════════════════════════════
# 1. 네 가지 케이스
# ═════════════════════════════════════════════════════════════════════
X = rng.normal(MU, SIGMA, size=(B, N))

# A. 자기참조 — 반응변수 그 자체로 집단을 만든다
G_self = (X > 50).astype(float)
F_a, p_a, R2_a, b1_a = anova2(X, G_self)

# B. 무작위 배정 — 동전던지기. X를 보기 전에 정해진다
G_rand = rng.integers(0, 2, size=(B, N)).astype(float)
deg = (G_rand.sum(axis=1) == 0) | (G_rand.sum(axis=1) == N)   # 한쪽이 비면 보정
G_rand[deg, 0], G_rand[deg, 1] = 1, 0
F_b, p_b, R2_b, b1_b = anova2(X, G_rand)

# C. 진짜 효과 3 — 집단이 먼저, 값이 나중
G_true = rng.integers(0, 2, size=(B, N)).astype(float)
Y_true = rng.normal(MU, SIGMA, size=(B, N)) + 3.0 * G_true
F_c, p_c, R2_c, b1_c = anova2(Y_true, G_true)

banner(f"모집단은 N(50,100) 하나뿐. '성별'이라는 실체는 없음.   반복 B = {B:,}")
print(f"{'':<32}{'β̂₁':>9}{'F':>10}{'R²':>9}{'기각률':>10}")
print("-" * 74)
for nm, F_, p_, R_, b_ in [("A. 자기참조 (X>50 → 남)", F_a, p_a, R2_a, b1_a),
                           ("B. 무작위 배정 (동전던지기)", F_b, p_b, R2_b, b1_b),
                           ("C. 진짜 효과 3 (집단 → 값)", F_c, p_c, R2_c, b1_c)]:
    print(f"{nm:<30}{np.abs(b_).mean():>9.3f}{F_.mean():>10.2f}"
          f"{R_.mean():>9.4f}{np.mean(p_ < .05):>10.4f}")
print("-" * 74)
print(f"{'   이론 F(1,98)':<30}{'':>9}{98/96:>10.2f}{'':>9}{0.05:>10.4f}")

# ═════════════════════════════════════════════════════════════════════
# 2. 케이스 A 해부 — '효과'의 정체는 100% 내생성 편의
# ═════════════════════════════════════════════════════════════════════
banner("케이스 A 해부")
print("  원래 모형:  X_i = 50 + ε_i,  ε_i ~ N(0,100)")
print("  집단 정의:  g_i = 1{X_i > 50} = 1{ε_i > 0}   ← 설명변수가 오차항의 부호 그 자체\n")
cov_ge = SIGMA * stats.norm.pdf(0)          # E[ε·1{ε>0}] = σ·φ(0)
print(f"  Cov(g, ε) = σ·φ(0)                = {cov_ge:.4f}")
print(f"  Var(g)                            = {0.25:.4f}")
print(f"  더미 OLS 기울기 = Cov/Var         = {cov_ge/0.25:.3f}   ← 전부 편의. 참효과는 0")
print(f"  이론 β₁ = 2σ√(2/π)                = {2*SIGMA*np.sqrt(2/np.pi):.3f}")
print(f"  시뮬레이션 β̂₁ 평균                = {b1_a.mean():.3f}\n")
print(f"  R²  이론 2/π = {2/np.pi:.4f}   시뮬 {R2_a.mean():.4f}   → 분산의 64%를 '설명'")
print(f"  F   평균 {F_a.mean():.2f}  중앙값 {np.median(F_a):.2f}  최솟값 {F_a.min():.2f}")
print(f"  p   최댓값 {p_a.max():.3e}   (B회 중 p>0.05 인 경우: {int(np.sum(p_a>.05))}회)")
print(f"  F(1,98) 5% 임계값 {stats.f.ppf(.95,1,98):.3f} — A의 최솟값이 이미 "
      f"{F_a.min()/stats.f.ppf(.95,1,98):.0f}배")

# ═════════════════════════════════════════════════════════════════════
# 3. 진단은 잡아내지 못한다
# ═════════════════════════════════════════════════════════════════════
banner("잔차 진단이 이 함정을 잡아낼 수 있는가")
Bd, sh_rej, lev_rej, v1, v0 = 3_000, 0, 0, [], []
rg = np.random.default_rng(7)
for _ in range(Bd):
    x = rg.normal(MU, SIGMA, N)
    a, b = x[x > 50], x[x <= 50]
    if min(len(a), len(b)) < 5:
        continue
    res = np.concatenate([a - a.mean(), b - b.mean()])
    sh_rej += stats.shapiro(res).pvalue < .05
    lev_rej += stats.levene(a, b, center="median").pvalue < .05
    v1.append(a.var(ddof=1)); v0.append(b.var(ddof=1))
print(f"  Levene  (등분산성) 기각률 = {lev_rej/Bd:.4f}   ← 명목 0.05. 완벽 통과. 못 잡는다")
print(f"  Shapiro (정규성)   기각률 = {sh_rej/Bd:.4f}   ← 60%는 그냥 통과한다")
print(f"  집단내 분산: 남 {np.mean(v1):.2f} / 여 {np.mean(v0):.2f}"
      f"   (이론 σ²(1−2/π) = {100*(1-2/np.pi):.2f})  → 정말로 등분산")
big = rg.normal(MU, SIGMA, 2_000_000)
print(f"  남 집단 왜도 = {stats.skew(big[big>50]):.3f}  (정규면 0) → 실제로는 절단정규")
print("  ⇒ '집단을 Y로 만들었다'는 정보는 데이터 안에 없다. 진단은 원리적으로 접근 불가.")

# ═════════════════════════════════════════════════════════════════════
# 4. 케이스 D — 절단점을 데이터에 물어보면
# ═════════════════════════════════════════════════════════════════════
banner("케이스 D: 절단점을 F 최대가 되게 고르면 (2,000회)")
Xs = np.sort(X[:2000], axis=1)
Fmax = np.empty(2000)
for i, x in enumerate(Xs):
    cs = np.cumsum(x); tot, k = cs[-1], np.arange(1, N)
    m0, m1, gm = cs[:-1]/k, (tot-cs[:-1])/(N-k), tot/N
    SStr = k*(m0-gm)**2 + (N-k)*(m1-gm)**2
    SST = ((x-gm)**2).sum()
    Fmax[i] = (SStr/((SST-SStr)/(N-2))).max()
crit = stats.f.ppf(.95, 1, N-2)
print(f"  max F: 평균 {Fmax.mean():.2f}  중앙값 {np.median(Fmax):.2f}  최솟값 {Fmax.min():.2f}")
print(f"  임계값 {crit:.2f} 초과 비율 = {np.mean(Fmax>crit)*100:.1f}%")
print("  ⇒ 99개 후보를 뒤졌는데 자유도는 여전히 (1, 98). 탐색 비용이 청구되지 않았다.")

# ═════════════════════════════════════════════════════════════════════
# 5. 그림
# ═════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Self-referential grouping: a 100% false-discovery machine\n"
             r"Population is a single $N(50,\ 100)$ — no group effect exists",
             fontsize=13, fontweight="bold")

# (1) 절단 그림
a0 = ax[0, 0]
s = X[0]
a0.hist(s[s <= 50], bins=18, alpha=.75, color="#4C78A8", label="'female'  (X ≤ 50)")
a0.hist(s[s > 50],  bins=18, alpha=.75, color="#E45756", label="'male'  (X > 50)")
a0.axvline(50, color="k", ls="--", lw=1.5)
for m, c in [(s[s <= 50].mean(), "#2B4F73"), (s[s > 50].mean(), "#A32C2B")]:
    a0.axvline(m, color=c, lw=2.5)
a0.set_ylim(0, 14)
a0.annotate("", xy=(s[s > 50].mean(), 10.4), xytext=(s[s <= 50].mean(), 10.4),
            arrowprops=dict(arrowstyle="<->", lw=2, color="#333"))
a0.text(50, 11.0, r"$\hat\beta_1 \approx 15.96$" "\nbaked in by the cut",
        ha="center", fontsize=10, fontweight="bold")
a0.set_title("(1) The gap is decided before you look at the data", fontsize=11)
a0.set_xlabel("X"); a0.set_ylabel("count"); a0.legend(fontsize=9)

# (2) F 분포 비교 (로그 x축)
a1 = ax[0, 1]
# 로그 구간에서 '구간확률'로 비교해야 두 케이스가 함께 보인다 (밀도 정규화는 A를 지워버림)
edges = np.logspace(-3, 2.8, 70)
ctr = np.sqrt(edges[:-1] * edges[1:])
a1.step(ctr, np.diff(stats.f.cdf(edges, 1, 98)), where="mid",
        color="k", lw=2, label="theory  F(1, 98)")
a1.hist(F_b, bins=edges, weights=np.full(B, 1/B), alpha=.6,
        color="#54A24B", label="B. randomized")
a1.hist(F_a, bins=edges, weights=np.full(B, 1/B), alpha=.8,
        color="#E45756", label="A. self-referential")
a1.axvline(crit, color="#B279A2", ls="--", lw=2, label=f"5% cutoff = {crit:.2f}")
a1.annotate("100% of case A\nlands out here",
            xy=(F_a.mean(), .055), xytext=(9, .085), fontsize=9.5,
            fontweight="bold", color="#A32C2B",
            arrowprops=dict(arrowstyle="->", lw=1.6, color="#A32C2B"))
a1.set_xscale("log"); a1.set_xlabel("F  (log scale)")
a1.set_ylabel("probability per bin")
a1.set_title("(2) Case A never even touches the null distribution", fontsize=11)
a1.legend(fontsize=9)

# (3) 기각률
a2 = ax[1, 0]
names = ["A. self-\nreferential", "B. randomized\n(no effect)", "C. real effect\n= 3"]
vals = [np.mean(p_a < .05), np.mean(p_b < .05), np.mean(p_c < .05)]
bars = a2.bar(names, vals, color=["#E45756", "#54A24B", "#4C78A8"], width=.6)
a2.axhline(.05, color="k", ls="--", lw=1.5)
a2.text(2.42, .07, "nominal 5%", fontsize=9)
for b_, v in zip(bars, vals):
    a2.text(b_.get_x() + b_.get_width()/2, v + .025, f"{v*100:.2f}%",
            ha="center", fontweight="bold")
a2.set_ylim(0, 1.15); a2.set_ylabel("rejection rate")
a2.set_title("(3) The fake effect is detected 3× better than the real one", fontsize=11)

# (4) 진단 무력함
a3 = ax[1, 1]
dn = ["Levene\n(equal variance)", "Shapiro-Wilk\n(normality)"]
dv = [lev_rej/Bd, sh_rej/Bd]
bars = a3.bar(dn, dv, color=["#54A24B", "#F58518"], width=.5)
a3.axhline(.05, color="k", ls="--", lw=1.5)
a3.text(1.30, .07, "nominal 5%", fontsize=9)
for b_, v in zip(bars, dv):
    a3.text(b_.get_x() + b_.get_width()/2, v + .015, f"{v*100:.1f}%",
            ha="center", fontweight="bold")
a3.set_ylim(0, .55); a3.set_ylabel("rejection rate of the diagnostic")
a3.set_title("(4) Diagnostics cannot see it — provenance is not in the data",
             fontsize=11)

fig.tight_layout(rect=[0, 0, 1, .94])
out = HERE / "fig_01_자기참조집단화.png"
fig.savefig(out, dpi=140)
print(f"\n[그림 저장] {out}")
