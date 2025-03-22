data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, color="blue", alpha=0.7)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normal Distribution")

plt.show()
