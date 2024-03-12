# 4 - Write a program in Python that prints on the screen the sum of 1234 and 532.

import sys

def addition(x: int | float, y: int | float):
   return x + y

def main():
   x = 1234
   y = 532
   result = addition(x, y)
   print(f"The sum of {x} and {y} is: {result}")
   
   return 0


if __name__ == '__main__':
  sys.exit(main())