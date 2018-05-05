from Jogo import *
from avaliação import *
PROFUNDIDADEM = 30

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
            valor_no = max(valor_no, self.mini_retorno(contador + 1, alpha, beta))
            if valor_no >= beta:
                return valor_no
            alpha = max(alpha, valor_no)
            self.jogo_copia.retira_disco(i)
        return valor_no


    # def max_retorno(self, contador):
    #     if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:
    #         return pontuacao(self.jogo_copia.tabuleiro)
    #     valor_no = float('-inf')
    #     for i in self.jogo_copia.ondeLivre:
    #         if i == -1:
    #             continue
    #         self.jogo_copia.coloca_disco(i)
    #         valor_no = max(valor_no, self.mini_retorno(contador+1))
    #         self.jogo_copia.retira_disco(i)
    #
    #
    #     return valor_no


#MINI COM PODA
    def mini_retorno(self, contador, alpha, beta):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:
            return pontuacao(self.jogo_copia.tabuleiro)
        valor_no = float('inf')
        for i in self.jogo_copia.ondeLivre:
            if i == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_no = min(valor_no, self.max_retorno(contador + 1, alpha, beta))
            if valor_no <= alpha:
                return valor_no
            beta = min(beta, valor_no)
            self.jogo_copia.retira_disco(i)
        return valor_no


    # def mini_retorno(self, contador):
    #     if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:     # Se o jogo terminou, retorna o resultado final
    #         return pontuacao(self.jogo_copia.tabuleiro)
    #     valor_no = float('inf')
    #     for i in self.jogo_copia.ondeLivre:
    #         if i == -1:
    #             continue
    #         self.jogo_copia.coloca_disco(i)
    #         valor_no = min(valor_no, self.max_retorno(contador+1))
    #         self.jogo_copia.retira_disco(i)
    #     return valor_no
    


    # def minimax_retorno(self):                            # Função que retorna o resultado da busca
    #     profundidade = 0                                  # Nível da profundidade
    #     melhor_jogada = 0                                 # melhor jogada = coluna em que a melhor jogada está
    #     valor_no = float('-inf')                          # Começa com - infinito
    #     for i in range(7):                                # Para cada coluna do tabuleiro
    #         if self.jogo_copia.ondeLivre[i] == -1:              # Verifica se a coluna está cheia
    #             continue                                            # Se estiver, vai para a próxima
    #         self.jogo_copia.coloca_disco(i)                     # Se não estiver coloca um disco nela
    #         valor_filho = self.mini_retorno(profundidade+1)     # valor_filho = jogada seguinte e é chamada a funcao mini
    #         if valor_filho > valor_no:                          # Se o valor do filho > maior pontuação anterior
    #             melhor_jogada = i                                     # Atualiza a melhor casa pra se jogar
    #             valor_no = valor_filho                                # Atualiza a pontuação
    #         self.jogo_copia.retira_disco(i)                           # Tira a peça da coluna atual e vai pra próxima
    #     return melhor_jogada                              # Retorna a coluna da melhor jogada calculada


#PODA ALFA-BETA
    def alfa_beta(self):                                # Função que retorna o resultado da busca
        profundidade = 0                                      # Nível da profundidade
        melhor_jogada = 0                                     # melhor jogada = coluna em que a melhor jogada está
        valor_no = float('-inf')                              # Começa com - infinito
        for i in range(7):                                    # Para cada coluna do tabuleiro
            if self.jogo_copia.ondeLivre[i] == -1:                  # Verifica se a coluna está cheia
                continue                                                # Se estiver, vai para a próxima
            self.jogo_copia.coloca_disco(i)                         # Se não estiver coloca um disco nela
            valor_filho = self.max_retorno(profundidade + 1, float('-inf'), float('inf'))
            if valor_filho > valor_no:
                melhor_jogada = i
                valor_no = valor_filho
            self.jogo_copia.retira_disco(i)
            return melhor_jogada
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
