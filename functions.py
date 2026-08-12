def get_todos():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg):
    with open("todos.txt", "w") as file:
        file.writelines(todos_arg)
