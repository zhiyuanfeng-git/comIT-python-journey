# 17 - Write a program in Python that converts from canadian dollars to US dollars. You will receive a decimal number corresponding to the amount in CAD and will answer with the corresponding amount in US dollars. Take the quotation of the dollar today.

import sys

DEFAULT_RATE = 0.74

def get_exchange_rate():
   rate = DEFAULT_RATE
   return rate

def convert_dollars(amount_cad: float):
   amount_us = amount_cad * get_exchange_rate()
   return amount_us


def main():

   amount_cad = 10
   amount_us = convert_dollars(amount_cad)
   print(f"The canadian dollars {amount_cad} equals to us dollars {amount_us}")
   print(f"The corresponding to the amount in US dollars for {amount_cad} CAD is: {amount_us}")

   return 0


if __name__ == '__main__':
  sys.exit(main())