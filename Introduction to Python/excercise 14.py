""" Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True if the number is strong number
    else false. Invoke the function and based on return value print the number is strong number or not.

    A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.

    Example:145 is strong number as
    1!=1
    4!=24
    5!=120
    Sum of all these is 145
"""

def check_strong_num(num):
    digits = []
    sum_digits = 0
    for i in str(num):
        digits.append(i)
    for i in digits:
        factorial = 1
        for j in range (1, int(i) + 1):
            factorial = factorial * j
        sum_digits += factorial
    if sum_digits == num:
        print("The entered number ",num," is a strong number.")
    else:
        print("The entered number ",num," is a not strong number.")
            
check_strong_num(145)
check_strong_num(40585)
check_strong_num(153)    