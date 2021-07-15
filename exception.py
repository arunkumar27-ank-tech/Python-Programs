a = int(input("Enter first number"))
b = int(input("Enter second number"))

try:
    print("resource open")
    print(a/b)
    k = int(input('enter the value pf k '))
    print(k)


except Exception as e:
    print("hey , you cannot divide a number by 0 ", e)

finally:
    print("resource closed")
