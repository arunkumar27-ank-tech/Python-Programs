seat_count = 3

student_count = int(input('enter the students count'))
i = 1

while i <= student_count:
    if i > seat_count:
        print('students not allowed')

        break
    print('Students are allowing')

    i += 1

