""""
Write a Python program to find the sum of digits of a given number.

Example: Sum of digits of the number 123 will be 6

Note: Initialize the number with various values and test your program.
"""

def sum_num(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)
    
sum_num(123)
sum_num(345)
sum_num(959)
