import numpy as np

a = np.array([10000, 12000, 15000, 20000])

print("Total sales:", np.sum(a))

p = ((a[3] - a[0]) / a[0]) * 100

print("Percentage increase:", p)
