print("INSTRUCTIONS")
print("""
type start to start the car
type stop to stop the car
type quit to exit""")
command = ""
while True:

    command = input("<")
    if command=="start":
        print("car started")
    elif command=="stop":
        print("car stopped")
    elif command=="quit":
        break
    else:
        print('sorry, your command is not supported by me')

