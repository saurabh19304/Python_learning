#Lambda functions are small anonymous functions, meaning they do not have a defined name. These are small, short-lived functions used to pass simple logic to another function.

#contain only one expression 
#result of that function is retuened automatically 

a = 'saurabh tiwari'
upper = lambda x: x.upper()  
print(upper(a))

#2. Using with List Comprehension
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())