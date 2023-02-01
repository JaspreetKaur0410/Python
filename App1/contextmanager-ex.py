# Context Manager provde _enter__() and __exi__()
# When "with" is encountered - _enter__() is called
# if __enter__() return object - binds to target value used in context(as stmt)
# Execute block
# __exit__() called
# once with block ends, file gets closed automatically
# but once you assign variable to file read function, you can access content of file after block ends

# with open('doc.txt', 'r') as file:
#       file.read()
#       content = file.read()
# For above block - content will be empty as file is already read

while True:
    user_action = input("Type add, edit, delete or show or exit ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo ")+"\n"

            with open('todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt','w') as file:
                todos = file.writelines(todos)
        case 'show':
            with open('todos.txt','r') as file:
                todos = file.readlines()

            #_________________LIST COMPREHENSION _______________________________________________#
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index+1}-{item}")
        case 'edit':
            number = input("Number of the TODO to edit: ")
            number = int(number)
            number = number - 1
            with open('todos.txt','r') as file:
                todos = file.readlines()
            new_todo = input("ENTER NEW ONE: ")
            todos[number] = new_todo+"\n"
            with open('todos.txt','w') as file:
                todos = file.writelines(todos)
        case 'delete':
            number = input("Number of the TODO to DELETE: ")
            number = int(number)
            number = number - 1
            todos.pop(number)
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
            print("NUMBER DELETED")
        case 'exit':
            break
        case whatever:
            print("Enter correct Action")