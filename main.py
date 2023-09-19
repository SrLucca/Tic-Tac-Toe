import PySimpleGUI as sg
import random
from minimax import jogada_cpu, vitoria


turno = True
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

sg.theme('DarkAmber') 


layout = [  
            [sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='00'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='01'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='02')],

            [sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='10'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='11'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='12')],

            [sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='20'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='21'),
            sg.Button('', image_filename='quadrado.png', button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='22')]
            
            ]


window = sg.Window('Tic Tac Toe', layout, finalize=True)

while True:

    if turno == False:

        try:
            linha, coluna = jogada_cpu(tabuleiro)
        except TypeError:
            sg.popup("Empate!")
            break

        tabuleiro[linha][coluna] = 'O'

        window[f'{linha}{coluna}'].update(image_filename='quadrado_marcado_bola.png')
        if vitoria(tabuleiro, 'X'):
            sg.popup("Vitória do Jogador!")
            break
        if vitoria(tabuleiro, 'O'):
            sg.popup("Vitória da CPU!")
            break
            

        turno = True
    

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event:
        print(f'Jogador x : {event[0]}')
        print(f'Jogador y : {event[1]}')
        window[event].update(image_filename='quadrado_marcado.png')
        tabuleiro[int(event[0])][int(event[1])] = "X"
        turno = False

    
    

window.close()
