import matplotlib.pyplot as plt

m = ['Jan', 'Feb', 'Mar', 'Apr']
s = [1000, 2000, 1500, 3000]

plt.plot(m, s, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
