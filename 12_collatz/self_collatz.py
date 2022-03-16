import sys
import time

print('''Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.
It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')

print('Enter a starting number (greater than 0) or QUIT:')


while True:
    response = input('> ')
    if not response.isdecimal() or response == "0":
        print("You must enter an integer greater than 0.")
    else:
        response = int(response)
        break

print(response,end="",flush=True)
while response != 1:
    if (response % 2) == 0:
        response = response // 2
    else:
        response = response * 3 + 1

    print(", ",str(response),end="",flush=True)
    time.sleep(0.1)

print()


