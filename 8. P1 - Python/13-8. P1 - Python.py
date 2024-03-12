# 13 - Write a program in Python that prints on the screen the numbers from 5 to 15,000.

import sys

def print_range(a: int | float, b: int | float):
   if a >= b:
      raise ValueError(f"unsupported range, {a} -> {b}")
   for i in range(a, b+1):
      print(i)

def main():

   a = 5
   b = 15000
   print_range(a, b)

   return 0


if __name__ == '__main__':
  sys.exit(main())