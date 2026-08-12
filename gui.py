import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a TO-DO')
#inside the gui, there's a label, i mean like a header
input_box = sg.InputText(tooltip= 'Enter TO-DO')
#inside the label you can input using this, this is where you enter
add_button = sg.Button('Add')
# a clickable button

window = sg.Window('My TO-DO App', layout= [[label] , [input_box,add_button]])
#the window of the gui i mean in the interface, with '..' as the title
#in layout[] there's a nested list indicating the contents will be in one row

window.read()
#displays the actual gui
window.close()