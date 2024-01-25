number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter another number"))
    # YOUDO.  use input function and int to set number2
except ValueError:
  print("You did not give an interger")
    


try:
    value = number1/number2
    print("The answer is, value")
 

except ZeroDivisionError:
    print("Your provided 0 and 0 is not divisible")  
    

    
