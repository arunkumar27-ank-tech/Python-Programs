def sort(list):
    for i in range(5):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j


        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

        print(list)


list = [5, 12, 8, 4, 9, 2]
sort(list)
print(list)