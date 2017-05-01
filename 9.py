def findTriplet(total):
    for i in range(1, total):
        for x in range (i, total):
           if i ** 2 + x ** 2 == (total - x - i) ** 2:
               print(i, x, total - x - i)

def main():
    print("hello 9")
    findTriplet(1000)


main()
