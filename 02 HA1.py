#Limutos, Gerald P.
#BSIT 2-2 
#DSA 02 HA1

def compare_numbers(num1, num2):
    if num1 < num2:
        print(f"{num1} is less than {num2}.")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")

def get_and_compare_numbers():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        compare_numbers (num1, num2)
    except ValueError:
        print("Please make sure your inputs are numbers.")

if __name__=="__main__":
    get_and_compare_numbers()