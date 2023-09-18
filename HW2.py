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
