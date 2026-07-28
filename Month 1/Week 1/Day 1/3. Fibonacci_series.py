"""
Question: 3: Print the Fibonacci series up to n terms.

"""
n = int(input("Enter a number: "))

previous, current = 0, 1

if n > 0:
    for i in range(n):
        print(f" {previous} ", end= " ")
        previous, current = current, previous + current
