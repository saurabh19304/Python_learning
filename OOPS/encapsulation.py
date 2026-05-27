# Encapsulation is one of the core concepts of Object Oriented Programming (OOP).

# The idea of encapsulation is to bind the data members and methods into a single unit.
# Helps in better maintainability, readability and usability as we do not need to explicitly pass data members to member methods
# Helps maintain data integrity by allowing validation and control over the values assigned to variables.
# It helps in achieving abstraction. A class can hide the implementation part and discloses only the functionalities required by other classes which allows later changes to representations or implementations without impacting the codes that uses this class.


#public and #protected members 
class Employee:
  def __init__(self, name, age):
    self.name = name #public
    self._age = age #protecred defined with one _

class SubEmployee(Employee):
  def show_age(self):
    print("age:", self._age) #accesible in the subclass

emp = SubEmployee("Ross", 30)
print(emp.name)
emp.show_age() #protectes accessed through subclass 

#private members
#can only be accessed through the class methods

class Employee:
  def  __init__(self):
    self.__salary = 5000 #private attribute

  def get_salary(self):  #getter
    return self.__salary
  
  def set_salary(self, amount): #setter
    if amount > 0:
      self.__salary = amount
    else:
      print("invalid salary amount!")

emp = Employee()
print(emp.get_salary()) #access salary using getter 

emp.set_salary(60000)
print(emp.get_salary())

   

  