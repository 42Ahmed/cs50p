import random

while True:
    try:
        level = int(input("Level: "))
        required = random.randint(1,level)
        break
    except EOFError:
        break
    except:
        pass

while True:
    try:
        guess = int(input("Guess: "))
    except EOFError:
        break
    except:
        pass

    else:
        if guess == required:
            print("Just right!")
            break
        elif guess > required:
            print("Too large!")
        elif guess < required:
            print("Too small!")

