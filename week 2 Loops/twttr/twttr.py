vowel = "aeiouAEIOU"
word = input("Input: ")
new = ""

for letter in word:
    if letter not in vowel:
        new += letter

print("Output:",new)