from abc import ABC, abstractmethod
#ABC(abstract base class)

class Greet(ABC):
  @abstractmethod
  def say_hello(self):
    pass #abstract method

class English(Greet):
  def say_hello(self):
    return "hello!"
  
g = English()
print(g.say_hello())


# Abstract Properties
# Abstract properties work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract using @abstractmethod. Subclasses must implement these properties.

from abc import ABC, abstractmethod

class Animal(ABC):
  @property
  @abstractmethod
  def species(self):
    pass #abstract property must be implemented by the subclasses 

class Dog(Animal):
  @property
  def species(self):
    return "canine"

dog = Dog()
print(dog.species)


#Abstract classes cannot be instantiated directly. This is because they contain one or more abstract methods or properties that lack implementations. Attempting to instantiate an abstract class results in a TypeError.
  
