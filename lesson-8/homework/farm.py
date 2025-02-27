class Animal:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species
  
  def eat(self):
    print(f"{self.name} is eating")
  
  def sleep(self):
    print(f"{self.sleep} is sleeping")
  
  def cry(self):
    print(f"{self.cry} is crying")
  
  def play(self):
    print(f"{self.play} is playing")
  
  def __repr__(self):
    return f"{self.species} named {self.name}, Age {self.age}"

class Cow(Animal):

  def __init__(self, name, age, milk_amount):
    super().__init__(name, age, "Cow")
    self.milk_amount = milk_amount
  def milk(self):
    print(f"{self.name} gives {self.milk_amount} L of milk each day")
  def __sound__(self):
    print(f"{self.name} says 'Moo-moo'")
  
class Chicken(Animal):
  def __init__(self, name, age, eggs_amount):
    super().__init__(name, age, "Chicken")
    self.eggs_amount = eggs_amount
  def lay_eggs(self):
    print(f"{self.name} lays {self.eggs_amount} eggs each day")
  def __sound__(self):
    print(f"{self.name} says 'Quu- quu'")

class Sheep(Animal):
  def __init__(self, name, age, wool_amount):
    super(). __init__(name, age, "Sheep")
    self.wool_amount = wool_amount
  def give_wool(self):
    print(f"{self.name} gives {self.wool_amount} kg of wool each month")
  def __sound__(self):
    print(f"{self.name} says 'Baa-baa'")

#using these values to output example

# Creating farm animals
cow1 = Cow("Sigir", 5, 10)
chicken1 = Chicken("Tovuq", 2, 5)
sheep1 = Sheep("Qoy", 4, 3)

# Performing actions
print(cow1)
cow1.eat()
cow1.milk()
cow1.cry()

print("\n" + str(chicken1))
chicken1.sleep()
chicken1.lay_eggs()
chicken1.__sound__()

print("\n" + str(sheep1))
sheep1.eat()
sheep1.give_wool()
sheep1.__sound__()