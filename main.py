def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    print("Available actions: ")
    print("1. Add todo - add <todo item>")
    print("2. Show todos - show")
    print("3. Edit todo - edit <item number>")
    print("4. Complete todo - complete <number>")
    print("5. Exit - exit")

    user_action = input("Enter a value: ")
    user_action = user_action.strip()


    if user_action.startswith("add"): # Add
        todo = user_action[4:] + "\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"): # Show
        todos = get_todos("todos.txt")

        print("Current list: ")

        for (i, item) in enumerate(todos):
            item = item.strip("\n")
            row = f"{i+1}.{item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"): # Edit
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"): # Complete
        try:
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos("todos.txt", todos)

            print(f"{todo_to_remove} : marked as completed.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif 'exit' in user_action: # Exit
        print("Exiting...")
        break

    else:
        print("Command not recognized. Try again.")
