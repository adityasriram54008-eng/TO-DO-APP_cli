import streamlit as st
import functions

todos = functions.get_todos()

st.title('My Todos App')
#creates a main title, could use st.subheader('') for sub headings and st.rite('') for normal text

for todo in todos:
    st.checkbox(todo)

st.text_input(label = 'Enter a TODO', placeholder = 'Add new TODO...')