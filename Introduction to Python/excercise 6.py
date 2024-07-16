# Write a Python program to print first n Fibonacci numbers.

def fib(n):
    if n < 0:
        print('Invalid Input. Number must be greater than 0')
    elif n == 0:
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(9))
print(fib(11))
print(fib(14))
print(fib(4))