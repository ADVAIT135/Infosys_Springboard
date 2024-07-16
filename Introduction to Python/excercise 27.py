""" Given a list of numbers, write a Python function to return the list of prime numbers present in it.
    Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]
"""
def prime_num_list():
    count = int(input("Enter the total number of integers you want to have in the list: "))
    num_list = []
    prime_num_list = []
    for i in range(count):
        num = int(input(f"Enter the {i+1} number of the list: "))
        num_list.append(num)
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in num_list:
        if is_prime(num):
            prime_num_list.append(num)
    print("From the given list of numbers:", num_list, "the list of prime numbers are", prime_num_list)

prime_num_list()
