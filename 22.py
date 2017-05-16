with open('p22.txt') as namesfile:
    names = namesfile.read().replace('"', '').replace('\n','').split(',')

namesSorted = sorted(names)
sumScore = 0

def findWeights(name):
    sumWeights = 0
    for letter in name:
        sumWeights += ord(letter) - 64

    return sumWeights

for i in range(0, len(namesSorted)):
    nameOrder = i + 1
    nameWeight = findWeights(namesSorted[i])
    nameScore = nameOrder * nameWeight
    sumScore += nameScore

print sumScore
