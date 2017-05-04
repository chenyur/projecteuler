import sys

def divisors(number):
    divisors = []
    for i in range (1, int(number ** 0.5 + 1)):
        if number % i == 0:
            divisors.append(i)
            if number / i != i:
                divisors.append(number / i)
    return len(divisors)

def checkTriangleNumbers(limit):
    currentAdd = 1
    current = 0
    while(1):
        current += currentAdd
        if divisors(current) > limit:
            return current
        currentAdd += 1

print(checkTriangleNumbers(int(sys.argv[1])))
