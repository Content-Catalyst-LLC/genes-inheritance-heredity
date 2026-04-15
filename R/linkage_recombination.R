set.seed(42)

r <- 0.18
gametes <- sample(
  c("AB", "ab", "Ab", "aB"),
  size = 20000,
  replace = TRUE,
  prob = c((1 - r) / 2, (1 - r) / 2, r / 2, r / 2)
)

freq <- prop.table(table(gametes))
print(round(freq, 4))

recomb_fraction <- freq["Ab"] + freq["aB"]
cat("Estimated recombination fraction =", round(recomb_fraction, 4), "\n")
