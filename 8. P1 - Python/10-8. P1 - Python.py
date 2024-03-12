# 10 - Write a program in Python that prints on the screen the numbers from 1 to 10,000.

import sys

def generator_numbers(a, b):
   for i in range(a, b):
      yield i

def print_range_by_generator(a, b):
   for result in generator_numbers(a, b):
      print(result)


def main():

   a = 1
   b = 10000
   print_range_by_generator(a, b)

   return 0


if __name__ == '__main__':
  sys.exit(main())