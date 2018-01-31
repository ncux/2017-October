def exponent(a, b):
    if b == 0:
        return 1  # base case
    else:
        return (a * a**(b-1))

y = exponent(2, 3)
print(y)

z = exponent(5, 3)
print(z)


