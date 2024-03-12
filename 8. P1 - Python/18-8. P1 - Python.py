# 18 - Write a program in Python that reads two numbers on the keyboard and say which is the largest and which is the smallest.

import sys

def compare_two_number(a: int | float, b: int | float) -> int:
   if a > b:
      return 1
   elif b > a:
      return 2
   
   return 0


def main():

   a = int(input("Please input number a:"))
   b = int(input("Please input number b:"))

   result = compare_two_number(a,b)
   
   if result == 1:
      print(f"The largest number is {a} and the smallest is {b}")
   elif result == 2:
      print(f"The largest number is {b} and the smallest is {a}")
   else:
      print(f"They are equal.")

   return 0


if __name__ == '__main__':
  sys.exit(main())