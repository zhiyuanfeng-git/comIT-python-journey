# 6 - Write a program in Python that prints the multiplication of 1234 and 532 on screen.

import sys

def multiplication(x: int | float, y: int | float):
   return x * y

def main():
   
   x = 1234
   y = 532
   result = multiplication(x, y)
   print(f"The multiplication of {x} and {y} is: {result}")

   return 0


if __name__ == '__main__':
  sys.exit(main())