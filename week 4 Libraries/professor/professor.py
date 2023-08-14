import random


def main():
    level = get_level()
    chances = 3
    score = 0
    equations = 10

    while equations != 0:
        if chances == 3:
            x,y = generate_integer(level)
            answer = x + y
        try:
            z = int(input(f"{x} + {y} = "))
            if z == answer:
                score += 1
                equations -= 1
                chances = 3
                continue
            else:
                raise ValueError
        except EOFError:
            break
        except:
            print("EEE")
            chances -= 1
        if chances == 0:
            print(f"{x} + {y} = {answer}")
            chances = 3
            equations -= 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y


if __name__ == "__main__":
    main()