def factorial(n):
    if n <= 1:       # base case
        return 1
    else:
        return n * factorial(n-1)

y = factorial(10)
print(y)
