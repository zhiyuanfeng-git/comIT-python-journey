# ON MODULARIZATION AND VARIABLES SCOPE.
# 2-WRITE AN ALGORITHM THAT INVOKES ANOTHER ONE TO BE CALLED "ADD”, THAT RECEIVES TWO NUMBERS. 
# THE "ADD" ALGORITHM MUST ADD THE PARAMETERS. 
# THE INVOKING ALGORITHM SHOULD RECEIVE BACK THAT VALUE AND SHOW IT ON SCREEN.

import sys
import random

def add(a, b):
   return a + b

def print_addition(a, b):
   result = add(a, b)
   print(f"The result of {a} + {b} is {result}")

def main():
   a = random.randint(100,3000)
   b = random.randint(400,8000)
   print_addition(a, b)
   return 0


if __name__ == '__main__':
  sys.exit(main())