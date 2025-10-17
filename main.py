todos = []

while True:
    user_action = input("(1)Add, (2)Show or (3)Edit or (4)Exit: ")
    user_action = user_action.strip()

    match user_action:
        case '1':
            todo = input("Enter a to do: ")
            todos.append(todo)
        case '2':
            for item in todos:
                print(item)
        case '3':
            print(todos) 
            number = int(input("Number of todo list to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
            print(todos)
        case _ :
            print("Bye!")
            break

