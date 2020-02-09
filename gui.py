import PySimpleGUI as sg 

sg.theme('DarkBlue')

layout = [  [sg.Text('What day is it?')],
            [sg.Text('Day of the Week'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    print('Today is', values[0])

window.close()