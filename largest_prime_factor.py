"""
Project Euler Problem 3: https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

References:
    - https://en.wikipedia.org/wiki/Prime_number#Unique_factorization
"""

def largest_prime(n: int = 600851475143) -> int:
    try: 
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or castable to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater than or equal to one.")
    prime = 1
    i = 2 
    while i * i <= n:
        while n % i == 0:
            prime = i
            n //= i
        i += 1
    if n > 1: 
        prime = n
    return int(prime)


if __name__ == "__main__":
    print(f"{largest_prime(10) = }")
    print(f"{largest_prime(25278) = }")
    print(f"{largest_prime(6857) = }")
    print(f"{largest_prime(-6857) = }")
