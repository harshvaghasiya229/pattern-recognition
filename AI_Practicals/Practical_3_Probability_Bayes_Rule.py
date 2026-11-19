print("IAR/17360")

# Probability of production by each machine
P_M1 = 0.60
P_M2 = 0.40

# Probability of defective items from each machine
P_D_M1 = 0.03
P_D_M2 = 0.05

# Total probability of getting a defective item
P_D = (P_M1 * P_D_M1) + (P_M2 * P_D_M2)

print("Total probability of a defective item:")
print(P_D)
print("Percentage:", P_D * 100, "%")

# Bayes' rule
P_M1_D = (P_M1 * P_D_M1) / P_D
P_M2_D = (P_M2 * P_D_M2) / P_D

print("\nProbability that defective item was made by M1:")
print(P_M1_D)
print("Percentage:", P_M1_D * 100, "%")

print("\nProbability that defective item was made by M2:")
print(P_M2_D)
print("Percentage:", P_M2_D * 100, "%")

# Find which machine is more likely
if P_M1_D > P_M2_D:
    print("\nMachine M1 is more likely to have produced the defective item.")
else:
    print("\nMachine M2 is more likely to have produced the defective item.")
