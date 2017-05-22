def sumPowerDigits(number, power):
    sumpd = 0
    for d in str(number):
        sumpd += int(d) ** power

    if sumpd == number:
        return True
    else:
        return False

found = 0
current = 2
numbers = []

#Since we don't know how many numbers there are...
while found < 6:
    if sumPowerDigits(current, 5):
       numbers.append(current)
       found += 1
       print "found " + str(current)
    current += 1
    if current % 10000 == 0:
        print current
print sum(numbers)
