months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month,day,year = date.split('/')
        elif "," in date:
            monthDays,year = date.split(', ')
            month,day = monthDays.split(' ')
            month = (months.index(month)) + 1
        if int(month) > 12 or int(day) > 31:
            raise ValueError
    except:
        continue
    else:
        print(f"{year}-{str(month).zfill(2)}-{day.zfill(2)}")
        break