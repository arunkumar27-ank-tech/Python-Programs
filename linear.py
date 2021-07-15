pos = 0


def search(list, n):  # creating a function search
    i = 0  # initializing a variable to iterate all the elements in list
    while i < len(list):  # condition to stop when iteration completed list
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i = i+1  # incrementing iterating value
    return False


list = [22, 33, 14, 63, 56]  # list

n = 14  # number to check whether it is in list or not

if search(list, n):  # calling a method called search and passing values of list and n
    print('found', pos+1)
else:
    print('not found')

