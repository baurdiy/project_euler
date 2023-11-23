"""
Project Euler Problem 5: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?

References:
    - https://en.wiktionary.org/wiki/evenly_divisible
"""


# def solution(n: int = 20) -> int:
#     """
#     Returns the smallest positive number that is evenly divisible (divisible
#     with no remainder) by all of the numbers from 1 to n.

#     >>> solution(10)
#     2520
#     >>> solution(15)
#     360360
#     >>> solution(22)
#     232792560
#     >>> solution(3.4)
#     6
#     >>> solution(0)
#     Traceback (most recent call last):
#         ...
#     ValueError: Parameter n must be greater than or equal to one.
#     >>> solution(-17)
#     Traceback (most recent call last):
#         ...
#     ValueError: Parameter n must be greater than or equal to one.
#     >>> solution([])
#     Traceback (most recent call last):
#         ...
#     TypeError: Parameter n must be int or castable to int.
#     >>> solution("asd")
#     Traceback (most recent call last):
#         ...
#     TypeError: Parameter n must be int or castable to int.
#     """

#     try:
#         n = int(n)
#     except (TypeError, ValueError):
#         raise TypeError("Parameter n must be int or castable to int.")
#     if n <= 0:
#         raise ValueError("Parameter n must be greater than or equal to one.")
#     i = 0
#     while 1:
#         i += n * (n - 1)
#         nfound = 0
#         for j in range(2, n):
#             if i % j != 0:
#                 nfound = 1
#                 break
#         if nfound == 0:
#             if i == 0:
#                 i = 1
#             return i
#     return None


# if __name__ == "__main__":
#     print(f"{solution(20) = }")

# def solution(n: int = 20) -> int:
#     try:
#         n = int(n)
#     except (TypeError, ValueError):
#         raise TypeError("Parameter n must be int or castable to int.")
#     if n <= 0:
#         raise ValueError("Parameter n must be greater than or equal to one.")

#     i = 0
#     iterations = 0

#     while 1:
#         i += n * (n - 1)
#         nfound = 0

#         for j in range(2, n):
#             if i % j != 0:
#                 nfound = 1
#                 break

#         if nfound == 0:
#             if i == 0:
#                 i = 1
#             return i

#         # Print values for the first 5 iterations
#         if iterations < 5:
#             print(f"Iteration {iterations + 1}: i = {i}, nfound = {nfound}")

#         iterations += 1


# if __name__ == "__main__":
#     print(f"{solution() = }")


# for j in range(2, 20):
#     print(f"j = {j} = {232792560/j}")
      
         

def smallest_multiple(n: int = 20) -> int: 
    i = 0
    while 1: #create an infinte loop, stopping point is if functions return
        i += n * (n - 1) # i = i + n * (n-1)
        nfound = 0 
        for j in range(2, n): # iterates through 2 to n
            if i % j != 0: # looks for number that will divide to all the numbers from 2 to n with 0 remainder, and if finds nfound value will remain 0 and next block code will execute, otherwise everytime when it finds remainder not equal to 0 it will update the nfound to 1 and break out the for loop. 
                nfound = 1
                break
        # if nfound value didn't change and it is still 0 it will check this condition
        if nfound == 0:
            if i == 0: # if i is equal to 0 then it will return 1, it is in case for n was equal to 0 that case you will get i as an 1 
                i = 1 
            return i # otherwise i equal to this => i += n * (n - 1) =>> i = i + n * (n-1), whenever this return will execute while loop will stop otherwise it will be continue, SO THIS IS THE STOPPING CASE FOR WHILE LOOP
    return None # The return None statement is placed outside the loop, and it will only be reached if the loop condition (while 1:) is never satisfied, which would mean the loop runs indefinitely. However, the loop is designed to exit when nfound == 0 is true, and the return i statement is executed.

if __name__ == "__main__":
    print(f"{smallest_multiple(0) = }")

