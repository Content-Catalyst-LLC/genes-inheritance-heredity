genotypes = [2, 2, 1, 1, 1, 0, 2, 1, 0, 2, 1, 1, 2, 0, 1, 2]
# 2 = AA, 1 = Aa, 0 = aa

n = len(genotypes)
n_AA = genotypes.count(2)
n_Aa = genotypes.count(1)
n_aa = genotypes.count(0)

p = (2 * n_AA + n_Aa) / (2 * n)
q = 1 - p
H_e = 2 * p * q

print("p =", round(p, 4))
print("q =", round(q, 4))
print("Expected heterozygosity =", round(H_e, 4))
