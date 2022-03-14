import sys
import time

print("""
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
""")

wins = 0
while True:
    print(f"{wins} wins,0 Losses,0 Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
    enter = input(">").upper()

    while True:
        if enter == "Q":
            sys.exit()
        elif enter == "R" or enter == "P" or enter == "S":
            break
        else:
            print("Type one of R, P, S, or Q.")

    if enter == "R":
        print("Rock versus...")
    elif enter == "P":
        print("Paper versus...")
    elif enter == "S":
        print("Scissors versus...")

    time.sleep(0.25)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")

    if enter == "R":
        print("Scissors")
    elif enter == "P":
        print("Rock")
    elif enter == "S":
        print("Paper")

    print("You win")
    wins +=1
