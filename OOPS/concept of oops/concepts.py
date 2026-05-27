# A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances)

class Dog:
  species = "canine" #class attribute

  def __init__ (self, name, age): #init is a constructor that runs automatically when new object is created ,used to initialize object data 
    self.name = name #instance attribute 
    self.age = age #self refers to the current object 

#__str__ method allows us to define a custom string representation of an object. By default, when we print an object or convert it to a string using str(), Python uses the default implementation, which returns a string like <__main__.ClassName object at 0x00000123>.
  def __str__(self):
    return f"{self.name} is {self.age} years old."


#Objects
# An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:

# State: represented by the attributes and reflects the properties of an object.
# Behavior: represented by the methods of an object and reflects the response of an object to other objects.
# Identity: gives a unique name to an object and enables one object to interact with other objects.

#cresting an object of the dog class
dog1 = Dog("Buddy", 3)
print(dog1.name)
print(dog1.species)