import itertools
#Inspiration from github.com/Nayuki

array = range(10)
temp = itertools.islice(itertools.permutations(array), 999999, None)
print next(temp)

