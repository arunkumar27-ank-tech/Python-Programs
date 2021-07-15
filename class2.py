class Student:

    def __init__(self, name, age, dept, batch, cutoff, state, country):
        self.a = name
        self.b = age
        self.c = dept
        self.d = batch
        self.e = cutoff
        self.f = state
        self.h = country

    def func(self):
        print('The student details are : ', self.a, self.b, self.c, self.d, self.e, self.f,)


s1 = Student('arun', '21', 'cse', '2020', '133.5', 'TN', 'india')

s2 = Student('anki', '21', 'cse', '2020', '190', 'kerala', 'india')

s3 = Student('undertaker', '65', 'wwe', '1947', '200', 'newyork', 'usa')

s4 = Student('martinscorrcese', '72', 'cinema', '1965', '1000', 'newjersey', 'usa')

s1.func()
s2.func()
s3.func()
