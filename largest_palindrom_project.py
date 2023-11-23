"""
Project Euler Problem 4: https://projecteuler.net/problem=4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

References:
    - https://en.wikipedia.org/wiki/Palindromic_number
"""

def largest_palindrome_number(n):
    answer = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product_string = str(i * j)
            if product_string == product_string[::-1] and i * j < n:
                answer = max(answer, i * j)
    return answer
    

if __name__ == "__main__":
    print(largest_palindrome_number(20000))

