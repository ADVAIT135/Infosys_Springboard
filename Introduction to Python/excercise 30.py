""" The python function, find_average() given below, is written to accept a list of marks and return the average marks.
    On execution, the program is resulting in an error.
    
    def find_average(mark_list):
          total=0
          for i in range(0, len(mark_list)):
                   total+=mark_list1[i]
          marks_avg=total/len(mark_list)
          return marks_avg
        m_list=[1,2,3,4]
    print("Average marks:", find_average(m_list))
    
    1: Add code to handle the exception occurring in the code.
    2: Make the necessary correction in the program to remove the error.
    3: Make the following changes in the code, execute, observe the results. Add code to handle the errors occurring in each case.
    Case – 1: Initialize m_list as ["1",2,3,4]
    Case – 2: Initialize m_list as given below
    mark1="A"
    mark1=int("A")
    m_list=[mark1,2,3,4]
    Case – 3: Initialize m_list as []
    Case – 4: Make the following change in the for loop statement
    for i in range(0, len(mark_list)+1):
"""

def find_average(mark_list):
    try:
        total = 0
        if len(mark_list) == 0:
            return 0  # Return 0 if mark_list is empty

        for i in range(0, len(mark_list)):
            total += mark_list[i]
        
        marks_avg = total / len(mark_list)
        return marks_avg
    
    except TypeError as e:
        print(f"TypeError occurred: {e}")
        return -1  # Return -1 to indicate error in case of TypeError
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
        return 0  # Return 0 if mark_list is empty and division by zero error occurs

# Case 1: Initialize m_list as ["1", 2, 3, 4]
m_list = ["1", 2, 3, 4]
print("Case 1 - Average marks:", find_average(m_list))

# Case 2: Initialize m_list as mark1="A"; mark1=int("A"); m_list=[mark1, 2, 3, 4]
mark1 = "A"
try:
    mark1 = int("A")
except ValueError as e:
    print(f"ValueError occurred: {e}")
m_list = [mark1, 2, 3, 4]
print("Case 2 - Average marks:", find_average(m_list))

# Case 3: Initialize m_list as []
m_list = []
print("Case 3 - Average marks:", find_average(m_list))

# Case 4: Change in the for loop statement to range(0, len(mark_list)+1)
m_list = [1, 2, 3, 4]
print("Case 4 - Average marks:", find_average(m_list))















