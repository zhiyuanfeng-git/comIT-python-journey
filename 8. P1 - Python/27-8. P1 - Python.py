# 27 - Write an algorithm that calls another, and the call prints a value.

import sys

def print_to_console(value):
   print(f"The value is: {value}")

def print_numeric():
   value = int(input("Please enter a numeric: "))
   print_to_console(value)

def main():
   print_numeric()
   return 0


if __name__ == '__main__':
  sys.exit(main())