# Write a Python function, find_sum() that accepts an integer n and returns the sum of first n numbers.
# Invoke the function and display the sum of first n numbers.

def find_sum(n):
    sum_num = 0
    for i in range(1,n+1):
        sum_num += i
    print("The entered number is ",n,"and the sum of first ",n," numbers is ",sum_num)
    
find_sum(5)
find_sum(4)
find_sum(8)
find_sum(11)