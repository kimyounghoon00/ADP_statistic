# =============================================================================
# ADP 32회 문제 3: Boston Housing (506 x 14) — 회귀 가정 검토
#   1. 선형회귀모델의 기본 가정을 검토하시오
#   2. 변수 간 관계 검토 + 문제점 해결방안 2가지 (정의 + 장단점)
#   3. 해결방안 구현 및 결과 제시
# =============================================================================

library(car)     # vif, ncvTest, crPlots, influencePlot
library(lmtest)  # bptest, dwtest, bgtest, resettest

DATA <- "C:/Users/kim_y/OneDrive/문서/Rprojects/Rbasics/ADP기출문제데이터/exam32/exam32_problem3.csv"
OUT  <- "C:/Users/kim_y/OneDrive/문서/회귀분석/.claude/worktrees/regression-model-assumptions-6e847f/튜터워크스페이스/과목별/회귀분석/ADP_exam32_p3_회귀가정"

df <- read.csv(DATA, header = TRUE)
cat("=== 데이터 구조 ===\n"); cat("dim:", dim(df), "\n")
cat("결측치 총합:", sum(is.na(df)), "\n\n")

fit <- lm(medv ~ ., data = df)
n <- nrow(df); p <- length(coef(fit))
cat("=== 완전모형 적합 (medv ~ .) ===\n")
print(summary(fit))

# =============================================================================
# 0. [이론 확인] 손으로 유도한 두 항등식을 데이터로 검증
#      ŷ'e = 0,  y'e = e'e = SSE,  e를 y에 회귀한 기울기 = 1 - R^2
# =============================================================================
y <- df$medv; e <- resid(fit); yhat <- fitted(fit)
SSE <- sum(e^2); SST <- sum((y - mean(y))^2); R2 <- summary(fit)$r.squared

cat("\n=== [0] 직교성 항등식 수치 검증 ===\n")
cat(sprintf("  yhat'e            = %.10f   (이론값 0)\n", sum(yhat * e)))
cat(sprintf("  y'e               = %.4f\n", sum(y * e)))
cat(sprintf("  e'e (=SSE)        = %.4f   -> 두 값이 일치해야 함\n", SSE))
cat(sprintf("  e~y 회귀 기울기   = %.6f\n", coef(lm(e ~ y))[2]))
cat(sprintf("  1 - R^2           = %.6f   -> 두 값이 일치해야 함\n", 1 - R2))
cat(sprintf("  e~yhat 회귀 기울기= %.10f   (이론값 0)\n", coef(lm(e ~ yhat))[2]))

# =============================================================================
# 1. 기본 가정 검토 — 선형성 / 독립성 / 등분산성 / 정규성
# =============================================================================
png(file.path(OUT, "p3_01_diagnostics.png"), width = 1100, height = 1000, res = 110)
par(mfrow = c(2, 2))
plot(fit, which = 1:4)
par(mfrow = c(1, 1))
dev.off()

cat("\n\n############ [1] 회귀 기본 가정 검토 ############\n")

cat("\n--- (1) 선형성: Ramsey RESET test ---\n")
cat("  H0: 모형이 선형 (누락된 고차항 없음)\n")
print(resettest(fit, power = 2:3, type = "fitted"))

cat("\n--- (2) 독립성: Durbin-Watson / Breusch-Godfrey ---\n")
cat("  H0: 오차 자기상관 없음 (rho = 0)\n")
print(dwtest(fit))
print(bgtest(fit, order = 1))

cat("\n--- (3) 등분산성: Breusch-Pagan / ncvTest ---\n")
cat("  H0: 오차 등분산 (homoscedasticity)\n")
print(bptest(fit))
print(ncvTest(fit))

cat("\n--- (4) 정규성: Shapiro-Wilk ---\n")
cat("  H0: 오차가 정규분포를 따름\n")
print(shapiro.test(e))
cat(sprintf("  왜도(skewness) = %.4f\n", mean((e - mean(e))^3) / sd(e)^3))
cat(sprintf("  첨도(kurtosis) = %.4f  (정규분포=3)\n", mean((e - mean(e))^4) / sd(e)^4))

cat("\n--- (참고) 이상치 · 영향점 ---\n")
cd <- cooks.distance(fit); hv <- hatvalues(fit); rst <- rstudent(fit)
cat(sprintf("  Cook's D > 4/n(=%.4f) 인 관측치 개수: %d\n", 4/n, sum(cd > 4/n)))
cat("  Cook's D 상위 5개:", paste(order(cd, decreasing = TRUE)[1:5], collapse = ", "), "\n")
cat(sprintf("  레버리지 > 2p/n(=%.4f) 인 관측치 개수: %d\n", 2*p/n, sum(hv > 2*p/n)))
cat(sprintf("  |외적 스튜던트화 잔차| > 3 인 관측치 개수: %d\n", sum(abs(rst) > 3)))
cat(sprintf("  medv == 50 (상한 절단 의심) 인 관측치 개수: %d\n", sum(df$medv == 50)))
