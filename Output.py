import PySimpleGUI as Sg

Sg.theme('Dark Amber')

layout = [
    [Sg.Text('File Browser W Output'), Sg.Text(size=(12,1), key='-OUTPUT-')],
    [Sg.Input(key='-IN-')],
    [Sg.Button('Show'), Sg.Button('Exit')]
]
window = Sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True)
'''
No código acima, foi usado "no_titlebar" para tirar a barre de tutulo da janela. 
No entanto, uma boa opção seria incluir o "grab_anywhere" para poder mover a janela. Se não houver esta 
opção, teria que fechar a janela pelo Gerenciador de tarefas.
keep_on_top é usado para manter esta janela sobre as outras se forem criadas.
'''


while True:
    event, values = window.read()
    print(event, values)
    if event == Sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])

window.close(); del window  # Boa pratica é usar o del window
