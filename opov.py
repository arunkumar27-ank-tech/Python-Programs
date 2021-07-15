class Student:
    def __init__(self, mark1, mark2):
        self.m1 = mark1
        self.m2 = mark2


    # def display(self):
        # print(self.m1, self.m2)

    def __add__(self, other):
        m1 = self.m1+self.m2
        m2 = other.m1+other.m2
        s3 = Student(m1, m2)
        return s3

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s4 = Student(m1,m2)
        return s4


s1 = Student(22, 45)
s2 = Student(55, 65)

s3 = s1+s2

s4 = s1-s2
print(s3.m1)
print(s3.m2)
print(s4.m1)
print(s4.m2)

# s1.display()
# s2.display()
