""" Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false.
    Invoke the function and based on return value print the output.
    Example: num=12321 output: Given number is a palindrome, num=12345 output: Given number is not a palindrome
"""

def is_palidrome(num):
    if str(num) == str(num)[::-1]:
        print("The entered number ",num," is a palindrome number.")
    else:
        print("The entered number ",num," is not a palindrome number.")

is_palidrome(12321)
is_palidrome(12345)
is_palidrome(3435343)
is_palidrome(3435543)