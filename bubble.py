def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]

                list[j] = list[j+1]
                list[j+1] = temp

                print(list)


list = [5, 12, 8, 4, 4, 9, 2]
sort(list)
print(list)
