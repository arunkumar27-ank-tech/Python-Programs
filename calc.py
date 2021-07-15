def add():
    print("1st function", __name__)


def sub():
    print("2nd func")


def mul():
    add()
    sub()


if __name__ == "__main__":
    mul()