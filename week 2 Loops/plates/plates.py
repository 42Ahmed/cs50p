def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    if any( not c.isalnum() for c in s):
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if any(not c.isdigit() for c in s[i:]):
                return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i:-1].startswith("0"):
                return False

    else:
        return True

main()