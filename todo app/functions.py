FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the text of file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_org, filepath=FILEPATH):
    """ Write the to-do item in the text file. """
    with open(filepath, 'w') as file_org:
        file_org.writelines(todos_org)


if __name__ == "__main__":
    print("Hello")
