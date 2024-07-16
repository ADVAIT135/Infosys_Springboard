""" Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments
    and returns True if the given pair of numbers are amicable numbers else return false.
    Invoke the function and based on return value print the numbers are amicable numbers or not.
 
    num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of num1 is equal to num2 and
    sum of all the proper devisors of num2 (except num1 itself) is equal to num1.

    Example: 220 and 284 are amicable numbers as
    Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284
    Proper divisors of 284 are 1, 2, 4, 71, 142 whose sum is 220
"""

def check_amicable_numbers(num1,num2):
    sum1 = 0
    sum2 = 0
    for i in range(1,num1):
        if num1%i == 0:
            sum1 += i
    for i in range(1,num2):
        if num2%i == 0:
            sum2 += i
    print('num1: ',num1, end = ' ')
    print('num2: ',num2)
    print('sum1: ',sum1, end = ' ')
    print('sum2: ',sum2)
    if (sum1 == num2) and (sum2 == num1):
        print("The given pair of numbers ",num1, "and", num2, "are amicable numbers")
    else:
        print("The given pair of numbers ",num1, "and", num2, "are not amicable numbers")
        
check_amicable_numbers(220, 284)
check_amicable_numbers(520, 850)        