user_num = input("How many todos?")
print("I want "+user_num+" todos")

i=1

todos = []
user_promt = "Enter todo: "

while i <= int(user_num):
    todo = input(user_promt)
    todos.append(todo)
    i=i+1

print(todos)