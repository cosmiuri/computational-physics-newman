def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f


def binomial(n,k):
    if k > n or k == 0:
        bin_coef = 1
    else:
        bin_coef = factorial(n) / (factorial(k) * factorial(n - k))

    return int(bin_coef)

print(binomial(10,6))

def pascal(rows):
    triangle = []
    for n in range(rows+1):
        rows = []
        for k in range(n+1):
            rows.append(binomial(n,k))
        triangle.append(rows)
    return triangle

for row in pascal(5):
    print(row)

def prob (tosses,heads):
    probability = binomial(tosses,heads) / 2**tosses
    return probability

print(prob(100,60))

def prob(tosses, heads):
    probability = binomial(tosses,heads) / 2**tosses
    return probability

print(prob(100,60))
for i in range(61,100):
    print(prob(100,i))
# 100 choose 60













