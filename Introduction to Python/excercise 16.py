""" Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
    The ticket number should be generated as airline:src:dest:number where
    Consider AL1 as the value for airline
    src and dest should be the first three characters of the source and destination cities.
    number should be auto-generated starting from 101
    The program should return the list of ticket numbers of last five passengers.
    Note: If passenger count is less than 5, then return the list of all generated ticket numbers.
"""

def pass_tickets():
    num = int(input("Enter the number of passengers travelling: "))
    dest_list = []
    src_list = []
    ticket_num_list = []
    for i in range(1,num+1):
        src = input(f"Enter the first three initials of the source city for the {i} passenger : ")
        if len(src) != 3:
            print("Please enter only the first three initials of the source city")
        else:
            src_list.append(src.upper())
        dest = input(f"Enter the first three initials of the destination city for the {i} passenger :")
        if len(dest) != 3:
            print("Please enter only the first three initials of the destination city")
        else:
            dest_list.append(dest.upper())
    for i in range(1,num+1):
        ticket = "10" + str(i)
        ticket_num_list.append(int(ticket))
    print("The following are the ticket details for the given number of passengers")
    for i in range(0,num):
        ticket_details = "AL1:"+src_list[i]+":"+dest_list[i]+":"+str(ticket_num_list[i])
        print(ticket_details)
        
pass_tickets()     