class Employee:

    def __init__(self, name, age):
        self.n = name
        self.a = age
        self.i = self.sub()

    def display(self):
        print('the details is ', self.n, self.a)
        self.i.display()

    class sub:

        def __init__(self):
            self.s = 8000
            self.w = 7

        def display(self):
            print('salary and working hour is ', self.s, self.w)


e1 = Employee('xyz', 22)

e1.display()