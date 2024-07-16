# Write a Python program to check the given number is prime number or not.

def prime(num):
    div = []
    for i in range(2,num):
        if num % i == 0:
            div.append(i)
    if len((div)) == 0:
        print("The entered number ",num," is a prime number")
    else:
        print("The entered number ",num," is not a prime number")
    
prime(28)
prime(17)
prime(15)
prime(11)
prime(19)