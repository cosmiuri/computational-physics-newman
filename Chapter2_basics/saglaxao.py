def great_divisor(m,n):
    if n == 0:
        return m
    else:
        return great_divisor(n,m%n)

print(great_divisor(108,192))