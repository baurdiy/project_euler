"""
Project Euler Problem 2: https://projecteuler.net/problem=2

Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

References:
    - https://en.wikipedia.org/wiki/Fibonacci_number
"""

def sum_even_fibonacci_numbers(n: int = 4000000) -> int:
    fib1 = 1 
    fib2 = 2
    sum_even = 0

    while fib2 <= n:
        if fib2 % 2 == 0: 
            sum_even += fib2 # sum = sum + fib2
        fib1, fib2 = fib2, fib1 + fib2 
    
    return sum_even
print("Sum of even numbers in Fibonacci: ")
print(sum_even_fibonacci_numbers())
print("End")

