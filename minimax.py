def verifica_ganhador(tabuleiro):
    # Verifica linhas
    for linha in range(0, 9, 3):
        if tabuleiro[linha] == tabuleiro[linha + 1] == tabuleiro[linha + 2]:
            if tabuleiro[linha] + tabuleiro[linha + 1] + tabuleiro[linha + 2] == 3:
                return 1
            if tabuleiro[linha] + tabuleiro[linha + 1] + tabuleiro[linha + 2] == -3:
                return -1

    # Verifica colunas
    for coluna in range(3):
        if tabuleiro[coluna] == tabuleiro[coluna + 3] == tabuleiro[coluna + 6]:
            if tabuleiro[coluna] + tabuleiro[coluna + 3] + tabuleiro[coluna + 6] == 3:
                return 1
            if tabuleiro[coluna] + tabuleiro[coluna + 3] + tabuleiro[coluna + 6] == -3:
                return -1

    # Verifica diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] or tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        if tabuleiro[0] + tabuleiro[4] + tabuleiro[8] == 3 or tabuleiro[2] + tabuleiro[4] + tabuleiro[6] == 3:
            return 1
        if tabuleiro[0] + tabuleiro[4] + tabuleiro[8] == -3 or tabuleiro[2] + tabuleiro[4] + tabuleiro[6] == -3:
            return -1

    return False

def minimax(tabuleiro, profundidade, vez):
    resultado = verifica_ganhador(tabuleiro)

    if resultado != False:
        return resultado
    
    if vez == True:
        maiorScore = -1000

        for x in range(0, 8):
            if tabuleiro[x] == 0:
                tabuleiro[x] = 1
                score = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[x] = 0
                maiorScore = max(score, maiorScore)
                

        return maiorScore

    else:
        maiorScore = 1000
        for x in range(0, 8):
            if tabuleiro[x] == 0:
                tabuleiro[x] = -1
                score = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[x] = 0
                maiorScore = min(score, maiorScore)
                
        return maiorScore

def ia_minimax(tabuleiro):

    maiorScore = -1000
    jogada = 0

    for x in range(0, 8):
        if tabuleiro[x] == 0:
            tabuleiro[x] = -1

            score = minimax(tabuleiro, 0, True)
            tabuleiro[x] = 0

            if score > maiorScore:
                maiorScore = score
                jogada = x

    tabuleiro[jogada] = -1

    if verifica_ganhador(tabuleiro) == 1:
        return 1
    if verifica_ganhador(tabuleiro) == -1:
        return -1

    print(jogada)
    print(tabuleiro)
    return jogada

