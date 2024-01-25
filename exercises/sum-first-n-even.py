# purpos: make an algorithm that sums the first "N" even numbers.

def calculate_sum_even(n):
    if n < 0:
        return -1
    
    even_number = 2
    sum = 0
    for i in range(1,n+1):
        sum += even_number
        even_number += 2

    return sum

def test_sum_even():
    print("Please input an integer:")
    n = int(input())
    result = calculate_sum_even(n)
    print(f"The sum of the first {n} even numbers is {result}")

#test_sum_even()
    
def calculate_sum_even2(n):
    if n < 0:
        return -1
    
    even_number = 2
    sum = 0
    count = 1
    while count <= n:
        sum += even_number
        even_number += 2
        count += 1

    return sum

def test_sum_even2():
    print("Please input an integer:")
    n = int(input())
    result = calculate_sum_even2(n)
    print(f"The sum of the first {n} even numbers is {result}")

#test_sum_even2()
    
def calculate_sum_even3(n):
    if n < 0:
        return -1
    
    sum = 0
    for i in range(n):
        sum += 2 * (i + 1)

    return sum

def test_sum_even3():
    print("Please input an integer:")
    n = int(input())
    result = calculate_sum_even3(n)
    print(f"The sum of the first {n} even numbers is {result}")

#test_sum_even3()
    
def calculate_sum_even4(n):
    if n < 0:
        return -1
    
    sum = n * (n + 1)
    return sum

def test_sum_even4():
    print("Please input an integer:")
    n = int(input())
    result = calculate_sum_even4(n)
    print(f"The sum of the first {n} even numbers is {result}")

#test_sum_even4()