def findSelfPower(number):
    ans = 0
    for x in range(1, number + 1):
        ans += x ** x
    return ans

print findSelfPower(1000)

