p <- 0.7
q <- 1 - p

AA <- p^2
Aa <- 2 * p * q
aa <- q^2
H_e <- 2 * p * q

cat("Expected genotype frequencies\n")
cat("AA =", round(AA, 4), "\n")
cat("Aa =", round(Aa, 4), "\n")
cat("aa =", round(aa, 4), "\n")
cat("Expected heterozygosity =", round(H_e, 4), "\n")
