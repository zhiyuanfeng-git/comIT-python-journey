# 19 - Write a Python program that does the following: declare a variable N of type int, a variable A of type double and a variable C of type char and assign to each one a value. The following screen displays:
# The value of each variable. The sum of N + A. And A - N

import sys


def main():

   N: int = 1
   A: float = 3.2
   C: str = '4'
   print(f"N is {N}")
   print(f"A is {A}")
   print(f"C is {C}")
   print(f"The sum of {N} + {A} is {N + A}")
   print(f"The sum of {A} - {N} is {A - N}")

   return 0


if __name__ == '__main__':
  sys.exit(main())