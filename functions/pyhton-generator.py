def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

# Generators are functions that can pause and resume their execution.
# # When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
#Generators allow you to iterate over data without storing the entire dataset in memory.

#Instead of using return, generators use the yield keyword.

def count_up_to(n):
  count = 1
  while count <= n:
    yield count 
    count += 1

for num in count_up_to(5):
  print(num)


# You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "email"
  yield "tobies"
  yield "linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))


# Generator Methods

# send() Method
# The send() method allows you to send a value to the generator:
def echo_generator():
  while True:
    recieved = yield
    print("recieved:", recieved)

gen = echo_generator()
next(gen)
gen.send("Hello")
gen.send("world")