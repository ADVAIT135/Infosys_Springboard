# Write a Python program to find and display the maximum of three given numbers.

def max_three(num):
    num_arr = []
    for i in str(num):
        num_arr.append(int(i))
    print(max(num_arr)) 
            
max_three(123)
max_three(758)
max_three(959)