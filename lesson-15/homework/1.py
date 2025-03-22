import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = x**2 - 4*x + 4

plt.plot(x, y, label="f(x) = x^2 - 4x + 4", color="blue")

plt.xlabel("x values")  
plt.ylabel("f(x) values")  
plt.title("Plot of f(x) = x^2 - 4x + 4")  
plt.legend()  
plt.grid(True)  

plt.show()
