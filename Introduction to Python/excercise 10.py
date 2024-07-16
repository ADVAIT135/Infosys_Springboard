# Write a Python function factorial(num) which returns the factorial of a given number.

def fact_num(num):
    factorial = 1
    if num < 0:
        print("The entered number is less than 0, cannot find factorial of negative numbers")
    elif num == 0:
        print("The factorial of the entered number ",num, " is 1")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        print("The factorial of the entered number ",num," is ", factorial)

fact_num(0)
fact_num(3)
fact_num(5)
fact_num(9)