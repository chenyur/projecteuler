fibonacci = [1, 1]
i = 0

while 1:
    fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    if len(str(fibonacci[-1])) == 1000:
        print i + 3
        break
    i += 1
