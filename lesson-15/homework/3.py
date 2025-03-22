fig, axs = plt.subplots(2, 2, figsize=(10, 8))

x = np.linspace(-2, 2, 100)
x_positive = np.linspace(0, 2, 100)  

axs[0, 0].plot(x, x**3, color="red")
axs[0, 0].set_title("f(x) = x^3")

axs[0, 1].plot(x, np.sin(x), color="blue")
axs[0, 1].set_title("f(x) = sin(x)")

axs[1, 0].plot(x, np.exp(x), color="green")
axs[1, 0].set_title("f(x) = e^x")

axs[1, 1].plot(x_positive, np.log(x_positive + 1), color="purple")
axs[1, 1].set_title("f(x) = log(x+1)")

plt.tight_layout()
plt.show()
