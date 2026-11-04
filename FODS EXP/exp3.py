import numpy as np

a = np.array([[3, 1500, 200000],
              [5, 2500, 400000],
              [6, 3000, 500000],
              [4, 1800, 250000]])

b = a[a[:, 0] > 4]

print("Average price:", np.mean(b[:, 2]))
