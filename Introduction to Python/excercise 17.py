""" Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.
    Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
"""

def proper_divisors(num):
    div_list = []
    for i in range(1,num):
        if num%i == 0:
            div_list.append(i)
    print("The list of the proper divisors of the number ",num," is ",div_list)
    
proper_divisors(220)
proper_divisors(250)
proper_divisors(137)
proper_divisors(148)
