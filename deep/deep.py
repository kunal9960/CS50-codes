prompt = input("What is the answer to the Greatest Question of Life, the Universe and Everything?: ")

if prompt.strip() == "42":
    print("Yes")
elif prompt.lower().strip() == "forty-two":
    print("Yes")
elif prompt.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
