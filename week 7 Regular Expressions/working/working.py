import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = "^(0?(?:[1-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM)?) to (0?(?:[1-9]|1[0-2])(?::[0-5][0-9])? (?:AM|PM)?)$"
    matches = re.search(pattern, s, re.IGNORECASE)

    if not matches:
        raise ValueError

    start_time, end_time = matches.groups()

    time, when = start_time.split(" ")
    time2, when2 = end_time.split(" ")

    frm = format_time(time, when)
    to = format_time(time2, when2)
    
    return f"{frm} to {to}"


def format_time(time, when):
    if ":" in time:
        hours, minutes = time.split(":")
    else:
        minutes = None
        hours = time

    if hours == "12":
        if when == "AM":
            hours = "00"
        else:
            hours = "12"
    else:
        if when == "AM":
            hours = f"{int(hours):02}"
        else:
            hours = f"{int(hours) + 12}"

    if minutes is None:
        minutes = "00"
    else:
        f"{int(minutes):02}"

    return f"{hours}:{minutes}"


if __name__ == "__main__":
    main()
