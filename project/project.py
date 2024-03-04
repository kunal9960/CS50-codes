import time

FILEPATH = "todos.txt"


def get_current_time():
    now = time.strftime("%b %d, %Y %H:%M:%S")
    return now


print("It is", get_current_time())


def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def main():
    while True:
        user_prompt = input("Type add, show, edit, complete or exit: ")
        user_prompt = user_prompt.strip()

        if user_prompt.startswith('add'):
            todo = user_prompt[4:].capitalize() + '\n'

            todos = get_todos()

            todos.append(todo)
            write_todos(todos)

        elif user_prompt.startswith('show'):
            todos = get_todos()
            for index, item in enumerate(todos):
                item = item.strip("\n")
                item = item.capitalize()
                row = f"{index + 1}.{item}"
                print(row)

        elif user_prompt.startswith('edit'):
            try:
                number = int(user_prompt[5:])
                print(number)
                number = number - 1

                todos = get_todos()

                new_todo = input("Enter the new todo: ").capitalize() + "\n"
                todos[number] = new_todo

                write_todos(todos)

            except ValueError:
                print("You should've entered the number of the todo.")
                continue

        elif user_prompt.startswith('complete'):
            try:
                number = int(user_prompt[9:])

                todos = get_todos()

                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                write_todos(todos)

                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)

            except IndexError:
                print("There is no item with that number.")
                continue

        elif user_prompt.startswith('exit'):
            break

        else:
            print("Hey, you typed a wrong command")

    print("Bye!")


if __name__ == "__main__":
    main()
