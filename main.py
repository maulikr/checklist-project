todos = []

while True:
    # print("Available actions: ")
    # print("1. Add todo - add <todo item>")
    # print("2. Show todos - show")
    # print("3. Edit todo - edit <new todo item>")
    # print("4. Complete todo - complete <number>")
    # print("5. Exit - exit")
    user_action = input("Enter a value: ")
    user_action = user_action.strip()


    if 'add' in user_action: # Add
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action: # Show
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        print("Current list: ")

        for (i, item) in enumerate(todos):
            item = item.strip("\n")
            row = f"{i+1}.{item.capitalize()}"
            print(row)

    elif 'edit' in user_action: # Edit

        number = int(user_action[5:])
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action: # Complete
        number = int(user_action[9:])
        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        print(f"{todo_to_remove} : marked as completed.")

    elif 'exit' in user_action: # Exit
        print("Exiting...")
        break

    else:
        print("Command not recognized. Try again.")
