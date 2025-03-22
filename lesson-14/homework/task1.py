import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = vectorized_conversion(temperatures_f)

print("Temperatures in Celsius:", temperatures_c)
