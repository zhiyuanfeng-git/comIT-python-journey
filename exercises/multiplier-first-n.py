# purpose: make an algorithm that calculates the multiplier of the first "N" natural numbers.

def calculate_multiplier(n):
    if n < 0:
        return -1
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def test_multiplier():
    print("Please input an integer:")
    n = int(input())
    result = calculate_multiplier(n)
    print(f"The multiplier of the first {n} natural numbers is : {result}")

#test_multiplier()

def multiplier_recursive(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * multiplier_recursive(n-1)
    
def test_recursive():
    print("Please input an integer:")
    n = int(input())
    result = multiplier_recursive(n)
    print(f"The multiplier of the first {n} natural numbers is : {result}")

#test_recursive()
    
import math
def multiplier_factorial(n):
    if n < 0:
        return -1
    return math.factorial(n)

def test_factorial():
    print("Please input an integer:")
    n = int(input())
    result = multiplier_recursive(n)
    print(f"The multiplier of the first {n} natural numbers is : {result}")

#test_factorial()