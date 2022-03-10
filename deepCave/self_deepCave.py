import random,sys,time

# set the constants
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # dispaly the tunnel segment
    rightWidth = WIDTH - leftWidth - gapWidth
    print('#' * leftWidth + ' ' * gapWidth + '#' * rightWidth)

    # check for ctrl-c press during brief pause
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    # adjust the left side width
    diceRoll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass
