import math


def primesBelow(limit):
    primes = []
    for i in range(5, limit + 1, 2):
        for k in range(2, int(math.sqrt(i)) + 1):
            if i % k == 0:
                break
            if k == int(math.sqrt(i)):
                print(i, " is a prime")
                primes.append(i)
    return primes

def main():
    print("hello 10")
    print (sum(primesBelow(2000000)) + 2 + 3, " is the sum")


main()

