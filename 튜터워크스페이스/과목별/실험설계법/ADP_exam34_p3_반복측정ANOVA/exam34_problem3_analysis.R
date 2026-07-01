# =====================================================================
# ADP exam34 - 문제3
# 성별(between) x 학습방법(within, 반복측정)에 따른 성적 차이
# 혼합설계 반복측정 분산분석 (Mixed-design Repeated Measures ANOVA)
# =====================================================================

suppressPackageStartupMessages({
  library(tidyr); library(dplyr); library(rstatix); library(car); library(emmeans)
  library(ggplot2)
})

path <- "C:/Users/kim_y/OneDrive/문서/Rprojects/Rbasics/ADP기출문제데이터/exam34/exam34_problem3.csv"
wide <- read.csv(path, fileEncoding = "UTF-8")
wide$gender <- factor(wide$gender, levels = c("M","F"))

# ---- wide -> long ----
long <- wide %>%
  pivot_longer(cols = c(Tradition, Online, Mix),
               names_to = "method", values_to = "score") %>%
  mutate(ID = factor(ID),
         method = factor(method, levels = c("Tradition","Online","Mix")))

cat("==== [0] 데이터 구조 ====\n")
cat("관측치:", nrow(long), " (40명 x 3방법)\n")
print(long %>% group_by(gender) %>% summarise(n_subj = n_distinct(ID)))
cat("\n셀별 평균/표준편차:\n")
print(long %>% group_by(gender, method) %>%
        summarise(mean = round(mean(score),2), sd = round(sd(score),2), .groups="drop"))

# =====================================================================
# [1] 사전 가정 검토
# =====================================================================
cat("\n\n==== [1] 사전 가정 검토 ====\n")

# (1) 정규성: 셀(gender x method)별 Shapiro-Wilk
cat("\n-- (1) 정규성 (Shapiro-Wilk, 셀별) --\n")
print(long %>% group_by(gender, method) %>%
        shapiro_test(score) %>%
        mutate(정규성 = ifelse(p > .05, "충족", "위배")) %>%
        as.data.frame())


# (2) 등분산성: Levene (between 요인 gender 기준, 각 방법별)
cat("\n-- (2) 등분산성 (Levene, gender 기준) --\n")
print(long %>% group_by(method) %>%
        levene_test(score ~ gender) %>% as.data.frame())

# (3) 구형성(Mauchly)은 아래 anova_test() 출력에 자동 포함됨
cat("\n-- (3) 구형성(Mauchly) -> [2] ANOVA 출력의 $`Mauchly's Test` 참조 --\n")

# =====================================================================
# [2] 혼합 반복측정 ANOVA (주효과 + 상호작용)
# =====================================================================
cat("\n\n==== [2] 혼합 반복측정 ANOVA ====\n")
res <- anova_test(data = long, dv = score, wid = ID,
                  between = gender, within = method) 
cat("\n-- ANOVA 표 (Greenhouse-Geisser 보정 포함) --\n")
print(get_anova_table(res, correction = "auto"))
cat("\n-- Mauchly 구형성 검정 --\n")
print(res$`Mauchly's Test for Sphericity`)
cat("\n-- 구형성 보정계수 (GGe/HFe) --\n")
print(res$`Sphericity Corrections`)

# =====================================================================
# [3] 사후분석 (학습방법 주효과 유의 시)
# =====================================================================
cat("\n\n==== [3] 사후분석: 학습방법 (Bonferroni 보정 pairwise paired t) ====\n")
ph <- long %>%
  pairwise_t_test(score ~ method, paired = TRUE,
                  p.adjust.method = "bonferroni")
print(as.data.frame(ph))

# =====================================================================
# [4] 시각화
# =====================================================================
cat("\n\n==== [4] 시각화 (PNG 저장) ====\n")
# PNG는 이 스크립트가 있는 폴더에 저장 (CSV는 원본 ADP 폴더에 유지)
outdir <- "C:/Users/kim_y/OneDrive/문서/회귀분석/튜터워크스페이스/과목별/실험설계법/ADP_exam34_p3_반복측정ANOVA"
# 한글 폰트 (Windows)
if (.Platform$OS.type == "windows") {
  windowsFonts(malgun = windowsFont("Malgun Gothic")); base_font <- "malgun"
} else base_font <- ""
thm <- theme_bw(base_size = 13) + theme(text = element_text(family = base_font))

# 셀별 요약 (평균 ± 표준오차)
summ <- long %>% group_by(gender, method) %>%
  summarise(mean = mean(score), se = sd(score)/sqrt(n()), .groups = "drop")

# (1) 상호작용 플롯 — 평균 ± SE
p1 <- ggplot(summ, aes(method, mean, color = gender, group = gender)) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  geom_errorbar(aes(ymin = mean - se, ymax = mean + se), width = .12) +
  labs(title = "상호작용 플롯: 학습방법 x 성별 (평균 ± SE)",
       x = "학습방법", y = "성적 평균", color = "성별") + thm
ggsave(file.path(outdir, "p3_01_interaction.png"), p1, width = 7, height = 5, dpi = 120)

# (2) 박스플롯 — 성별 x 방법
p2 <- ggplot(long, aes(method, score, fill = gender)) +
  geom_boxplot(alpha = .7, outlier.size = 1, position = position_dodge(.8)) +
  labs(title = "성별 x 학습방법별 성적 분포",
       x = "학습방법", y = "성적", fill = "성별") + thm
ggsave(file.path(outdir, "p3_02_boxplot.png"), p2, width = 7, height = 5, dpi = 120)

# (3) 개체 프로파일 (spaghetti) — 반복측정 구조 시각화
p3 <- ggplot(long, aes(method, score, group = ID)) +
  geom_line(alpha = .25, color = "grey40") +
  stat_summary(aes(group = 1), fun = mean, geom = "line",
               color = "red", linewidth = 1.3) +
  stat_summary(aes(group = 1), fun = mean, geom = "point",
               color = "red", size = 3) +
  facet_wrap(~ gender) +
  labs(title = "개체별 프로파일 (회색=개인, 빨강=평균)",
       x = "학습방법", y = "성적") + thm
ggsave(file.path(outdir, "p3_03_profile.png"), p3, width = 9, height = 5, dpi = 120)

# (4) 사후분석 시각화 — 유의 쌍 표시
p4 <- ggplot(long, aes(method, score)) +
  geom_boxplot(fill = "#9ecae1", alpha = .7, width = .5) +
  stat_summary(fun = mean, geom = "point", color = "red", size = 3) +
  labs(title = "학습방법 주효과 (Online < Mix, p.adj=0.00013 ***)",
       x = "학습방법", y = "성적") + thm
ggsave(file.path(outdir, "p3_04_posthoc.png"), p4, width = 7, height = 5, dpi = 120)

cat("저장: p3_01_interaction.png, p3_02_boxplot.png, p3_03_profile.png, p3_04_posthoc.png\n")

cat("\n분석 완료.\n")
