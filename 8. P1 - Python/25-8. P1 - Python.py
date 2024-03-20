# 25 - Calculate the salary increase for a group of employees of a company 
# considering the following criteria: 
# If the salary is less than $ 1,000.00: Increase 15% 
# If the salary is greater than or equal to $ 1,000.00: Increase 12% 
# The program must do The following: 
# - Save the new salaries in the arrangement 
# - Calculate the payroll 
# - Print the salaries from the settlement

import sys

DIVIDING_SALARY = 1000
RATE_UNDER = 1.15
RATE_ABOVE = 1.12

class NegativeException(Exception):
   """ Cannot calculate the negative salary."""
   pass

def keep_decimal(value, keep=2):
   return round(value, keep)

def calculate_salary_increase(salary):
   if salary < 0:
      raise NegativeException
   
   if salary < DIVIDING_SALARY:
      return keep_decimal(salary * RATE_UNDER)
   
   return keep_decimal(salary * RATE_ABOVE)

def calculate_new_salaries(salaries):
   arrange_list = []
   payroll = 0
   for salary in salaries:
      new_salary = calculate_salary_increase(salary)
      arrange_list.append(new_salary)
      payroll += new_salary

   return arrange_list, payroll

def main():
   salaries = [100,300,1100,3000]
   new_salaries, payroll = calculate_new_salaries(salaries)
   print(f"new_salaries: {new_salaries}")
   print(f"payroll: {payroll}")
   return 0


if __name__ == '__main__':
  sys.exit(main())