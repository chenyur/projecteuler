with open('p67.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

i = 0
for l in lines:
    lines[i] = l.split(" ")
    lines[i] = [int(x) for x in lines[i]]
    i += 1

for l in range(len(lines) - 2, -1, -1):
    for p in range(0, l + 1):
        lines[l][p] = lines[l][p] + max(lines[l + 1][p], lines[l + 1][p + 1])

print lines[0]
