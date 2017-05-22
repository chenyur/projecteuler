import math, itertools

def isAbundant(number):
    divisors = [1]
    for x in range (2, int(number ** 0.5) + 1):
        if number % x == 0:
            divisors.append(x)
            if number / x != x:
                divisors.append(number / x)
    if sum(divisors) > number:
        return True
    else:
        return False


def generateAbundant(limit):
    numbers = []
    for x in range (1, limit + 1):
        if isAbundant(x):
            numbers.append(x)
    return numbers

abundants = generateAbundant(30000)

possibleCombos = itertools.product(abundants, repeat = 2)

possibles = set()

for combos in possibleCombos:
    possibles.add(combos[0] + combos[1])

impossibles = set(range(1, 30000)) - possibles

print(sum(list(impossibles)))
