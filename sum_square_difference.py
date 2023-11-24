"""
Project Euler Problem 6: https://projecteuler.net/problem=6

Sum square difference

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

# square_sum = []
# natural_numbers = []
# for i in range(1, 11):
#     square_sum.append(i ** 2)
#     natural_numbers.append(i)
    

# print(sum(square_sum))
# print(sum(natural_numbers) ** 2)
# print((sum(natural_numbers) ** 2) - sum(square_sum))

def sum_square_difference(n: int = 100) -> int:
    """ Difference between sum of the squares and square of the sum from 1 to n """
    square_of_sum = []
    sum_of_squares = []
    for i in range(1, n + 1):
        square_of_sum.append(i)
        sum_of_squares.append(i ** 2)
    
    return sum(square_of_sum) ** 2 - sum(sum_of_squares)
    

if __name__ == "__main__":
    print(f"{sum_square_difference(20) = }")

