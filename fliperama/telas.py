# ==============================================================
# ARQUIVO    : telas.py  (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 20 
# Autor      : [Samuel Ribeiro da Cruz]
# Data:      : 2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================

# definição da Moldura Caracteres e Tamanho
CAR = '-'
TAM = 60

# Desenha uma linha na tela
def linha():
    print(CAR * TAM)

# Desenha um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()
