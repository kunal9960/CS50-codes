prompt = input("Greeting: ")

lower = prompt.lower()

if 'hello' in lower:
    print("$0")
elif 'h' == lower[0]:
    print("$20")
else:
    print("$100")
