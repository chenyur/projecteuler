amicables = []
for i in range(1, 10000):
    if i % 1000 == 0:
        print i
    divisors = []
    for x in range(1, i):
        if i % x == 0:
            divisors.append(x)
    divisors2 = []
    number2 = sum(divisors)
    for k in range(1, number2):
        if number2 % k == 0:
            divisors2.append(k)
    if i == sum(divisors2) and i != number2 and i not in amicables:
        amicables.append(i)
        amicables.append(sum(divisors))

print(sum(amicables))
