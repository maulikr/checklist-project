todos = []

while True:
    print("Available actions: ")
    print("1 : Add")
    print("2 : Show")
    print("3 : Edit")
    print("4 : Complete")
    print("5 : Exit")
    user_action = input("Enter a value: ")
    user_action = user_action.strip()

    match user_action:
        case '1': # Add
            todo = input("Enter a to do: ") + "\n"

            # with open("todos.txt", "r") as file:
            #     todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case '2': # Show
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            print("Current list: ")

            for (i, item) in enumerate(todos):
                item = item.strip("\n")
                row = f"{i+1}.{item.capitalize()}"
                print(row)

        case '3': # Edit

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            print("Current list: ")
            for (i, item) in enumerate(todos):
                item = item.strip("\n")
                row = f"{i+1}.{item.capitalize()}"
                print(row)

            number = int(input("Number of todo list to edit: "))
            number = number - 1

            # with open("todos.txt", "r") as file:
            #     todos = file.readlines()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case '4': # Complete
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            print("Current list: ")
            for (i, item) in enumerate(todos):
                item = item.strip("\n")
                row = f"{i+1}.{item.capitalize()}"
                print(row)

            number = int(input("Number of todo list to complete: "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"{todo_to_remove} : marked as completed.")

        case _ :
            print("Exiting...")
            break
