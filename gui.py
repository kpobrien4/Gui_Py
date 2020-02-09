import PySimpleGUI as sg 

sg.theme('DarkBlue')

layout = [  [sg.Text('First GUI')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    print('You entered ', values[0])

window.close()