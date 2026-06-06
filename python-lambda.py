# In Python, a lambda function is an anonymous function meaning it is defined without a name. Unlike regular functions defined using def keyword, lambda functions are created using lambda keyword

# They are useful for writing small, simple functions in a concise way, especially when you need a function temporarily.

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))