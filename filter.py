from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda n: n % 2 == 0, lst))

doubles = list(map(lambda n: n+2, evens))

sum1 = reduce(lambda a, b: a+b, doubles)
print(evens)
print(doubles)
print(sum1)
