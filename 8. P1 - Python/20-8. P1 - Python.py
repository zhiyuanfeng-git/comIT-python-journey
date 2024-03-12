# 20 - Write a Python program that declares an integer variable B and assign it a value. It then displays a message indicating whether the value of B is positive or negative. We will consider 0 as positive.
# If for example B = 1 the output will be 1 is positive. If for example B = -1 the output will be: -1 is negative.

import sys

def print_positive_negative(x: int):
   if x >= 0:
      print(f"The integer {x} is a positive integer")
   else:
      print(f"The integer {x} is a negative integer")


def main():

   B:int = 1
   print_positive_negative(B)
   
   B = -1
   print_positive_negative(B)

   return 0


if __name__ == '__main__':
  sys.exit(main())