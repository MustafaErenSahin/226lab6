import math

answer = 0

def factorial(x):
    if x == 1 or x == 0:
        return 1
    return x * factorial(x - 1)

single = lambda x, n : (-1 ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

def sine_x(x, n):
    if n == 50:
        return single(x, n)
    return single(x, n) + sine_x(x, n + 1)

def sum(n):
    """calculates summation of 1/n to 1"""
    global answer
    if(n == 0):
        return 0
    answer = answer + (1 / n)
    sum(n - 1)

print(factorial(3))
print(sine_x(1, 5))
sum(3)
print(answer)
