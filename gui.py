import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('Reddit')

clock = sg.Text('', key = 'clock')
label = sg.Text('Type in a TO-DO:')
#inside the gui, there's a label, i mean like a header

input_box = sg.InputText(tooltip= 'Enter TO-DO', key = 'TO-DO')
#inside the label you can input using this, this is where you enter

add_button = sg.Button('Add')
# a clickable button

list_box = sg.Listbox(values=functions.get_todos(), key = 'todos', enable_events = True, size = [45,10])
#a list box to be displayed in gui and has values from get_todos

edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My TO-DO App',layout= [[clock], [label] , [input_box,add_button], [list_box,edit_button,complete_button],[exit_button]], font = ('Helvetica', 12))
#the window of the gui i mean in the interface, with '..' as the title
#in layout[] there's a nested list indicating the contents will be in one row

while True:
    event , values = window.read(timeout = 1000)
    # for eg window.read() for adding hi using the 'Add' button does == event = 'Add'  and values = {TO-DO:'hi'})
    window['clock'].update(value = time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
    #checks for feature to be done similar to todo_cli.py

        case "Add":
            todos = functions.get_todos()
            new_todo = values['TO-DO'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            # todos gets the existing todos for get_todos() function if any or is just empty
            # then new_todo gets assigned the todos entered, using the key value TO-DO which stores the entered input
            #that new_todo is appeneded to the existing todos list with \n, and is written into todos.txt

            window['todos'].update(values=todos)
            #this does real time addition of to_do in the list box

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                #todo_to_edit gets the value associated with the todos key from the listbox, i.e by clicking on a particular to_do
                #you get the event as todos with values, but by clicking on the edit button this case matches and the following operations are done

                new_todo = values['TO-DO'] +'\n'
                # new_todo stores the value associated with the key TO-DO entered in the input box after selection of the to-do to be edited

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                #gets the index of to_do clicked on
                todos[index] = new_todo
                #using the index the old to_do is replaced with the new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                #this does real time changing in the todos listbox

            except IndexError:
                sg.popup('please select a valid TO-DO',text_color = 'maroon', font = ('Helvetica', 12))

        case 'todos':
            window['TO-DO'].update(value=values['todos'][0])
            #this does real time updation when a to_do is clicked it gets pasted in the input box

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['TO-DO'].update(value = '')
            except IndexError:
                sg.popup('please select a valid TO-DO', text_color='maroon', font=('Helvetica', 12))

        case 'Exit':
            break

        case sg.WIN_CLOSED:
        #case when close clicked, loop breaks out and the window is closed
            break

window.close()