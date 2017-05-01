import math
print("Hello problem 5")

limit = 5

def smallest(limit):
    i = 1;
    while 1:
        for k in range(1, limit + 1):
            if i % k != 0:
                break
            if i % 1000000 == 0 and k == 1: print(i)
            if k == limit: return i
        i += 1

def main():
    target = input(int("target?\n"))
    print("answer: " + str(smallest(target)))


main()
