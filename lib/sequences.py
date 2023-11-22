#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        result = []
    elif length == 1:
        result = [0]
    elif length == 2:
        result = [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, length):
            next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fib)
        result = fibonacci_sequence
    
    print(result) 
    return result if length > 0 else "[]" 

