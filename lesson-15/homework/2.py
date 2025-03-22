x = np.linspace(0, 2*np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, linestyle='-', marker='o', color='r', label="sin(x)")

plt.plot(x, y_cos, linestyle='--', marker='s', color='b', label="cos(x)")

plt.xlabel("x values")
plt.ylabel("Function values")
plt.title("Sine and Cosine Functions")
plt.legend()
plt.grid(True)

plt.show()
