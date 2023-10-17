

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

#text = ("As illustrated by this infographic, the share of writers working for the absolute "
        #"minimum set by the MBA grew significantly from the 2013-14 season to the 2021-22 season. "
        #"In total, the share of writers at the minimum level rose from 33 to 49 percent.")
#print(len([i for i in text if i.isdigit()]))
#print(len([i for i in text if i.isalpha()]))



#Lesson 4. Task 2


#message = ("After 146 days of striking, the Writers Guild of America (WGA), the union representing Hollywood writers,"
           #"has announced that it had reached a tentative agreement to end the negotiation impasse which,"
           #"coupled with an actors strike, has brought the industry to a standstill.")
#count = 0
#for letter in message:
    #if letter == "a":
        #count += 1



#Lesson 4. Task 3

#text = "Hi! I want to request funds."
#text = text.replace("funds","vacation")
#print(text)


#Lesson 4. Task 4

#message = "Our first chart illustrates the following."
#print(message[2]) #1
#print(message[-2]) #2
#print(message[:5]) #3
#print(message[0:40]) #4
#print(message[1:42:2]) #5
#print(message[0:42:2]) #6
#print(message[::-1]) #7
#print(message[::2]) #8
#print(len(message)) #9

#Lesson 5. Task 1

#nums = [ 1, 7, 4, -5, -11, 3, 76, -34, 6, 2, 9 ]
#print(nums)

# сума негативних чисел

#sum_of_negative = 0
#for i in nums:
    #if i < 0:
        #sum_of_negative = sum_of_negative + i
#print("Sum of negatives:", sum_of_negative)

# сума парних чисел

#sum_of_paired = 0
#for i in nums:
    #if i % 2 == 0:
        #sum_of_paired = sum_of_paired + i
#print("Sum of paired:", sum_of_paired)


# сума непарних чисел

#sum_of_unpaired = 0
#for i in nums:
    #if i % 2 > 0:
        #sum_of_unpaired = sum_of_unpaired + i
    #continue
#print("Sum of unpaired:", sum_of_unpaired)


# добуток елементів з кратними індексами 3

# v1
#nums = [ 1, 7, 4, -5, -11, 3, 76, -34, 6, 2, 9 ]
#a = -5
#b = 76
#c = 2
#result = a * b * c
#print(f"Result of multiplication:", result)

# v2

import random

#numbers = [random.randint(-100, 100) for _ in range(20)]
#print("List of numbers:", numbers)


#product_of_multiples_of_3 = 1
#for i in range(0, len(numbers), 3):
    #product_of_multiples_of_3 *= numbers[i]

#print("Product of numbers with indices multiples of 3:", product_of_multiples_of_3)

# добуток елементів між мінімальним та максимальним елементом

#min_value = min(nums)
#max_value = max(nums)
#result = min(nums) * max(nums)
#print(f"Result (min_value * max_value): {result}")

# суму елементів, що знаходяться між першим та останнім позитивними елементами

#list = [-1, 1, 3, -4, 4, -5, -6, 9, -5, -9, ]
#p1 = p2 = 0
#for p1, a in enumerate(list):
    #if a > 0:
        #break  # определить индекс первого положительного элемента
#for p2, a in enumerate(reversed(list)):
    #if a > 0:
        #break  # определить индекс последнего положительного элемента
#s = sum(list[p1+1: -p2-1])  # взять сумму между индексами
#print(s)

# Lesson 5. Task 2

#Є список цілих, заповнений випадковими числами.
#На підставі даних цього масиву потрібно:
#Створити список цілих, що містить лише парні числа з першого списку;
#Створити список цілих, що містить лише непарні числа з першого списку;
#Створити список цілих, що містить лише негативні числа з першого списку;
#Створити список цілих, що містить лише позитивні числа з першого списку.

#from random import sample
#list = sample(range(-10, 11), 20)
#print(list)

#paired_list = [i for i in list if i % 2 == 0]
#unpaired_list = [j for j in list if j % 2]
#negative_list = [i for i in list if i < 0]
#positive_list = [i for i in list if i >= 0]

#print(f"Paired list:", paired_list)
#print(f"Unpaired list:", unpaired_list)
#print(f"Negative list:", negative_list)
#print(f"Positive list:", positive_list)


# Lesson 7. Task 1

# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.


numbers_1 = [random.randint(1, 10) for _ in range(5)]
print(numbers_1)

def mult():
    n1 = a
    n2 = b
    n3 = c
    n4 = d
    n5 = e
    return










# Task 2.

# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.





# Task 3.

# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.




# Task 4.

# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.





# Task 5.

# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.






# Task 6.

#Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.