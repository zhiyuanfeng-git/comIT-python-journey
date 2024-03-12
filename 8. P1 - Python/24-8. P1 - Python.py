# 24 - Make a calculator.

import sys

class Calculator:

    operator_list = ('1','2','3','4')
    symbol_list = ('+','-','x','/')

    __last_result = None
    __is_continue = False

    @staticmethod
    def addition(a: int | float, b: int | float):
        return a + b
    
    @staticmethod
    def subtraction(a: int | float, b: int | float):
        return a - b
    
    @staticmethod
    def multiplication(a: int | float, b: int | float):
        return a * b
        
    @staticmethod
    def division(a: int | float, b: int | float):
        if b == 0:
            print("Error: divided by zero.")
            raise ZeroDivisionError
        return a / b

    @staticmethod
    def is_valid_operator(operator):
        if operator in Calculator.operator_list:
            return True
        return False
    
    @staticmethod
    def get_symbol(operator):
        return Calculator.symbol_list[operator]
    
    @staticmethod
    def is_continue():
        return Calculator.__is_continue
    
    @staticmethod
    def set_continue(is_continue):
        Calculator.__is_continue = is_continue
    
    @staticmethod
    def check_exit(input_str):
        if input_str == 'q':
            return True
        return False
    
    @staticmethod
    def get_last_result():
        return Calculator.__last_result
    
    @staticmethod
    def perform_calculator(operator, *args):
        result = 0
        a = args[0]
        b = args[1]
        match operator:
            case '1':
                Calculator.__last_result = Calculator.addition(a, b)
            case '2':
                Calculator.__last_result = Calculator.subtraction(a, b)
            case '3':
                Calculator.__last_result = Calculator.multiplication(a, b)
            case '4':
                Calculator.__last_result = Calculator.division(a, b)
            case _:
                result = -1
        return result

        
def do_calculate():
    print("Operator:\n- 1 means addition\n- 2 means subtraction\n- 3 means multiplication\n- 4 means division\n- others means exiting the program")

    while True:
        print("Enter q to exit whenever you want to exit")
        if not Calculator.is_continue():
            input_str = input("Please enter first number:")
            if Calculator.check_exit(input_str):
                break
            try:
                input_number = float(input_str)
            except ValueError:
                print("input error.")
            
            a = input_number
        else:
            a = Calculator.get_last_result()


        input_operator = input("Please enter a operator(1:+,2:-,3:*,4:/):")
        if Calculator.check_exit(input_operator):
            break
        if not Calculator.is_valid_operator(input_operator):
            print("operator error.")
            continue
        
        
        input_str = input("Please enter second number:")
        if Calculator.check_exit(input_str):
            break
        try:
            input_number = float(input_str)
        except ValueError:
            print("input error.")
        b = input_number

        Calculator.perform_calculator(input_operator, a, b)

        print(f"The result of {a} {Calculator.get_symbol(int(input_operator)-1)} {b} is : {Calculator.get_last_result()}")

        is_continue = input("Is this a continuous calculation?(Y or N): ")
        if Calculator.check_exit(is_continue):
            break
        if is_continue.lower() == 'y':
            Calculator.set_continue(True)
        else:
            Calculator.set_continue(False)


def main():

   do_calculate()

   return 0


if __name__ == '__main__':
  sys.exit(main())