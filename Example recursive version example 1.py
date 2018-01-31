def recursiveSum(n):
    if n == 1:
        return 1  # base case
    else:
        return recursiveSum(n-1) + n

x = 10
y = recursiveSum(x)
print(y)

