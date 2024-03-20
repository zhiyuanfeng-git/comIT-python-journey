# ON MODULARIZATION AND VARIABLES SCOPE.
# 3 - WRITE AN ALGORITHM AND SUB ALGORITHM. 
# WRITE TWO VARIABLES WITH THE SAME NAME SO THAT THE COMPILER DOES NOT SHOW AN ERROR.

import sys
import random

CITY_NAME = "CALGARY"

def print_city():
   print(f"The city name is {CITY_NAME}")

def print_random_name():
   CITY_NAME = random.randbytes(5) # CITY_NAME BAD USE CASE
   print(f"The random bytes are {CITY_NAME}")
   print_city()

def main():
   print_random_name()
   return 0


if __name__ == '__main__':
  sys.exit(main())