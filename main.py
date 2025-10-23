todos = []

while True:
    print("1 : Add")
    print("2 : Show")
    print("3 : Edit")
    print("4 : Complete")
    print("5 : Exit")
    # Get user input and strip whitespace
    user_action = input("Enter a value: ")
    user_action = user_action.strip()

    match user_action:
        case '1': # Add
            todo = input("Enter a to do: ") + "\n"

            # Read existing todos from file
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            # Add new todo to the list
            todos.append(todo)

            # Write updated todos back to file
            txtfile = open("todos.txt", "a")
            txtfile.writelines(todo)
            txtfile.close()
        case '2': # Show
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for (i, item) in enumerate(todos):
                item = item.strip('\n')
                row = f"{i+1}.{item.capitalize()}"
                print(row)
        case '3': # Edit
            for (i, item) in enumerate(todos):
                row = f"{i+1}.{item.capitalize()}"
                print(row)
            number = int(input("Number of todo list to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
            for (i, item) in enumerate(todos):
                row = f"{i+1}.{item.capitalize()}"
                print(row)
        case '4': # Complete
            number = int(input("Number of todo list to complete: "))
            todos.pop(number - 1)
        case _ : # Exit
            print("Exiting...")
            break
