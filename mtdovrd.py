class A:
    def a(self):
        print('First one')


class B(A):
    def a(self):
        print('second one')


b = B()
b.a()
