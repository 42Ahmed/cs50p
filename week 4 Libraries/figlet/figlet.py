from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
elif "-f" in sys.argv or "--font" in sys.argv:
    if "-f" in sys.argv:
        index = sys.argv.index("-f") + 1
    elif "--font" in sys.argv:
        index = sys.argv.index("--font") + 1
    try:
        font = sys.argv[index]
        figlet.setFont(font=font)
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))
