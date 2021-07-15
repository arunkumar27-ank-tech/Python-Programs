for row in range(5):
    for col in range(3):
        if row == 0 and col == 1 or row == 2 and col == 1:
            print('A', end='')
        elif row == 0 and (col == 0 or col == 2) or col == 1:
            print(" ", end = '')
        else:
            print('A', end = '')
    print()