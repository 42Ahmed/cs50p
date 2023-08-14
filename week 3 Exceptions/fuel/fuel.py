while True:
    try:
        x,y = input("Fraction ").split("/")
        x = int(x)
        y = int(y)
        z = x/y * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if x >y:
            continue
        else:
            break

if z >= 99:
    print("F")
elif z <= 1:
    print("E")
else:
    print(f"{round(z)}%")