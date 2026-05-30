# Exception Handling allows a program to handle unexpected errors during execution in a controlled way, instead of crashing abruptly. It enables programs to detect errors, manage them properly and continue execution wherever possible.

# Handles runtime errors such as invalid input, file not found, division by zero and type mismatches that occur during program execution.
# Helps improve program reliability by ensuring the application does not terminate unexpectedly when an error occurs.

n = 10
try:
  res = n / 0
except ZeroDivisionError:
  print("Can't be diveded by zero!")

# ry:
#       # Code 
# except SomeException:
#       # Code 
# else:
#      # Code 
# finally:
#     # Code 

# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.


try:
  n = 0
  res = 100 / n

except ZeroDivisionError:
  print("You can not devide by zero!")

except ValueError:
  print("Enter a valid number!")

else:
  print("Result is ", res)

finally:
  print("Execution complete.")


# #  Multiple Exceptions
# We can catch multiple exceptions in a single block if we need to handle them in the same way or we can separate them if different types of exceptions require different handling.

a = ["10", "twenty", 30]

try:
  # 'twenty' cannot be converted to int
  total = int(a[0]) + int(a[1])

except (ValueError, TypeError) as e:
  print("Error", e)

except IndexError:
  print("Index out of range.")


# # Raise an Exception
# We raise an exception using the raise keyword followed by an instance of the exception class that we want to trigger. We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python's built-in Exception class.

def set(age):
  if age < 0:
    raise ValueError("age can not be negative")
  print(f"age set to {age}")

 
try:
  set(-5)
except ValueError as e:
  print(e) 