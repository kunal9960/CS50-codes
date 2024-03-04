import inflect

p = inflect.engine()

listNames = []

while True:
    try:
        name = input("Name: ")
        listNames.append(name)
    except EOFError:
        break

mylist = p.join((listNames))

print(f"Adieu, adieu, to {mylist}")
