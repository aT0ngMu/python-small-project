import sys
import time

try:
    i = 0
    bottles = 99
    while True:
        i += 1

        time.sleep(2)
        print(f"{bottles} bottles of milk on the wall,")
        time.sleep(2)
        print(f"{bottles} bottles of milk,")
        time.sleep(2)
        print("Take one down, pass it around,")

        bottles -= 1
        time.sleep(2)
        print(f"{bottles} bottles of milk on the wall!")
        print()


        if i == 98:
            time.sleep(2)
            print(f"{bottles} bottles of milk on the wall,")
            time.sleep(2)
            print(f"{bottles} bottles of milk,")
            time.sleep(2)
            print("Take one down, pass it around,")

            time.sleep(2)
            print(f"No more bottles of milk on the wall!")
            break


except KeyboardInterrupt:
    sys.exit()