import PySimpleGUI as sg

def create_scene2_layout():
    layout = [
        [sg.Text("This is scene 2", key='-SCENE2-')],
        [sg.Button("Back")]
    ]
    return layout