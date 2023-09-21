#Task 1-1
print("Enter 3 digit below to define the number with the highest value.")
a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
print(mx)

print("Enter 3 digits below to define the number with the lowest value.")
a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
mn = a
if b < a:
    mn = b
if c < a:
    mn = c
print(mn)

print("Enter 3 digit below to define the arithmetic value.")
a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
result = ( a + b + c) / 3
print(f"Result: {result}")

meter = int(input("Enter the number of meters to be converted into inches and yards:"))
n = int(input("Press the number to make a choice: 1. Convert into inches, 2. Convert into yards. "))
if n == 1:
    print ( meter * 36.37 )
elif n == 2:
    print ( meter * 1.09 )
else:
    print("Wrong choice!")
