#!/usr/bin/env python 

def print_fibonacci(length):
    fibonacci_sequence = []  # Initialize an empty list to store the Fibonacci sequence
    
    # Generate Fibonacci sequence up to the specified length
    a, b = 0, 1
    for _ in range(length):
        fibonacci_sequence.append(a)  # Add the current Fibonacci number to the sequence
        a, b = b, a + b  # Calculate the next Fibonacci number
    
    print(fibonacci_sequence)  # Print the Fibonacci sequence
