import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']+'\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todos App')
#creates a main title, could use st.subheader('') for sub headings and st.rite('') for normal text

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = 'Enter a TODO', placeholder = 'Add new TODO...', on_change = add_todo, key = 'new_todo')

st.session_state