## Algorithms

1. What is the difference between the contents of a varible and its name?
   * In python, a variable name is a reference or identifier used to access the value stored in memory.
   * The contents of a variable refer to the actual data or value stored in memory.
   * Unlike C++, where variables can directly store the value or the memory address, the contents of a variable actually store the reference to an object in memory in Python.
   * When you assign a value to a variable in Python, you are creating an object in memory,and the variable holds a reference to the memory location where the object is stored.
   * If you declare a variable like 'x', not to assign any value to it, it refers to the 'None' object.'None' is a built-in constant in Python that represents the absence of a value of a null value.

2. What is the difference between a variable,a constant and a literal? What do they have in common?
   * Variables,constants,and literals are all used to represent and manipulate values in a program, they are all contributing to the functionality and structure of a program.
   * But designed for different purpose,they have some differences.
     * a variable is a named storage location that can change its value during execution.
     * a constant is a fixed value that does not change during execution.
     * a literal is a notation representing a specific value directly in the source code,like hard-code.
3. What is an expression?
   * In programming, an expression is a combination of values,variables,operators,and function calls that results in a single value. Expressions are used to represent computations or operations.
7. Write an algorithms to read a number and say if it is positive or negative.
   ```
    num = read_io()
    if num is greater than 0, then
        print("{0} is positive.",num)
    else if num is less than 0, then
        print("{0} is negative.",num)
    else
        print("The number you inputed is zero.")
   ```
9. Write an algorithm that determines if a number is even.
   ```
   num = 4
   if num modulo 2 is equal to 0, then
        print("{0} is even",num)
   else
        print("{0} is odd",num)
   ```
10.  Make an algorithm to read two real numbers and print the largest of them.
   ```
   num1 = read_io()
   num2 = read_io()
   if num1 is greater than num2, then
        print("{0} is the largest number",num1)
   else num2 is greater than num1, then
        print("{0} is the largest number",num2)
   else
        print("Both numbers are equal.")
   ```
11. Given the radius of a circle, make an algorithm to calculate the value of the area.
   ```
   radius = 18
   area = π * radius ^ 2
   ```
12. Write an algorithm that determines if an "N" number is divisible by another "M".
   ```
   if N modulo M is equal to 0,then
        print("The {0} number is divisible by {1} number",N,M)
   else
        print("The {0} number is not divisible by {1} number",N,M)
   ```
13. Write an algorithm to translate a time expressed in days, hours, minutes and seconds to time expressed in seconds.
   ```
   seconds = (days * 24 * 60 * 60) + (hours * 60 *60) + (minutes * 60) + seconds
   ```
14.  We are being informed of three environmental temperature values, and we are asked to develop an algorithm to calculate and report the sum and average of these values.
   ```
   temperature1 = read_io()
   temperature2 = read_io()
   temperature3 = read_io()
   sum_temperature = temperature1 + temperature2 + temperature3
   average = sum_temperature / 3
   print("The average of these values is {0}",average)
   ```
15.  For our brave ones: translate a time expressed in seconds to a time expressed in days, hours, minutes and
seconds.
   ```
    constant ONE_MINUTE_SECONDS = 60
    constant ONE_DAY_SECONDS = 24 * 60 * ONE_MINUTE_SECONDS
    constant ONE_HOUR_SECONDS = 60 * ONE_MINUTE_SECONDS
    time_in_seconds = read_seconds()
    days = time_in_seconds / ONE_DAY_SECONDS
    remaining_seconds = time_in_seconds % ONE_DAY_SECONDS
    hours = remaining_seconds / ONE_HOUR_SECONDS
    remaining_seconds = remaining_seconds % ONE_HOUR_SECONDS
    minutes = remaining_seconds / ONE_MINUTE_SECONDS
    seconds = remaining_seconds % ONE_MINUTE_SECONDS
   ```
