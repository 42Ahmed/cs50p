import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

required = sys.argv[1]
try:
    with open(required, "r") as file:
        lines = file.readlines()
except:
    sys.exit("File does not exist")


counter = 0
for line in lines:
    if line.lstrip().startswith("#"):
        continue
    elif line.strip() =="":
        continue
    else:
        counter +=1

print(counter)