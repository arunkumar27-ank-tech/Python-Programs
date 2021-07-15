from array import *

arr = array('i', [])

n = int(input('Enter the size of array'))

for i in range(n):
    x = int(input('Enter the values '))
    arr.append(x)
print(arr)

s = int(input('Enter the number to search '))
k = 0
for e in arr:
    if e == s:
        print('the position of number is',k)
        break
    k += 1
