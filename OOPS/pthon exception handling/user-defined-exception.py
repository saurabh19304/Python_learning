# Steps to Create and Use User-Defined Exceptions
# Define a New Exception Class: Create a new class that inherits from Exception or any of its subclasses.
# Raise the Exception: Use the raise statement to raise the user-defined exception when a specific condition occurs.
# Handle the Exception: Use try-except blocks to handle the user-defined exception.

# Example: In this example, we create a custom exception InvalidAgeError to ensure that age values fall within a valid range (0–120).

class InvalidAgeError(Exception):
  def __init__(self, age , msg="age must be between 0 to 120"):
    self.age = age
    self.msg = msg
    super().__init__(self.msg)  #this calls the parent class for it's method

  def __str__(self):
    return F'{self.age} -> {self.msg}'
  
#use the custom exception in your code 
def set_age(age):
  if age < 0 or age > 120:
    raise InvalidAgeError(age)
  else:
    print(f"Age set to: {age}")

# Handling the exception
try:
 set_age(150) #this will raise the custom exception 

except InvalidAgeError as e:
  print(e)

  
class InvalidAgeError(Exception):
  def __init__(self, age , msg="age must be between 0 to 120"):
    self.age = age
    self.msg = msg
    super().__init__(self.msg)  #this calls the parent class for it's method

  def __str__(self):
    return F'{self.age} -> {self.msg}'
  
#use the custom exception in your code 
def set_age(age):
  if age < 0 or age > 120:
    raise InvalidAgeError(age)
  else:
    print(f"Age set to: {age}")

# Handling the exception
try:
 set_age(150) #this will raise the custom exception 

except InvalidAgeError as e:
  print(e)