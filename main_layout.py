import PySimpleGUI as sg

def create_main_layout():
    layout = [
        [sg.Text("Main Menu")],
        [sg.Button("New Game")],
        [sg.Button("Exit")]
    ]
    return layout