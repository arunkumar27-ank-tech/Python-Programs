class A:
    #def __init__(self):
        #print('object a is working')
    def feature1(self):
        print('Feature 1 is working')
    def feature2(self):
        print('feature 2 is working')


class B(A):

    #def __init__(self):
        #super().__init__()
        #print('class b is executing')

    def feature3(self):
        print("feature 3 is working")


a1 = B()
a1.feature1()


