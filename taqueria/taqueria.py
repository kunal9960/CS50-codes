menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_amount = 0

while True:
    try:

        prompt = input("Item: ").title()

        if prompt in menu:
            total_amount += menu[prompt]
            print("Total: $", end="")
            print("{:.2f}".format(total_amount))

    except EOFError:
        print()
        break
