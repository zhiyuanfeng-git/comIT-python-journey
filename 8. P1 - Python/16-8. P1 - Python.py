# 16 - Write a program in Python that reads an integer from the keyboard and makes the sum of the next 100 numbers, showing the result on screen.

import sys

# approach first
def addition_range(start: int, end: int):
   result = 0
   for i in range(start, start + end):
      result += i
   return result

# approach second
def recursion_addition_range(number: int, end: int, count: int = 0, total: int = 0):
   if count == end:
      return total
   return recursion_addition_range(number + 1, end, count + 1, total + number)

def call_fun(number, end, func):
   result = func(number, end)
   print(f"The sum of the next {end} numbers from {number} is {result}")

def main():

   number = int(input("Please enter a number:"))
   end = 100
   call_fun(number, end, addition_range)
   call_fun(number, end, recursion_addition_range)

   return 0


if __name__ == '__main__':
  sys.exit(main())