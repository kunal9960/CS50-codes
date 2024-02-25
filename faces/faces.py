def main():
    prompt = input("Enter an emoji: ")
    result = convert(prompt)
    print(result)

# function to convert into emoji
def convert(prompt):

        prompt1 = prompt.replace(":)", '🙂')
        prompt2 = prompt1.replace(":(", '🙁')
        return prompt2

main()
