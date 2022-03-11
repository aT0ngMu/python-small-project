import time
import random

print(
    """
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.

0 Wins, 0 Losses 0 Ties
Enter your move: (R)ock (P)aper (S)cissors or (Q)uit
"""
)

prompt = "> "
options = ["R", "P", "S"]
exit_option = ["Q"]
avaliable_options = options + exit_option


def evaluate(choose, computer):
    weak_options = ["S", "R", "P"]
    for first, second in zip(options, weak_options):
        if choose == first and computer == second:
            return True

    return False


def play_game():
    computer = random.choice(options)
    print(computer)

    if choose == computer:
        print("State is tie")
    elif evaluate(choose, computer):
        print("You win")
    else:
        print("You lose")


while True:
    choose = input(prompt).upper()

    if choose not in avaliable_options:
        print("Please enter: (R)ock (P)aper (S)cissors or (Q)uit")
        continue

    if choose in exit_option:
        break

    play_game()
