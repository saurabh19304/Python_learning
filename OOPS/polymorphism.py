# Polymorphism allows same method, function or operator to behave differently depending on object it is working with. This makes code more flexible and reusable.

# 1. Compile-time Polymorphism
#not supported in python 

#2. Runtime polymorphism 

class Animal:
  def sound(self):
    return "some generic sound"
  
class Dog(Animal):
  def sound(self):
    return "bark"
  
class Cat(Animal):
  def sound(self):
    return "meow" 
#polymorphism behavior 
animals = [Dog(), Cat(), Animal()]
for animal in animals:
  print(animal.sound())