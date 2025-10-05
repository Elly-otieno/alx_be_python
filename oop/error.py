'''
try:
  # Code that might raise an exception
except ExceptionType:
  # Code to handle the exception
else:
  # Code that executes if no exception occurs
finally:
  # Code that always executes, regardless of exceptions
'''


# use the raise statement to explicitly raise an exception when encountering an error condition within your code
def divide(x,y):
    if y == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    return x / y
