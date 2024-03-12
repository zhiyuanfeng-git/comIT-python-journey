# 14 - Write a program in Python that prints 200 times the word "hello". Note: in the source code that you write you must only enter once the word "hello".

import sys

# approach first
def print_simple_count(value, count = 1):
   print(value * count)

# approach second
def print_with_sep(value, count = 1, sep=','):
   value_list = [value]
   print(*count*(value_list), sep=sep)

# approach third
def print_loop(value: str, count: int = 1):
   for i in range(1, count + 1):
      print(value)

def main():

   value = "hello"
   count = 200
   print_simple_count(value, count)
   print_with_sep(value, count)
   print_loop(value, count)

   return 0


if __name__ == '__main__':
  sys.exit(main())