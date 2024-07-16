# Write a Python function generate_fibanacci(n) to return a list of first n Fibonacci numbers.

def generate_fibanacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return "The list of first",n,"Fibonacci numbers are",fib_sequence
    
print(generate_fibanacci(10))
print(generate_fibanacci(19))
print(generate_fibanacci(16))
print(generate_fibanacci(18))