# Write a Python program to find the number of characters present the given string.

def find_num_char():
    user_string = input('Enter you string in which you want to find the number of characters: ')
    char_sum_space = 0
    char_sum = 0
    for i in user_string:
        if not i.isdigit():
            char_sum_space += 1
        else:
            char_sum_space += 0
    for i in user_string:
        if (not i.isdigit()) and (not i.isspace()):
            char_sum += 1
        else:
            char_sum += 0
    print("The total number of characters (including space) present in the string '",user_string,"' is :  ",char_sum_space)
    print("The total number of characters (excluding space) present in the string '",user_string,"' is :  ",char_sum)
    
find_num_char()