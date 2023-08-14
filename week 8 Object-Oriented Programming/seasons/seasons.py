import inflect
from datetime import date
import sys

p = inflect.engine()




def main():
    try:
        today = date.today()
        year,month,day = input("Date of Birth: ").split("-")
        birthdate = date(int(year),int(month),int(day))
        diff = today - birthdate
        total = int(diff.total_seconds() / 60)
        print(to_words(total))
    except:
        sys.exit("Invalid date")


def to_words(i):
    return f"{p.number_to_words(i, andword='').capitalize()} minutes"




if __name__ == "__main__":
    main()
