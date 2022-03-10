import math,sys

def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True

    if num % 2 == 0:
        return False

    return True

def main():
    while True:
        num = input(">")
        if num.isdecimal():
            num = int(num)
            break

    while True:
        if isPrime(num):
            print(str(num) + ',',end='',flush=True)
        num += 1



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()