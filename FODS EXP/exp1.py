import numpy as np

a = np.array([[80, 90, 70, 85],
              [85, 80, 90, 75],
              [90, 85, 80, 90],
              [75, 95, 85, 80]])

avg = np.mean(a, axis=0)

print("Averages:", avg)
print("Highest subject:", ["Math", "Science", "English", "History"][np.argmax(avg)])
