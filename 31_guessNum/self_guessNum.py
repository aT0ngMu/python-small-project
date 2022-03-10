import random

# output hint message
print("I am thinking of a number between 1 and 100." + "\n" + "You have 10 guesses left. Take a guess.")



count = 0
while True:
    # get input
    num = int(input(">"))

    rand_num = random.randint(1,101)
    if num > rand_num:
        print("please lower")
    elif num < rand_num:
        print("please higher")
    else:
        print("correct")

    count += 1
    if count == 10:
        break


