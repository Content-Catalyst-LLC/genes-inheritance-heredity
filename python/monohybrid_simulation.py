import random
from collections import Counter

def gamete(genotype):
    return random.choice(list(genotype))

offspring = []
for _ in range(10000):
    child = "".join(sorted(gamete("Aa") + gamete("Aa")))
    offspring.append(child)

counts = Counter(offspring)
total = sum(counts.values())

for genotype in sorted(counts):
    print(genotype, round(counts[genotype] / total, 4))
