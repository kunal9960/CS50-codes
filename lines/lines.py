import sys
count = 0


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    fileName = sys.argv[1]
    if fileName.endswith(".py"):
        try:
            with open(fileName) as file:
                for line in file:
                    if not line.lstrip().startswith("#") and line.split() != []:
                        count += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a python file")
print(count)
