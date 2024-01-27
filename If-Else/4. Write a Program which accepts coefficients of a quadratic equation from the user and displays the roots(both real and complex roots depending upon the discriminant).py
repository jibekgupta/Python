import math

def quadratic_roots(a,b,c):
    discriminant =b**2 - 4*a*c

    if discriminant >0:
        root1=(-b + math.sqrt(discriminant)) / (2*a)
        root2=(-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are real and distinct")
        print("Root 1: ",root1)
        print("Root 2: ",root2)

    elif discriminant==0:
        root = -b/(2*a)
        print("The roots are real and equal:")
        print("Root 1 and Root 2:",root)

    else:
        real_part = -b /(2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        print("The roots are complex:")
        print("Root 1:", real_part, "+", imag_part, "i")
        print("Root 2:", real_part, "-", imag_part, "i")

#Input coefficients from the user
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))

#Call the function to calculate and display roots
quadratic_roots(a,b,c)

