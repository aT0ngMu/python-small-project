import time,sys

try:
    import bext
except ImportError:
    sys.exit()

print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0
indentIncreasing = True

try:
    while True:
        print(" " * indent,end="")

        bext.fg("red")
        print("##" * indent,end="")

        bext.fg("yellow")
        print("##" * indent,end="")

        bext.fg("green")
        print("##" * indent,end="")

        bext.fg("blue")
        print("##" * indent,end="")

        bext.fg("cyan")
        print("##" * indent,end="")

        bext.fg("purple")
        print("##")

        if indentIncreasing:
            indent += 1

            if indent == 60:
                indentIncreasing = False

        else:
            indent -= 1

            if indent == 0:
                indentIncreasing = True

        time.sleep(0.02)

except KeyboardInterrupt:
    sys.exit()


