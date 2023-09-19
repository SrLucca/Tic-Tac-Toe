import random


def vitoria(tabuleiro, jogador):
    # Verifica as linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
            all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    #verifica se todas as linhas e colunas da matriz sao diferentes de ''(vazio)
    return all([cell != ' ' for row in tabuleiro for cell in row])

def minimax(tabuleiro, profundidade, jogador):
    if vitoria(tabuleiro, 'X'):
        return -1
    if vitoria(tabuleiro, 'O'):
        return 1
    if tabuleiro_cheio(tabuleiro):
        return 0

    #jogada CPU
    if jogador == 'O':
        #valor "infinito" negativo
        melhor_valor = -float('inf')

        #percorrendo linhas
        for i in range(3):
            #percorrendo colunas
            for j in range(3):
                #executar jogada se valor no indice [x][y] for vazio ('')
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'O'
                    valor = minimax(tabuleiro, profundidade + 1, 'X')
                    tabuleiro[i][j] = ' '
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor

    #jogada Jogador
    else:
        #valor "infinito" positivo
        melhor_valor = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'X'
                    valor = minimax(tabuleiro, profundidade + 1, 'O')
                    tabuleiro[i][j] = ' '
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def jogada_cpu(tabuleiro):
    melhor_jogada = None
    melhor_valor = -float('inf')

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'O'
                valor = minimax(tabuleiro, 0, 'X')
                tabuleiro[i][j] = ' '

                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (i, j)

    return melhor_jogada