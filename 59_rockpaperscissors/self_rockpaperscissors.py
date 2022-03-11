import sys
import time
import random

print("""
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
""")
print()
print("0 Wins, 0 Losses 0 Ties")
print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")

options = ["R","P","S"]


while True:
    choose = input(">")
    choose = choose.upper()

    if choose != options[0] and \
            choose != options[1] and \
            choose != options[2] and \
            choose != "Q":
        print("Please enter: (R)ock (P)aper (S)cissors or (Q)uit")

    elif choose == "Q":
        sys.exit()

    else:
        computer = random.choice(options)

        if choose == computer:
            print("State is tie")

        elif (choose == "R" and computer == "S") or \
                (choose == "P" and computer == "R") or \
                (choose == "S" and computer == "P"):
            print("You win")

        else:
            print("You lose")




    print(computer)