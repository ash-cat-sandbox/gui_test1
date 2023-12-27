import PySimpleGUI as sg
import main_layout
import scene2_layout

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
def main():
  

    window = sg.Window('Main Window', main_layout.create_main_layout())

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'New Game':
            layout_scene2 = scene2_layout.create_scene2_layout()
            window.close()
            window = sg.Window('New Game', layout=layout_scene2)
        elif event == 'Back':
           layout_main = main_layout.create_main_layout()
           window.close()
           window = sg.Window('Main Window', layout=layout_main)

    window.close()

if __name__ == '__main__':
    main()