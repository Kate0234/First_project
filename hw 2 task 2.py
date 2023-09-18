# Task 1-4
meter = int(input("Enter the number of meters to be be converted into inches and yards:"))
n = int(input("Press the number to make a choice: 1. Convert into inches, 2. Convert into yards. "))
if n == 1:
    print ( meter * 36.37 )
elif n == 2:
    print ( meter * 1.09 )
else:
    print("Wrong choice!")

#comment for another commit