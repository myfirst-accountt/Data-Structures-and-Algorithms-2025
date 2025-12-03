#Limutos, Gerald P.
#BSIT 2-2 
#DSA 02 HA1

def find_sum(n):
    if n <= 0:
        return 0
    else:
        return n + find_sum(n-1)
    
n = int(input("Please enter a number: "))
print(f"The sum of the first {n} integers is {find_sum(n)}.")