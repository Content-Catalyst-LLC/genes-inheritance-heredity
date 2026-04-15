observed <- c(dominant = 315, recessive = 105)
expected <- c(dominant = 420 * 3/4, recessive = 420 * 1/4)

chi_square <- sum((observed - expected)^2 / expected)

cat("Observed counts\n")
print(observed)

cat("Expected counts\n")
print(expected)

cat("Chi-square =", round(chi_square, 4), "\n")
