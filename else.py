auditorium_max = 500

students = 500

if students < auditorium_max:
    print('Students are allowed to enter the auditorium')

elif students == auditorium_max:
    print('Students count correctly matched with auditorium seat count')
else:
    print('There are more number students than auditorium can hold')
