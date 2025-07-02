def factorial (n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

def catalan (n):

    if n == 0:
        return 1
    else:
        return (4*n-2)/(n+1)*catalan(n-1)

print(catalan(100))

def great_divisor(m,n):
    if n == 0:
        return m
    else:
        return great_divisor(m,n%m)

print(great_divisor(108,192))

