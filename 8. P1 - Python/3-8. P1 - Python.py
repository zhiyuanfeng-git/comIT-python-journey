# 3 - Write a program in Python that prints a float number, for example the 5.3, or the 7.5.

import sys


def main():
   value = 5.3
   print(f"The float number is: {value}")

   value = 7.5
   print(f"The float number is: {value}")
   return 0


if __name__ == '__main__':
  sys.exit(main())