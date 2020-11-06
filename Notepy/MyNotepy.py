import PySimpleGUI as psg

# -*- coding: utf-8 -*-
"""
Autor: Josué C. da Rosa
Versão: 0.1

"""

psg.theme('Dark')
# psg.theme('BrownBlue')

largura = 90
altura = 25

bar_menu_layout = (
    ["Editar", ["Converter para MAIÚSCULA", "Converter para Title"]],
    ["Sobre", ["Autor   ", "Créditos"]],
)

layout_window = [
    [psg.MenuBar(bar_menu_layout)],
    [psg.Multiline(font="Roboto 14", size=(largura, altura), right_click_menu=['Contexto', ['Converter para MAIÚSCULA', 'Converter Title']], key="_body_multiline_")],
    [psg.Text('Localização do arquivo: ', size=(largura, 1), key='caminho_arquivo')],
]

window = psg.Window('Notepy - Programa escrito em Python 3', layout_window, resizable=True, margins=(0, 0))
window.read(timeout=1)
window.maximize()
window["_body_multiline_"].expand(expand_x=True, expand_y=True)


def tornar_texto_caixa_alta():
    window["_body_multiline_"].update(value=str(values["_body_multiline_"]).upper())


def tornar_texto_title():
    window["_body_multiline_"].update(value=str(values["_body_multiline_"]).title())


def menu_contexto_title():
    window["_body_multiline_"].update(value=str(values["_body_multiline_"]).title())


def menu_contexto_caixa_alta():
    window["_body_multiline_"].update(value=str(values["_body_multiline_"]).upper())


def autor():
    texto_autor = """
    Nome: Josué C. da Rosa
    
    Orgulhosamente escrito em Python e PySimpleGUI
    
  
    """
    psg.popup(texto_autor, title='Autor', grab_anywhere=True)


def creditos():
    texto_creditos = """
    Eder Cruz
    youtube.com/channel/UCz1ipXWkAYjcS4jie_IKs6g.
    
    Jhonatan Souza - Canal Dev Aprender
    """
    psg.popup(texto_creditos, no_titlebar=False, title='Créditos', grab_anywhere=True)


while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == "Converter para MAIÚSCULA":
        tornar_texto_caixa_alta()
    if event == 'Converter para Title':
        tornar_texto_title()
    if event == "Converter para MAIÚSCULA":
        menu_contexto_caixa_alta()
    if event == "Converter Title":
        menu_contexto_title()
    if event == "Autor   ":
        autor()
    if event == "Créditos":
        creditos()

