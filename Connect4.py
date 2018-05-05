import os
from Jogo import Jogo
from Jogo import bcolors
from minimax import Int_Art

clear = lambda: os.system('cls')

def mainLoop():
    xogao = Jogo()

    while(True):
        clear()
        os.system('cls')
        xogao.imprime()
        xogao.imprime_vez()

        entrada = int(input(bcolors.BOLD + bcolors.VERDE + "Sua vez: "))

        while entrada > 7 or entrada < 0 or xogao.ondeLivre[entrada] < 0:
            entrada = int(input(bcolors.BOLD + bcolors.VERMELHO + "Diga uma coluna válida"))
            if xogao.ondeLivre[entrada] < 0:
                continue

        xogao.coloca_disco(entrada)
        computador = Int_Art(xogao)
        xogao.coloca_disco(computador.minimax_retorno())

        if xogao.alguemGanhou() != 0 or xogao.cheio():
            xogao.imprime_vencedor()
            break


mainLoop()