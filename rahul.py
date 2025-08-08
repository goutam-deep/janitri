# for  row in range(10):
#     for col in range(10):
#         if col<=10//2 or row>=10//2:
#             print(" ",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# def factrol(num:int =0):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num * factrol(num-1)
# print(factrol(4))


# def tri_recurton(k:int):
#     if (k>0):
#         result=k+tri_recurton(k-1)
#         print(result)
#     else:
#         result=0
#         return result
# print("\n\nrecursion exmpale result")
# tri_recurton(10)

# def febonaci (num):
#     if num == 1:
#         return 0 
#     elif num == 2 or num == 3:
#         return 1
#     else:
#          return febonaci (num-1) + (num-2)
# print(febonaci(9)) 


# def febonaci (num):
#     if num == 1:
#         return 0
#     elif num == 2 or num == 3:
#         return 1
#     else:
#           return febonaci (num-1) + (num-2)
# print(febonaci(9)) 

        

# class car:
#     print("object is created")
#     wheels = 4
#     windows = 4
#     mirror = 1

#     def speed(self):
#         print("300") 

# car()

# print(car())
# print(car)


# obj1 = car()
# print(obj1)
# print(obj1.wheels)
# print(wheels)
###########LCM NUMBER#######
'''a = int(input("Enate a fast number:"))
b = int(input("Enater a second number:"))
num_max = max(a,b)

while True:
    if num_max % a == 0 and num_max % b == 0 :
        lcm_= num_max
        break
    num_max += 1

print(f"the LCM of {a} and {b} is {lcm_}")'''


# ########HCF Number#####
# a = int(input("Enter a fist Number:"))
# b = int(input("Enter a secend Number:"))
# c = int(input("Enter a therd number:"))
# min_num = min(a,b,c)

# for i in range(min_num,0,-1):
#     if a % i == 0 and b % i == 0 and c % i == 0:
#         hcf = i
#         break

# print(f"The HCF of {a} and {b} and {c} is {hcf}")


# def is_prime(num):
#     if num < 2:
#         return False

#     for i in range(2, int(num**0,5) + 1):
#         if num % i == 0 :
#             return False
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number. ")

# else:
#     print(f"{num} is not a prime number.

# number = [1,2,-4,3,-5,-6,8,7,10]
# positive_number_count = 0
# for num in number:
#     if num > 0:
#         positive_number_count +=1
# print(f"final count of positiv number is:{positive_number_count}")

# user_input=int(input("Enter a number to sum of even number:"))

# sum_even = 0
# for i in range(1,user_input+1):
#     if i % 2 == 0 :
#         sum_even +=1
# print(f"sum of even number is:{sum_even}")

# number = 4
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(number,"x",i,'=',number * i)


# input_str= "python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str
# print(reversed_str)


# def is_preme(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n ** 0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# print(is_preme(11))
# # print(is_preme
# num = int(input("Enter a number:"))

# if(num % 2) == 0:
#     print ("0 is even number". format(num))
# else:
#     print("0 is odd number".format(num))    


# try:
#     num = int(input("Enter a number: "))  # User input
#     result = 10 / num  # May cause ZeroDivisionError
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")  # Handling division by zero
# except ValueError:
#     print("Error: Invalid input! Please enter a number.")  # Handling invalid input
# else:
#     print("No errors occurred!")  # Executes if no exception
#
# num = 12 

# if num % 2 == 0:
#     print("it is an even number")
# else:
#     print("it is an odd number")




# num = 16

# if num % 2 == 0:
#     print("it is an even num")
# else:
#     print("it is an odd num")


# num = 60

# if num % 2 == 0:
#     print(" it is an even num")
# else:
#     print(" it is an odd num"


# class baik2:
#     def sound (self):
#         print("booo")
# class baik1 (baik2) :
#         def model (self):
#             print("rc 350")

# b1 = baik1()
# b1.model()
# b1.sound()
    
# class vehicle :
#     def start(self):
#         print("vehicle start")
# class car(vehicle):
#     def drive(self):
#         print("car is driving")
# c = car()
# c.start()
# c.drive()
# class Dog:
#     def sound(self):
#         print("bow bow")
# class cat:
#     def sound(self):
#         print("Meow")
# for animal in (Dog(),cat()):
#     animal.sound()

# i = 1
# while i <= 10 :
#     print(i)
#     i += 1

# i = 1
# while i <= 10 :
#     if i % 2 == 0 :
#         print(i)
#     i += 1
# for i in range (1,21,2):
    # print(i)
# i = 1
# while i <= 20:
    # print("out",i) 
    # i += 1
# squares =[]
# for x in range(1,6):
    # squares.append(x**2)
# print(squares)
# squares =[x**2 for x in range(1,6)]
# print(squares)
# evens = [x for x in range(1,11) if x % 2 == 0]
# print(evens)
# for i in range(1,11):
    # if i % 2 == 0:
        # print(i)
# def factorial(n,fact=1):
    # if n == 0:

# from random import randint

# chr(randint(65,90)) + chr(randint(67,122))  
# import math
# def is_strong_number(num):
#     oringal_num = num
#     sum_of_factorials = 0

#     while num > 0:
#         digit = num % 10
#         sum_of_factorials += math.factorial(digit) 
#         num //=10
#     return sum_of_factorials == oringal_num
# number = int(input("enter a number:"))
# if is_strong_number(number):
#     print(f"{number} is astrong number.")
# else:
#     print(f"{number} is NOT a strong number.")

# def fibonacci():
#     a,b =0,1
#     while True:
#         yield a
#         a,b=b,a+b
# f1=fibonacci()
# for f1 in range(1,11):
#     print(f1)
print("HH")