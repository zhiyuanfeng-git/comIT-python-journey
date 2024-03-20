# 30 - Write a program that asks for a numerical password and allows three attempts. 
# If the user enters the correct password, it shows "Correct!" And run any program, 
# after the message. Otherwise the program should display "Wrong password". 
# Then finish the program immediately.

import sys
import random

ATTEMPTS_COUNT = 3

def is_correct(password):
   value = random.random()   
   if value >= 0.5:
      return False
   return False

def ask_password():
   password = int(input("Please enter the password: "))
   return password

def enter_program():
   print("You are in the program.")

def try_handle_password():
   correct_pwd = None
   for i in range(1, ATTEMPTS_COUNT+1):
      password = ask_password()
      if is_correct(password):
         correct_pwd = password
         break
      else:
         if i <= ATTEMPTS_COUNT:
            print(f"Please enter the correct password({ATTEMPTS_COUNT - i} times left)")
   
   if correct_pwd is not None:
      enter_program()
   else:
      print("The program will exit.")

def main():
   try_handle_password()
   return 0


if __name__ == '__main__':
  sys.exit(main())