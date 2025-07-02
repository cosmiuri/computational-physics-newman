from math import sqrt

def prime(limit):

    primes = [2]
    number = 3

    while number <= limit:
        for prime in primes:
            if number%prime == 0:
                break
            elif prime > sqrt(number):
                primes.append(number)
                break
        number += 1

    return primes
print(prime(10000))

