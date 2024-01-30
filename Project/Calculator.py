import math
first_number=float(input("Enter first number: "))
second_number=float(input("Enter second number: "))
Operator=input("Enter operator (+, -, *, /, %, //, **, sqrt): ")


if Operator=="+":
  result=first_number+second_number
  print("Addition is: ",result)
elif Operator=="-":
  result=first_number-second_number
  print("Subtraction is: ",result)
elif Operator=="*":
  result=first_number*second_number
  print("Multiplication is: ",result)
elif Operator=="/":
  if second_number!=0:
    result=first_number/second_number
    print("Division is: ",result)
  else:
    print("Error: Division by zero!")
elif Operator=="%":
  result=first_number%second_number
  print("Modulus is: ",result)
elif Operator=="//":
  if second_number!=0:
    result=first_number//second_number
    print("Floor Division is:",result)
  else:
    print("Error: Division by zero!")
elif Operator=="sqrt":
  if first_number >=0:
    result=math.sqrt(first_number)
    print("Square root of", first_number, "is:", result)
  else:
    print("Error: Cannot calculate square root of a negative number!")
else:
  print("Invalid operator")

print("Thank You For Using The Calculator")
