class Arun:

    def __init__(self, brand, model, ram):
        self.b = brand
        self.c = model
        self.d = ram

    def config(self):
        print('The lap specification is', self.b, self.c, self.d)


comp = Arun('dell', 'vostro', '8gb')
comp1 = Arun('hp', 'inspiron', '8gb')

comp.config()
comp1.config()
