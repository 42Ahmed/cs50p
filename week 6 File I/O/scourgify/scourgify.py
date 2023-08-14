import csv
import sys

if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

try:
    students_before = []
    required1 = sys.argv[1]
    with open(required1) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_before.append({"name":row["name"],"house":row["house"]})
except:
    sys.exit(f"Could not read {sys.argv[1]}")

required2 = sys.argv[2]
students_after = []

for student in students_before:
    last,first= student["name"].split(", ")
    students_after.append({"first":first,"last":last,"house":student["house"]})

with open(required2,"w") as file:
     writer = csv.DictWriter(file, fieldnames=["first","last","house"])
     writer.writeheader()
     for student in students_after:
         writer.writerow(student)