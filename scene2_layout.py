import PySimpleGUI as sg

def create_scene2_layout():

    

    layout = [
        [sg.Text("This is scene 2")],
        [sg.Button("Back", pad=(0, 0))],
        [sg.Button("Plant", pad=(10,0)), sg.pin(sg.Button("Water"))],
        [sg.Graph((400, 400), (0, 0), (400, 400), background_color='white', key='-SCENE2-GRAPH-')]
        
    ]
    return layout

def draw_green_rectangle(window):
    graph = window['-SCENE2-GRAPH-']
    graph.Erase()
    graph.DrawRectangle((10,10), (390, 390), line_color='black', fill_color='green')
    graph.DrawRectangle((10, 350), (40, 280), line_color='black', fill_color='white')
    