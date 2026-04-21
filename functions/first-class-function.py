#following GFG instead of the docs from now on 22-04-26

#1. Assigning Functions to Variables

def msg(name):
  return f"Hello, {name}!"
# Assigning the function to a variable
f = msg
# Calling the function using the variable
print(f("Emma"))

#2. Passing Functions as Arguments
def msg(name):
  return f"Hello, {name}!"

def fun1(fun2, name):
  return fun2(name)
# Passing the msg function as an argument
print(fun1(msg, "alex")) 


#3. Returning Functions from Other Functions
def fun1(msg):
  def fun2():
    return f"Message: {msg}"
  return fun2
# Getting the inner function
func = fun1("Hello , World!")
print(func())


#4. Storing Functions in Data Structures
def add(x, y):
  return x + y
def subtract(x,y):
  return x - y
# Storing functions in a dictionary
d = {
  "add": add,
  "subtract": subtract
}
# Calling functions from the dictionary
print(d["add"](5,4))
print(d["subtract"](5,3))