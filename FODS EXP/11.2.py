import matplotlib.pyplot as plt

m = [1, 2, 3, 4]
s = [1000, 2000, 1500, 3000]

plt.scatter(m, s)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
