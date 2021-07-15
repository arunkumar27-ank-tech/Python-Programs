def gene():
     yield 5
val = gene()
print(val.__next__())