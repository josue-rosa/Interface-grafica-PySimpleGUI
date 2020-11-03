import PySimpleGUI as sg
sg.theme('Default')

# Definindo o que sera inserido dentro da janela/screen/tela
layout = [
    [sg.Text('Hello World')],
    [sg.Text('Are you ready?', font='Courier 12', text_color='blue', background_color='white'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

# Criar a janela, Dei o nome de window mas poderia ser qualquer nome para a variavel
window = sg.Window('Titulo da Janela', layout=layout)  # como layout repete o mesmo nome, eu posso deixar apenas "layout" uma vez. Mas nesse caso, deixei todo o comando.
# Event Loop para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()  # novamente chamado a variavel window. Agora com a função read() para ler os valores da tela
    if event == sg.WIN_CLOSED or event == 'Cancel':  # se o usuário fechar a janela ou clicar em cancelar
        break
    print(f'Voce inseriu: {values[0]}')
print('Fim do programa')
window.close()
