# 22 - Make the program in Python such that given as a worker's salary, apply a 15% increase if your salary is less than $ 1000 and 12% otherwise. Print the new salary of the worker. Fact: SUE (variable of real type that represents the salary of the worker).

import sys

BASE_SALARY = 1000
HIGHER_RATE = 1.15
LOWER_RATE = 1.12

def calculate_salary(original_salary):
   if original_salary < BASE_SALARY:
      return original_salary * HIGHER_RATE
   
   return original_salary * LOWER_RATE



def main():

   salary = float(input("Please enter the worker's salary:"))
   new_salary = calculate_salary(salary)
   print(f"The new salary of the work is {new_salary}")

   return 0


if __name__ == '__main__':
  sys.exit(main())