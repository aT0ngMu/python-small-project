import sys
import random

print("""
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
""")

purse = 5000

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}
print("You have 5000 mon. How much do you bet? (or QUIT)")

while True:
    while True:
        enter = input(">")
        if enter.upper() == "QUIT":
            sys.exit()
        elif not enter.isdecimal():
            print("Please input numbers")
            continue
        elif int(enter) > purse:
            print("You don't have enought money")
            continue
        else:
            enter = int(enter)
            break

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print("""
    The dealer swirls the cup and you hear the rattle of dice.
    The dealer slams the cup on the floor, still covering the
    dice and asks for your bet.
    """)
    print()
    print("    CHO (even) or HAN (odd)?")

    while True:
        choose = input(">").upper()
        if choose != "CHO" and choose != "HAN":
            print("Please enter either CHO or HAN")
            continue
        else:
            break

    print("The dealer lifts the cup to reveal:")
    print(" ",JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("   ",dice1, "-", dice2)

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = "CHO"
    else:
        correctBet = "HAN"

    playerWon = choose == correctBet
    if playerWon:
        print("You win")
        purse += enter
        print(f"The house collects a {enter // 10} mon fee")
        purse = purse - (enter // 10)
    else:
        print("You lose")
        purse = purse - enter

    if purse == 0:
        print("You don't have enough money")
        sys.exit()



