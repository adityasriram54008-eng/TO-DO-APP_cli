import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a TO-DO:')
#inside the gui, there's a label, i mean like a header
input_box = sg.InputText(tooltip= 'Enter TO-DO', key = 'TO-DO')
#inside the label you can input using this, this is where you enter
add_button = sg.Button('Add')
# a clickable button

window = sg.Window('My TO-DO App',layout= [[label] , [input_box,add_button]], font = ('Helvetica', 12))
#the window of the gui i mean in the interface, with '..' as the title
#in layout[] there's a nested list indicating the contents will be in one row

while True:
    event , values = window.read()
    # for eg window.read() for adding hi does == event = 'Add'  and values = {TO-DO:'hi'})
    print(values)
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['TO-DO'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()