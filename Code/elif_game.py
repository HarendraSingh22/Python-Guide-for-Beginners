print("Let's play a game\nInput a number from (1 or 2): ")
number = int(input("> "))
if number==1:
    print("A bear is standing in front of you")
    print("Enter another number (1 or 2)")
    num = int(input(">"))
    if num==1:
        print("Bear ate you.")
    elif num==2:
        print("Bear scratched your face")
    else:
        print("You fought back.\nBear ran away.\nYou are safe")
elif number==2:
    print("A lion is standing in front of you")
    print("Enter another number (1 or 2)")
    num = int(input(">"))
    if num==1:
        print("Lion ate you.")
    elif num==2:
        print("Lion scratched your face")
    else:
        print("You fought back.\nLion ran away.\nYou are safe")
else:
    print("You are safe, go home")
