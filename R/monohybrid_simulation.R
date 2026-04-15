set.seed(42)

gamete <- function(genotype) sample(strsplit(genotype, "")[[1]], 1)

offspring <- replicate(10000, {
  paste(sort(c(gamete("Aa"), gamete("Aa"))), collapse = "")
})

result <- prop.table(table(offspring))
print(round(result, 4))
