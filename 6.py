import sys

def sumsquared(target):
    if target == 1:
        return 1
    else:
        return target * target + sumsquared(target - 1)
def sum(target):
    if target == 1:
        return 1
    else:
        return target + sum(target - 1)

def main(target):
    print(sum(target)**2 - sumsquared(target))

main(int(sys.argv[1]))
