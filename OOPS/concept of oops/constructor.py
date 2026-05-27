# The method __new__ is the constructor that creates a new instance of the class while __init__ is the initializer that sets up the instance's attributes after creation

# __new__ Method
# This method is responsible for creating a new instance of a class. It allocates memory and returns the new object. It is called before __init__.

class className:
  def __new__(cls, parameters):
    instance = super(className, cls).__new__(cls)
    return instance  
  #new returns new object while the init does not retuen anything 
  def __init__(self, parameters):
    self.atribute = value 
#init is used to initialize the object 


  