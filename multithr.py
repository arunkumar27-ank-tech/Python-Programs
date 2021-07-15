from time import sleep
from threading import *

class A(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)


a = A()
b = B()

a.run()
b.run()
print('bye')