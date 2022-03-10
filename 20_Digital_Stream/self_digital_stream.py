import random,shutil,sys,time

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHAR = ['ㅅ', 'ㅕ']

# Density can range from 0.0 to 1.0
DENSITY = 0.02

# get the size of the terminal window
WIDTH = shutil.get_terminal_size()[0]

print("Digital Stream")
print("Press Ctrl-C to quit")

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH,MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(random.choice(STREAM_CHAR),end="")
                columns[i] -= 1
            else:
                print(" ",end="")

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()