"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_3_5(n):
    
    l = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)

    return sum(l)

if __name__ == "__main__":
    print(multiples_3_5(10))

