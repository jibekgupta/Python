n=int(input("Enter any number to find the Factorial: "))
fact=1
for i in range(n,0,-1):
    fact*=i
print("The factorial of",n,"number is:",fact)
