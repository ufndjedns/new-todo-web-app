FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    """read a text file and return the list of
    todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_given, filepath=FILEPATH):
    """add, edit or complete the todo items in
    the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todo_given)
