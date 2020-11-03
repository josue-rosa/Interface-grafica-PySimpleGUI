import PySimpleGUI as psg

psg.theme('Dark Blue')

layout = [
    [psg.Text('O limite de velocidade da via é de 80Km/h.\nO valor é de 123,50 por Km ultrapassado.')],
    [psg.Text('Informe a velocidade em Km/h '), psg.Input(key='-multa-', size=(13, 1))],
    [psg.Button('Calcular Multa', disabled_button_color=None), psg.Button('Sair')],
    [psg.Output(size=(38, 10))]
]

window = psg.Window('Calculadora de multas', layout, resizable=True, margins=(10, 10))

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED or event == 'Sair':
        break
    if event == 'Calcular Multa':
        velocidade = values['-multa-']
        if velocidade == '':
            psg.popup_notify('por favor, entre com dados para calculo da multa', title='Notificação')
        else:
            velocidade = float(values['-multa-'])
            if velocidade > 80:
                calculo = (velocidade - 80) * 123.50
                from time import sleep
                print('Aguarde...calculando')
                sleep(2)
                print(f'Você foi multado! \nEfetue o pagamento de R$ {calculo:.2f}')
            else:
                print('Muito bem. Você não foi multado. \nDirija sempre com cinto de segurança')

"""
velocidade = float(input('Informe a velocidade do veículo em Km/h '))

if velocidade > 80:
    calculo_da_multa = (velocidade - 80) * 123.50
    print(f'Você foi multado em R$ {calculo_da_multa:.2f}')

print('Dirija sempre com cinto de segurança')
"""