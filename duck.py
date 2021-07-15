class Laptop:  # define a class with base method
    def code(self, ide):
        ide.execute()


class PyCharm:
    def execute(self):
        print('have some specified work')


class somewhat:
    def execute(self):  # the method is named as execute because the base method has method value as execute
        print('this class doing the same work as before class technically termed as duck-typing')


m = somewhat() # creating object and calling constructor for the base method
l1 = Laptop()
l1.code(m)  # calling code
# object is passed into method as argument

# idk where this will be used
