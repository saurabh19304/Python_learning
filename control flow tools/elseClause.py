#find prime number

for n in range(2,10):
  for x in range(2,n):
    if n % x == 0:
      print(n, "equals" ,x, 'to', n//x)
      break
  else:
    print(n,'is the prime number')


#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)