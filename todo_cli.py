import time
import functions

t = time.strftime("%d-%Y-%m- %H:%M:%S")
print(t)

while True:
    user_need = input("Enter add, show, edit, complete or exit: ")
    user_need = user_need.lower()
    user_need = user_need.strip()

    if user_need.startswith('add'):

        todo = user_need[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_need.startswith('show'):
        todos = functions.get_todos()
        for index,todo in enumerate(todos):
            print(f"{index+1}: {todo}",end="")

    elif user_need.startswith('edit'):
        try:
            todos = functions.get_todos()
            if len(todos) < 1:
                print("No todos added")
            number  = int(input("Enter the number of todo to edit: "))
            updated_todo = input("Enter the updated version: ")
            todos[number-1] = updated_todo + "\n"
            functions.write_todos(todos)

        except IndexError:
            print(f"Invalid todo to edit because {number} does not exist")
            continue

    elif user_need.startswith('complete'):
        try:
            todos = functions.get_todos()
            if len(todos) < 1:
                print("No todos added")
            for index,todo in enumerate(todos):
                print(f"{index+1}: {todo}",end="")
            number = int(input("Enter the number of todo to delete: "))
            deleted = todos.pop(number-1)
            print(f"{number}: {deleted.strip('\n')} has been deleted")
            functions.write_todos(todos)

        except IndexError:
            print(f"The {number} numbered todo does not exist")

    elif user_need.startswith('exit'):
        break

    else:
        print("Invalid input")
