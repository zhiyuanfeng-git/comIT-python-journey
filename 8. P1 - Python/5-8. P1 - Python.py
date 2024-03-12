# 5 - Write a program in Python that prints the subtraction of 1234 and 532.

import sys

def subtraction(x: int | float, y: int | float):
   return x - y

def main():
   x = 1234
   y = 532
   result = subtraction(x, y)
   print(f"The subtraction of {x} and {y} is: {result}")
   
   return 0


if __name__ == '__main__':
  sys.exit(main())