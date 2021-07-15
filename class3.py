class Employee:
    def __init__(self, name, age, idno):
        self.n = name
        self.a = age
        self.i = idno
        self.m = self.sub()

    def show(self):
        print('The employee name, age, and idno is ', self.n, self.a, self.i)
        self.m.display()

    class sub:
        def __init__(self):
            self.s = 8000
            self.w = 8

        def display(self):
            print('salary and work hour ', self.s, self.w)


e1 = Employee('arun', 22, 27)
e2 = Employee('arunkumar', 22, 28)

e1.show()
e2.show()

