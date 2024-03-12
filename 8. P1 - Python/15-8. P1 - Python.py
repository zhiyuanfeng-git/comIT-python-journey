# 15 - Exercise: Write a program in Python that prints the squares of the first 30 natural numbers on the screen.

import sys

# approach first
def calculate_squares(value):
   for i in range(1, value + 1):
      print(f"The squares of {i} is {i ** 2}")

# approach second
def recursion_squares(value):
   if value <= 0:
      return
   recursion_squares( value - 1)
   print(f"The squares of {value} is {value ** 2}")


# approach third
def generate_squares(value):
   for i in range(1, value + 1):
      yield i, i ** 2

def print_squares(value):
   for i, result in generate_squares(value):
      print(f"The squares of {i} is {result}")


def main():

   value = 30
   calculate_squares(value)
   print("*" * 30)
   recursion_squares(value)
   print("*" * 60)
   print_squares(value)
   
   return 0


if __name__ == '__main__':
  sys.exit(main())