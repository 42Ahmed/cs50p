import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        out = os.path.splitext(sys.argv[2])
        if out[1].lower() not in format:
            sys.exit("Invalid output")
        elif inp[1].lower() != out[1].lower():
            sys.exit("Input and output have different extensions")

destination = sys.argv[2]
shirt = Image.open("shirt.png")
with Image.open(sys.argv[1]) as input:
    output = ImageOps.fit(input,shirt.size)
    output.paste(shirt,mask = shirt)
    output.save(destination)
