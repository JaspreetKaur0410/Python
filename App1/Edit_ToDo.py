todos = []

while True:
    user_action = input("Type add, edit, delete or show or exit ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo ")+"\n"
            # if existing
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file_1 = open('todos.txt', 'w')
            file_1.writelines(todos)
            file_1.close()
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index+1}-{item}")
        case 'edit':
            number = input("Number of the TODO to edit: ")
            number = int(number)
            number = number - 1
            new_todo = input("ENTER NEW ONE: ")
            todos[number] = new_todo
        case 'delete':
            number = input("Number of the TODO to DELETE: ")
            number = int(number)
            number = number - 1
            todos.pop(number)
            print("NUMBER DELETED")
        case 'exit':
            break
        case whatever:
            print("Enter correct Action")