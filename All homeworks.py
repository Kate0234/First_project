

# Task 1-1

#number =int(input("Enter any three numbers on your keyboard. The sum will be displayed on the screen."))
#n1= number // 100
#n2= number // 10 % 10
#n3= number % 10
#result = n1 + n2 + n3
#print(f"n1: {n1} n2: {n2} n3: {n3} ")
#print(f"Result: {result}")

# Task 1-2


#print("This formula will help to calculate an area of a rhombus. Enter the length of each side.")
#s1 =int(input("s1:"))
#s2 =int(input("s2:"))
#result = s1*s2 / 2
#print(f"Result: {result}")

# Task1-3

#number =int(input("Enter any four numbers on your keyboard. The multiplication result will be displayed on the screen."))
#n1= number % 10
#n2= number // 10 % 10
#n3= number // 100 % 10
#n4= number // 1000
#result = n1 * n2 * n3 * n4
#print(f"n1: {n1} n2:{n2} n3:{n3} n4:{n4})")
#print(f"Result: {result}")

#Task 1-1
#print("Enter 3 digit below to define the number with the highest value.")
#a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
#mx = a
#if b > mx:
#   mx = b
#if c > mx:
#    mx = c
#print(mx)


# print("Enter 3 digit below to define the number with the lowest value.")
# a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
# mn = a
# if b < a:
#     mn = b
# if c < a:
#     mn = c
# print(mn)


# print("Enter 3 digit below to define the arithmetic value.")
# a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
# result = ( a + b + c) / 3
# print(f"Result: {result}")



#Task 1-1
# print("Enter 3 digit below to define the number with the highest value.")
# a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
# mx = a
# if b > mx:
#     mx = b
# if c > mx:
#     mx = c
# print(mx)

# print("Enter 3 digits below to define the number with the lowest value.")
# a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
# mn = a
# if b < a:
#     mn = b
# if c < a:
#     mn = c
# print(mn)

# print("Enter 3 digit below to define the arithmetic value.")
# a, b, c = int(input("Enter the first number:")), int(input("Enter the second number:")), int(input("Enter the third number:")),
# result = ( a + b + c) / 3
# print(f"Result: {result}")

# meter = int(input("Enter the number of meters to be converted into inches and yards:"))
# n = int(input("Press the number to make a choice: 1. Convert into inches, 2. Convert into yards. "))
# if n == 1:
#     print ( meter * 36.37 )
# elif n == 2:
#     print ( meter * 1.09 )
# else:
#     print("Wrong choice!")

#test comment to try commit and push

#Lesson 3. Task 1

#print("Lesson 3. Task 1")
#try:
    #print("Enter the number that corresponds to the day of the week: 1 - Monday, 2 - Thursday. 3 - Wednesday, 4 - Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday")
    #user_select = int(input("Enter number: " ))

    #match user_select:
        #case 1:
           #print("Monday")
        #case 2:
            #print("Tuesday")
        #case 3:
           #print("Wednesday")
        #case 4:
            #print("Thursday")
        #case 5:
            #print("Friday")
        #case 6:
           #print("Saturday")
        #case 7:
            #print("Sunday")
        #case 8:
            #print("Incorrect value! Choose number from 1 to 7!")
#except Exception as e:
    #print(f"Error: {e}. Enter number!")

#Lesson 3. Task 2

#print("Lesson 3. Task 2")
#while True:
    #try:
        #a, b = int(input(" Enter first number (a):")), int(input("Enter second number (b):"))
        #data = a, b
        #if a == b:
           #print("Numbers equal")
        #elif a > b or b > a:
          #print(sorted(data))
        #break
        #except ValueError:
        #print("Enter number!")
    #continue

#Lesson 3. Task 3

#print("Lesson 3. Task 3")
#print("Enter two numbers to perform further calculations.")
#n1, n2 = int(input("Enter n1:")), int(input("Enter n2:"))
#print("1.Sum 2. Exclude 3. Multiply 4. Divide")
#user_select = int(input("Enter number of option you want to perform:"))

#try:
    #match user_select:
             #case 1:
                 #result = n1 + n2
                 #print(f"Result: {result}")
             #case 2:
                    #result = n1 - n2
                    #print(f"Result: {result}")
             #case 3:
                  #if n1 > 0 and n2 > 0 :
                      #result = n1 * n2
                      #print(f"Result: {result}")
                #elif n1 == 0:
                      #result = 0
                      #print(f"Result: {result}")
                #elif n2 == 0:
                      #result = 0
                      #print(f"Result: {result}")
             #case 4:
                  #while True:
                      #try:
                            #if n1 > 0 and n2 > 0:
                              #result = n1 / n2
                              #print(f"Result: {result}")
                            #elif n1 == 0:
                              #result = n1 / n2
                              #print(f"Result: {result}")
                            #elif n2 == 0:
                                #result = n1 / n2
                            #except Exception as e:
                             #print(f"Error: {e}. You cannot divide into 0!")
                      #finally:
    #print("End of calculation")

#Lesson 4. Task 1

text = ("As illustrated by this infographic, the share of writers working for the absolute "
        "minimum set by the MBA grew significantly from the 2013-14 season to the 2021-22 season. "
        "In total, the share of writers at the minimum level rose from 33 to 49 percent.")
print(len([i for i in text if i.isdigit()]))
print(len([i for i in text if i.isalpha()]))



#Lesson 4. Task 2


message = ("After 146 days of striking, the Writers Guild of America (WGA), the union representing Hollywood writers,"
           "has announced that it had reached a tentative agreement to end the negotiation impasse which,"
           "coupled with an actors strike, has brought the industry to a standstill.")
count = 0
for letter in message:
    if letter == "a":
        count += 1
        print(count)


#Lesson 4. Task 3

text = "Hi! I want to request funds."
text = text.replace("funds","vacation")
print(text)


#Lesson 4. Task 4

message = "Our first chart illustrates the following."
print(message[2]) #1
print(message[-2]) #2
print(message[:5]) #3
print(message[0:40]) #4
print(message[1:42:2]) #5
print(message[0:42:2]) #6
print(message[::-1]) #7
#print(message[::, 2]) #8
print(len(message)) #9








