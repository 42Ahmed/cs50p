def main():
    time = input("what time is it? ").strip().lower()
    time = convert(time)
    if 7<= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if time.endswith('a.m.') or time.endswith('p.m.'):
        hours, minutes = time[:-5].split(':')
        hours = int(hours)

        if time.endswith('p.m.') and hours != 12:
            hours += 12
        elif time.endswith('a.m.') and hours == 12:
            hours = 0

    else:
        hours,minutes = time.split(":")

    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()