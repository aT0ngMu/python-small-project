import sys
import time
import sevseg

secondsLeft = 4234

try:
    while True: # Main program loop
        # clear the screen by printing several newlines:
        print('\n' * 60)


        # Get the hours/minutes/seconds from secondleft
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        hDigits = sevseg.getSevSegStr(hours,2)
        htopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes,2)
        mtopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds,2)
        stopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(htopRow + "   " + mtopRow + "   " + stopRow)
        print(hMiddleRow + " * " + mMiddleRow + " * " + sMiddleRow)
        print(hBottomRow + " * " + mBottomRow + " * " + sBottomRow)

        if secondsLeft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)
        secondsLeft -= 1

except KeyboardInterrupt:
    sys.exit()


