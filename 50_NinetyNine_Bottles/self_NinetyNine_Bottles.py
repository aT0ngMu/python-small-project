import sys

try:
    i = 0
    start_bottles = 99
    while True:
        i += 1

        print(f"{start_bottles} bottles of milk on the wall,")
        print(f"{start_bottles} bottles of milk,")
        print("Take one down, pass it around,")

        start_bottles -= 1
        print(f"{start_bottles} bottles of milk on the wall,")
        print()

        if i == 98:
            print(f"{start_bottles} bottles of milk on the wall,")
            print(f"{start_bottles} bottles of milk,")
            print("Take one down, pass it around,")

            print(f"No more bottles of milk on the wall,")
            print()

            break





except KeyboardInterrupt:
    sys.exit()