# 23 - Make a program that prints the 10 multiplication tables.

import sys

# approach first
def multiplication_tables(value):
   for i in range(1, value + 1):
      for j in range(1, value + 1):
            print(i * j)
      print("\n")

# approach second
def print_multiplication_tables(value):
   count_asterisk = value * 5 + 7
   print('-'*count_asterisk)
   for i in range(1, value + 1):
      print(f"{'\033[0m'}|{'\033[91m'}{i:2}{'\033[0m'} : ", end="")
      for j in range(1, value + 1):
            print(f"|{i*j:3}", end=" ")
      print("|")
      print('-'*count_asterisk)

   print('|     ', end="")
   for i in range(1, value + 1):
      print(f"{'\033[0m'}|{'\033[91m'}{i:3}{'\033[0m'}", end=" ")
   print("|")
   print('-'*count_asterisk)


def main():

   value = 10
   multiplication_tables(value)

   print_multiplication_tables(value)

   return 0


if __name__ == '__main__':
  sys.exit(main())