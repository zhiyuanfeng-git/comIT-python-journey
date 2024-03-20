# 26 - Make a program that asks for the salary of N workers 
# (first you must ask how many workers there are) and print the one with the highest salary.

import sys

def handle_salaries(count):
   highest_salary = 0
   for i in range(1, count+1):
      try:
         salary = float(input(f"Please input the salary(totally {count} times):"))
         if salary > highest_salary:
            highest_salary = salary
      except ValueError:
         raise

   return highest_salary

def salary_process():
   try:
      worker_count = int(input("Input an integer representing the amount of workers: "))
      highest_salary = handle_salaries(worker_count)
      print(f"The highest salary is: {highest_salary}")
   except ValueError:
      print("Please enter the numeric.")



def main():
   salary_process()
   return 0


if __name__ == '__main__':
  sys.exit(main())