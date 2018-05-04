import copy
from Jogo import *
from avaliação import *
PROFUNDIDADEM = 5

class Int_Art:
    jogo_copia = None

    def __init__(self, jogo_atual):
        self.jogo_copia = copy.deepcopy(jogo_atual)

    def max_retorno(self, contador, alpha, beta):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:
            return pontuacao(self.jogo_copia.tabuleiro)
        valor_no = float('-inf')
        for i in self.jogo_copia.ondeLivre:
            if i == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_no = max(valor_no, self.mini_retorno(contador+1, alpha, beta))
            if valor_no >= beta:
                return valor_no
            alpha = max(alpha, valor_no)
            self.jogo_copia.retira_disco(i)
        return valor_no

    def mini_retorno(self, contador, alpha, beta):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:
            return pontuacao(self.jogo_copia.tabuleiro)
        valor_no = float('inf')
        for i in self.jogo_copia.ondeLivre:
            if i == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_no = min(valor_no, self.max_retorno(contador+1, alpha, beta))
            if valor_no <= alpha:
                return valor_no
            beta = min(beta,valor_no)
            self.jogo_copia.retira_disco(i)
        return valor_no

    """
    def minimax_retorno(self):
        profundidade = 0
        melhor_jogada = 0
        valor_no = float('-inf')
        for i in range(7):
            if self.jogo_copia.ondeLivre[i] == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_filho = self.mini_retorno(profundidade+1)
            if valor_filho > valor_no:
                melhor_jogada = i
                valor_no = valor_filho
            self.jogo_copia.retira_disco(i)
        return melhor_jogada
    """
    def alpha_beta(self):
        profundidade = 0
        melhor_jogada = 0
        valor_no = float('-inf')
        for i in range(7):
            if self.jogo_copia.ondeLivre[i] == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_filho = self.max_retorno(profundidade+1, float('-inf'), float('inf'))
            if valor_filho > valor_no:
                melhor_jogada = i
                valor_no = valor_filho
            self.jogo_copia.retira_disco(i)
        return melhor_jogada
