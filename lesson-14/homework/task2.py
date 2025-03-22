def power_func(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power_func)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
powers = vectorized_power(bases, exponents)

print("Power results:", powers)
