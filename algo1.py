#Limutos, Gerald P.
#BSIT 2-2
#DSA 01 HA1: algo1.py

#3. Create a python script that will compare two entered numbers.
#3.1. User enters first number.
#3.2. User enters second number.
#3.3. If the first number is less than, greater than, 
#or equal the second number, a message is displayed.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if a > b:
    print("Your first number is greater than the second number.")
elif a < b:
    print("Your first number is less than the second number.")
else:
    print("Your first number is equal to the second number.")

