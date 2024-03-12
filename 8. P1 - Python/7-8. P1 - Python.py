# 7 - Write a program in Python that prints the division of 1234 between 532.

import sys

def division(x: int | float, y: int | float):
   result = 0
   try:
      result = x / y
   except ZeroDivisionError:
      print(f"division by zero!")
   except Exception as e:
      print(e)
   return result

def main():

   x = 1234
   y = 532
   result = division(x, y)
   print(f"The division of {x} and {y} is: {result}")

   return 0


if __name__ == '__main__':
  sys.exit(main())