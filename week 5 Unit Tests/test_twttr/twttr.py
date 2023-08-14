def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    vowel = "aeiouAEIOU"
    new = ""
    for letter in word:
        if letter not in vowel:
            new += letter
    return new


if __name__ == "__main__":
    main()
