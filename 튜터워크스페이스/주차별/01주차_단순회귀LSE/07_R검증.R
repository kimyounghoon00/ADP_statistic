# 01주차 단순회귀 LSE 기초 - R 검증 스크립트
# 손으로 유도한 회귀계수의 기대값과 분산 공식이 시뮬레이션 결과와 일치하는지 검증합니다.

# 1. 가상 데이터 생성 설정
set.seed(42)
n <- 30
x <- runif(n, 1, 10)  # x는 비확률변수(상수)처럼 고정
beta0 <- 2.0
beta1 <- 1.5
sigma <- 1.0  # 오차항의 표준편차

# S_xx 직접 계산
x_bar <- mean(x)
S_xx <- sum((x - x_bar)^2)

# 이론적 분산 값 계산
var_beta1_theory <- (sigma^2) / S_xx
cat("이론적 Var(beta1_hat):", var_beta1_theory, "\n")

# 2. 몬테카를로 시뮬레이션 (10,000회 반복)
sim_runs <- 10000
beta1_hat_sims <- numeric(sim_runs)

for (i in 1:sim_runs) {
  epsilon <- rnorm(n, mean = 0, sd = sigma)
  y <- beta0 + beta1 * x + epsilon
  
  # LSE 추정
  fit <- lm(y ~ x)
  beta1_hat_sims[i] <- coef(fit)["x"]
}

# 3. 결과 비교
mean_beta1_hat_sim <- mean(beta1_hat_sims)
var_beta1_hat_sim <- var(beta1_hat_sims)

cat("======================================\n")
cat("성질 검증 결과:\n")
cat("--------------------------------------\n")
cat("1) 기대값 E[beta1_hat] (이론값:", beta1, ")\n")
cat("   -> 시뮬레이션 평균:", mean_beta1_hat_sim, "\n\n")
cat("2) 분산 Var(beta1_hat) (이론값:", var_beta1_theory, ")\n")
cat("   -> 시뮬레이션 분산:", var_beta1_hat_sim, "\n")
cat("======================================\n")
