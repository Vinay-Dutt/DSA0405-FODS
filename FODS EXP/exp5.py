import numpy as np

a = np.array([25, 30, 35, 40])

print("Average:", np.mean(a))

p = ((a[1] - a[0]) / a[0]) * 100

print("Improvement:", p, "%")
