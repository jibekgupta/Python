year=int(input("Enter any year: "))
if year %4 ==0:
    if year%100!=0 or year %400 ==0 :
        print("The year ", year, "is a Leap Year.")
    else:
        print("The year ", year, "is not a Leap Year." )
else:
    print("The year ", year, "is not a Leap Year." )
        


