from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    selection = random.choice(fonts)
    figlet.setFont(font = selection)


elif len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        if sys.argv[1] != "--font":
            sys.exit("Invalid usage")
    if sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
        sys.exit("Invalid usage")

prompt = input("Input: ")
print(f"Output: {figlet.renderText(prompt)}")

