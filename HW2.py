print("Let's calculate the maximum value of three numbers. Enter numbers and you will see the number with the highest value on the screen.")
a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
mx = a
if b > a > c:
    mx = b
elif c > a > b:
    mx = c

print(mx)

print("Let's define the number with the minimum value.")
a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
mn = a