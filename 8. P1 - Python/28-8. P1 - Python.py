# 28 - Write an algorithm that calls another name "add", which receives 2 numbers. 
# The summation algorithm must add its parameters. 
# The algorithm you invoke must receive that value and display it on the screen.

import sys

def add(a, b):
   return a + b

def ask_addition():
   a = int(input("Please enter the first numeric:"))
   b = int(input("Please enter the second numeric: "))
   result = add(a, b)
   print(f"The result of {a} + {b} is: {result}")


def main():
   ask_addition()
   return 0


if __name__ == '__main__':
  sys.exit(main())