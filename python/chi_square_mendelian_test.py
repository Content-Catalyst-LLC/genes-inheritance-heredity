observed = {"dominant": 315, "recessive": 105}
total = sum(observed.values())

expected = {
    "dominant": total * 3/4,
    "recessive": total * 1/4
}

chi_square = sum(
    (observed[k] - expected[k])**2 / expected[k]
    for k in observed
)

print("Observed counts:", observed)
print("Expected counts:", expected)
print("Chi-square =", round(chi_square, 4))
