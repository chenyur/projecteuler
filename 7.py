import math
import sys
import pdb

def prime(index):
    current = 2
    count = 2
    while 1:
        for i in range(2, current):
            if current % i == 0:
                break

            if i == current - 1:
                if count % 100 == 0:
                    print(current, count)
                count += 1
        # pdb.set_trace()
        if count > int(index):
            return current
        else: current += 1

def main(index):
    print("finding nth prime n = " + str(index))
    print(prime(index))

main(sys.argv[1])
