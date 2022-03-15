try:
    import pyperclip
except ImportError:
    print("Please install pyperclip")

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

def main():
    print("Enter your message:")
    enter = input(">")
    pigLation = englishToLPigLation(enter)
    print(pigLation)

def englishToLPigLation(message):
    pigLation = ""
    for word in message.split():

        prefixNonLetters = ""
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]

        if len(word) == 0:
            pigLation = pigLation + prefixNonLetters + " "
            continue

        suffixNonLetters = ""
        while not word[-1].isalpha():
            suffixNonLetters += word[-1]
            word = word[:-1]

        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()

        prefixConstants = ""
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConstants += word[0]
            word = word[1:]

        if prefixConstants != "":
            word += prefixConstants + "ay"
        else:
            word += "yay"

        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        pigLation += prefixNonLetters + word + suffixNonLetters + " "

    return pigLation



if __name__ == "__main__":
    main()