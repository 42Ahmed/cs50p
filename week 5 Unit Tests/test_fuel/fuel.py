def main():
    while True:
        try:
            percentage = convert(input())
        except:
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    z = x/y * 100
    if y ==0:
        raise ZeroDivisionError
    elif x >y:
        raise ValueError
    return int(round(z))


def gauge(z):
    if z >= 99:
        return "F"
    elif z <= 1:
        return "E"
    else:
        return f"{str(z)}%"

if __name__ == "__main__":
    main()