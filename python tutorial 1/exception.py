x=input("Enter number1: ")
y = input("Enter number2: ") 
try:
  z = int(x)/int(y)

except ZeroDivisionError as e:
  print('Division by zero exception')
  z = None

except TypeError as e:
  print('Type error exception')
  z = None

# handles generic error
except Exception as e:
  # get the exact error type
  print('exception type: ', type(e).__name__)
  
  print('Exception occurred: ', e)
  z = None


print("Division is: ", z)