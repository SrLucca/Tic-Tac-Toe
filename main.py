import PySimpleGUI as sg
import random
import time
from minimax import ia_minimax

turno = True
tabuleiro_exemplo = [0,0,0,0,0,0,0,0,0]
jogada = 0

sg.theme('DarkAmber') 


layout = [  [sg.Text("Turno:"), sg.Text("Jogador", key="vez")],
            [sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='0'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='1'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='2')],

            [sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='3'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='4'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='5')],

            [sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='6'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='7'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='8')]
            
            ]


window = sg.Window('Tic Tac Toe', layout)

while True:
    

    if turno == False:
        jogada = ia_minimax(tabuleiro_exemplo)

        if jogada == 1:
            sg.popup("Jogador venceu!")
            break
        if jogada == -1:
            sg.popup("Maquina venceu!")
            break
        else:
            pass

        window[str(jogada)].update(image_filename='quadrado_marcado_bola.png')
        tabuleiro_exemplo[int(jogada)] = -1
        turno = True
        window['vez'].update('Jogador')
    

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event:
        window[event].update(image_filename='quadrado_marcado.png')
        tabuleiro_exemplo[int(event)] = 1
        turno = False
        window['vez'].update('Maquina')

    
    

window.close()
