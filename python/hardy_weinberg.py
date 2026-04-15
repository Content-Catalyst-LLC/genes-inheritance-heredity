p = 0.7
q = 1 - p

AA = p**2
Aa = 2 * p * q
aa = q**2
H_e = 2 * p * q

print("Expected genotype frequencies")
print("AA =", round(AA, 4))
print("Aa =", round(Aa, 4))
print("aa =", round(aa, 4))
print("Expected heterozygosity =", round(H_e, 4))
