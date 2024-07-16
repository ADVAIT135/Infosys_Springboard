""" Given a list of integer values, write a Python program to check whether the list contains the same number in adjacent positions.
    Display the count of such adjacent occurrences.

    Sample Input                  Sample Output
    [1,1,5,100,-20,-20,6,0,0]       3
    [10,20,30,40,30,20]             0
    [1,2,2,3,4,4,4,10]              3
"""

def list_ops():
    n = int(input("Enter the number of elements you want to have in the list: "))
    list_a = []
    
    for i in range(1,n+1):
        value = input(f"Enter the value of the {i} term in the list: ")
        list_a.append(value)
        
    count_adjacent_values = 0
    for j in range(len(list_a)-1):
        if list_a[j] == list_a[j+1]:
            count_adjacent_values += 1
    
    print("The number of occurences of same values which are in adjacent positions in list is: ", count_adjacent_values)
    
list_ops()       
        
    
        