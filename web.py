import streamlit as st
import functions

todos = functions.get_todos()
#getting existing todos from the tods.txt file

def add_todo():
    todo = st.session_state['new_todo']+'\n'
    #on calling add_todo, to_do gets the value from input box(i.e the entered string) with a break line as string
    todos.append(todo)
    functions.write_todos(todos)

st.title('My Todos App')
#creates a main title, could use st.subheader('') for sub headings and st.rite('') for normal text

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    #creates a checkbox with the entered to_do, stores it in a key to_do
    if checkbox:
        #checkbox is true, when the box is checked
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        #poppin might delete it from todos but not from session_state so del is used
        st.rerun()
        #gotta use it

st.text_input(label = 'Enter a TODO', placeholder = 'Add new TODO...', on_change = add_todo, key = 'new_todo')
#this is the input box, label is just a side heading, placeholder is like a tool tip,entered to_do gets a new_todo key
#and the on pressing enter the on_change is implemented which calls the add_todo function