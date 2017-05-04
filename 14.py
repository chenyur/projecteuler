def collatz(current, counter):
    if current == 1:
        return counter
    if current % 2 == 0:
        return collatz (current / 2, counter + 1)
    if current % 2 == 1:
        return collatz (current * 3 + 1, counter + 1)

def main():
    longest = 0
    number = 0
    for i in range(1, 1000000):
        if i % 1000 == 0:
            print i
        current = collatz(i, 1)
        if current > longest:
            longest = current
            number = i
    print number

main()
