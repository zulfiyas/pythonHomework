import math

class Vector: 
  def __init__(self, *components):
    self.components = tuple(components)

  def __repr__(self):
    return f"Vector{self.components}"
  
  def __add__(self, other):
    if not isinstance(other, Vector) or len(self.components) != len(other.components):
      raise ValueError("Vectors must have the same dimentions")
    return Vector(*(a + b for a, b in zip(self.components, other.components)))
  
  def __sub__(self, other):
    if not isinstance(other, Vector) or len(self.components) != len(other.components):
      raise ValueError("Vectors must have the same dimentions")
    return Vector(*(a - b for a, b in zip(self.components, other.components)))
  
  def __mul__(self, other):
    if isinstance(other, (int, float)):  # Scalar multiplication
        return Vector(*(a * other for a in self.components))
    elif isinstance(other, Vector):  # Dot product
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))  # <-- Move return outside!
    else:
        raise TypeError("Unsupported operand type, expected int, float, or Vector")

    
  def __rmul__(self, other):
    return self. __mul__(other)

  def magnitude(self):
    return math.sqrt(sum(a **2 for a in self.components))
  
  def normalize(self):
    mag = self.magnitude()
    if mag ==0:
      raise ValueError ("can't normalize zero vector")
    return Vector(*(a / mag for a in self.components))

#the codes below are just to check my work
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v1 + v2)
print("v1 - v2:", v1 - v2)
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())
print("2 * v1:", 2.0 * v1)
print("Dot product of v1 and v2:", v1 * v2)