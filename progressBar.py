import random
import time


BAR = chr(9608)

def getProgressBar(progress,total):
    progressBar = ""
    progressBar += "["

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    progressSize = 40
    percent = round(progress / total, 2)
    num_of_block = int(progressSize * percent)

    progressBar += BAR * num_of_block

    progressBar += " " * (progressSize - num_of_block)

    progressBar += "]"

    progressBar += f"{percent * 100}% {progress}/{total}"

    return progressBar


def main():
    byteDownload = 0
    downloadSize = 4096

    while byteDownload < downloadSize:
        byteDownload += random.randint(0,100)

        barStr = getProgressBar(byteDownload,downloadSize)

        time.sleep(0.3)
        print("\r",end="",flush=True)
        print(barStr,end="",flush=True)



if __name__ == "__main__":
    main()