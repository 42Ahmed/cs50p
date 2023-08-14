from tabulate import tabulate
import csv
import sys

flag = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    required = sys.argv[1]
except:
    sys.exit("File does not exist")

with open(required) as file:
    reader = csv.reader(file)
    table = tabulate(reader, headers="firstrow", tablefmt="grid")
    print(table)