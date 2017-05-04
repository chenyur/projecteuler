cdef int collatz(int current, int counter):
    if current == 1:
        return counter
    if current % 2 == 0:
        return collatz (current / 2, counter + 1)
    if current % 2 == 1:
        return collatz (current * 3 + 1, counter + 1)

def findLongest(int target):
    cdef int longest = 0
    cdef int number = 0
    cdef int i = 1
    for i in range(1, target):
        if i % 1000 == 0:
            print i
        current = collatz(i, 1)
        if current > longest:
            longest = current
            number = i
    return number
