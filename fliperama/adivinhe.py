# ==============================================================
# ARQUIVO    : adivinhe.py  (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 20 
# Autor      : [Samuel Ribeiro da Cruz]
# Data:      : 2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================

# importar bibliotecas e funções e arquivos (módulos)
from random import randint
from telas import titulo, linha
from modulos import ler_numero

def jogar_adivinhe():
    titulo('JOGO ADIVINHE O NÚMERO')
    print('Tente adivinhar o número que estou pensando entre 1 e 10.')
    segredo = randint(1, 10)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = ler_numero('Digite seu palpite', 1, 10)
        tentativas += 1

        if palpite < segredo:
            print('O número secreto é maior. Tente novamente.')
        elif palpite > segredo:
            print('O número secreto é menor. Tente novamente.')
        else:
            acertou = True
    else:
        linha()
        print(f'Parabéns! você acertou o número secreto {segredo} em {tentativas} tentativas.')
