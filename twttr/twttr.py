prompt = input("Input: ")
print("Output: ", end = "")

for i in prompt:
    if not i.lower() in ['a','e','i','o','u']:
        print(i, end = "")
print()
