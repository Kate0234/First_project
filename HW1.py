
# Task 1

number =int(input("Enter any three numbers on your keyboard. The sum will be displayed on the screen."))
n1= number // 100
n2= number // 10 % 10
n3= number % 10
result = n1 + n2 + n3
print(f"n1: {n1} n2: {n2} n3: {n3} ")
print(f"Result: {result}")

# Task 2


print("This formula will help to calculate an area of a rhombus. Enter the length of each side.")
s1 =int(input("s1:"))
s2 =int(input("s2:"))
result = s1*s2 / 2
print(f"Result: {result}")

# Task3

number =int(input("Enter any four numbers on your keyboard. The multiplication result will be displayed on the screen."))
n1= number % 10
n2= number // 10 % 10
n3= number // 100 % 10
n4= number // 1000
result = n1 * n2 * n3 * n4
print(f"n1: {n1} n2:{n2} n3:{n3} n4:{n4})")
print(f"Result: {result}")