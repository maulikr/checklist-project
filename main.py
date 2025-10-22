todos = []

while True:
    print("1 : Add")
    print("2 : Show")
    print("3 : Edit")
    print("4 : Complete")
    print("5 : Exit")
    user_action = input("Enter a value: ")
    user_action = user_action.strip()

    match user_action:
        case '1':
            todo = input("Enter a to do: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()

            todos.append(todo)
            txtfile = open("todos.txt", "a")
            txtfile.writelines(todo)
        case '2':
            for (i, item) in enumerate(todos):
                row = f"{i+1}.{item.capitalize()}"
                print(row)
        case '3':
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
        case '4':
            number = int(input("Number of todo list to complete: "))
            todos.pop(number - 1)
        case _ :
            print("Exiting...!")
            break
