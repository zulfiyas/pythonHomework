x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, c="blue", marker="o", alpha=0.6)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot of Random Points")
plt.grid(True)

plt.show()
