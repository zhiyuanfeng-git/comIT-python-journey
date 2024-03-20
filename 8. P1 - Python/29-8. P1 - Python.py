# 29 - Write an algorithm and a sub-algorithm. 
# Write two variables with the same name and the compiler does not show error.

import sys

Company_Name = "James Legend Ltd."

def print_jack_company():
   Company_Name = "Jack Shell Ltd."
   print(f"The Jack's company name is {Company_Name}")


def print_companies():
   print(f"The James's company name is : {Company_Name}")
   print_jack_company()

def main():
   print_companies()
   return 0


if __name__ == '__main__':
  sys.exit(main())