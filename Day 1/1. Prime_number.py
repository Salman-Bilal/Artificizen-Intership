"""
Question no. 1: Write a program to check whether a number is prime.

"""

n = 2
if n > 1:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a prime number")    