"""
An organization has decided to provide salary hike to its employees based on their job level.
Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:

Job level   Hike Percentage (applicable on current salary)

3            15
4            7
5            5

In case of invalid job level, consider hike percentage to be 0.
Given the current salary and job level, write a Python program to find and display the new salary of an employee.
"""

def new_sal(curr_sal,job_level):
    if job_level == 3:
        print("New Salary, for current salary: ",curr_sal, "and job level ", job_level ,"is: ",
              curr_sal + (curr_sal * 0.15)," with a hike of ", (curr_sal * 0.15))
    elif job_level == 4:
        print("New Salary, for current salary: ",curr_sal, "and job level ", job_level ,"is: ",
              curr_sal + (curr_sal * 0.07)," with a hike of ", (curr_sal * 0.07))
    elif job_level == 5:
        print("New Salary, for current salary: ",curr_sal, "and job level ", job_level ,"is: ",
              curr_sal + (curr_sal * 0.05)," with a hike of ", (curr_sal * 0.05))
    else:
        print("Invalid Job level")
        print("New Salary, for current salary: ",curr_sal, "and job level ", job_level ,"is: ",
              curr_sal + (curr_sal * 0.0), "with no hike")
        
new_sal(15000, 3)
new_sal(15000, 5)
new_sal(15000, 4)
new_sal(15000, 8)
    