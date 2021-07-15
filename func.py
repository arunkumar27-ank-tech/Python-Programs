a = 10
print(id(a))


def some():
    a = 9
    x = globals()['a']
    print(id(x))
    print(a)


some()
print(a)
