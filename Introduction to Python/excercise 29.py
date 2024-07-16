""" Write a python function, find_pairs_of_numbers(num_list,n) which accepts a list of positive integers with no repetitions and
    returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.
    Example: num_list=[1, 2, 7, 4, 5, 6, 0, 3], n=6 output:3
            num_list= [3, 4, 1, 8, 5, 9, 0, 6], n=9 output:4
"""
def find_pairs_of_numbers(num_list, n):
    count = 0
    num_dict = {}
    
    for num in num_list:
        target = n - num
        if target in num_dict and num_dict[target] > 0:
            count += 1
            num_dict[target] -= 1
        else:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
    
    return count

num_list1 = [1, 2, 7, 4, 5, 6, 0, 3]
n1 = 6
output1 = find_pairs_of_numbers(num_list1, n1)
print(output1) 

num_list2 = [3, 4, 1, 8, 5, 9, 0, 6]
n2 = 9
output2 = find_pairs_of_numbers(num_list2, n2)
print(output2) 

