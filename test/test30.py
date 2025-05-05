import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title("简单折线图")
plt.xlabel("X 轴")
plt.ylabel("Y 轴")
plt.grid(True)
plt.show()
