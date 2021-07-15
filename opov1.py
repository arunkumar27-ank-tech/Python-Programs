class Student:

    def __init__(self, mark1, mark2):
        self.m1 = mark1
        self.m2 = mark2

    def display(self):
        print(self.m1, self.m2)

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m1
        s4 = Student(m1, m2)
        return s4


s1 = Student(80, 40)
s2 = Student(55, 45)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
s3 = s1 + s2
print(s3.m1)

print(s1)

s4 = s1 - s2
print(s4.m1)


# s1.display()
# s2.display()
# print(s1.m1)
