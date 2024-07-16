""" Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and
    returns value of the integer num rotated to the right by n positions.
    Assume both the numbers are unsigned. Invoke the function and print the return value.
    Hint: use >> binary operator to shift the bits.
    Example: num=60, n=2 result=15
"""

def right_shift(num, n):
    bits = 32
    n = n % bits
    rotated = (num >> n) | (num << (bits - n))
    rotated = rotated & ((1 << bits) - 1)
    print("The entered number is: ", num)
    print("The entered number after it is rotated by right by ",n," times is ", rotated)
    
right_shift(60, 2)
right_shift(30,3)
right_shift(10,9)