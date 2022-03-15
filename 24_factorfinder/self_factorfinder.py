import math
import sys

while True:
    print("Enter a positive whole number to factor (or QUIT):")
    enter = input(">")

    if enter.upper() == "QUIT":
        sys.exit()

    if not (enter.isdecimal() and len(enter) > 0):
        continue

    number = int(enter)

    factours = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factours.append(i)
            factours.append(number // i)

    factours = list(set(factours))
    factours.sort()

    for i,factor in enumerate(factours):
        factours[i] = str(factor)

    print(", ".join(factours))
