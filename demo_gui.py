import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text("Your URL"), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='-IN-')],
        [sg.Button("Import"), sg.Button('Exit')]
    ]
    window = sg.Window("URL to PDF", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == "-IN-" and values:
            # Faire quelque chose ici
            pass
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            # Update the "output" text element to be the value of "input" element
            window['-OUTPUT-'].update(values['-IN-'])

    window.close()


if __name__ == '__main__':
    sg.theme('BluePurple')

    main()
