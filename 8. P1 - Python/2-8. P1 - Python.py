# 2 - Write a program in Python that prints an int number, for example 273, or 597.

import sys

def main():
   value = 273
   print(f"The int number is: {value}")
   
   value = 597
   print(f"The int number is: {value}")
   return 0


if __name__ == '__main__':
  sys.exit(main())