from datetime import date
import PySimpleGUI as psg

psg.theme('DarkAmber')
layout = [
    [psg.Text('Informe o ano que você nasceu', font='Roboto 14'), psg.Input(size=(8, 1), key='ano')],
    [psg.Button('Calcular'), psg.Button('Sair')],
    [psg.Output(size=(46, 4))]
]

window = psg.Window('Calculo de aniversário', layout)

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED or event == 'Sair':
        break
    if event == 'Calcular':
        ano_pessoa = int(values['ano'])  # o retorno era str
        ano_corrente = date.today().year
        print(f'No ano de {ano_corrente}, você completa {ano_corrente - ano_pessoa} anos de idade.')

"""

colocar em uma mensagem e popup

"Todas as grandes coisas têm pequenos começos" Perter Senge
"""
