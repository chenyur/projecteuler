from num2words import num2words

length = 0
for x in range (1, 1001):
    length += len(num2words(x).replace(" ", "").replace("-", ""))

print length
