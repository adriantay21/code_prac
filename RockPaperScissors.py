import random

Player = input("ROCK/ PAPER/ SCISSORS (R, P, S):")
print()
print(f"You entered {Player}")

CPU = random.randrange(1,4)

if CPU == 1:
    print ("CPU: ROCK!")
elif CPU == 2:
    print ("CPU: PAPER!")
elif CPU == 3:
    print("CPU: SCISSORS!")

if Player == "R":
    if CPU == 1:
        print ("TIE")
    elif CPU == 2:
        print ("CPU WINS")
    elif CPU == 3:
        print ("YOU WIN")
elif Player == "P":
    if CPU == 1:
        print ("YOU WIN")
    elif CPU == 2:
        print ("TIE")
    elif CPU == 3:
        print ("CPU WINS")
elif Player == "S":
    if CPU == 1:
        print ("CPU WINS")
    elif CPU == 2:
        print ("YOU WIN")
    elif CPU == 3:
        print ("TIE")