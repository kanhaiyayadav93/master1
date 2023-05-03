# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M%S")
print("it is", now)

while True:
    user_Action = input("Type add, show, edit, complete exit: ")
    user_Action = user_Action.strip()

    if user_Action.startswith('add'):
        todo = user_Action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif user_Action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_Action.startswith('edit'):
        try:
            number = int(user_Action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_Action.startswith('complete'):

        try:
            number = int(user_Action[9:])

            todos = functions.get_todos()

            index = number - 1
            doto_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"doto {doto_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_Action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("bye")