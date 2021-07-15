f = open('dett.txt', 'r')

print(f.readline())

f1 = open('abc.txt', 'w')

for data in f:
    f1.write(data)
