# ON MODULARIZATION AND VARIABLES SCOPE.
# 1-WRITE AN ALGORITHM THAT INVOKES ANOTHER ONE, AND THE INVOKED ONE PRINTS A VALUE.

import sys
import random

def print_value(value):
   print(f"The value of is {value}")

def print_random_value():
   rand = random.random()
   print_value(rand)
   rand_bytes = random.randbytes(10)
   print_value(rand_bytes)
   rand_int = random.randint(10,10000)
   print_value(rand_int)
   rand_range = random.randrange(100000,200000,1000)
   print_value(rand_range)

def main():
   print_random_value()
   return 0


if __name__ == '__main__':
  sys.exit(main())