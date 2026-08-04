# ==============================================================
# ARQUIVO    : modulos.py  (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 20 
# Autor      : [Samuel Ribeiro da Cruz]
# Data:      : 2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================


def ler_opcao(mensagem, validas):
    resposta = input(mensagem + ': ').strip()
    while resposta not in validas:
        print('Opção Inválida! Tente Novamente.')
        resposta = input(mensagem + ': ').strip()
    return resposta

def ler_numero(mensagem, minimo, maximo):
    numeros = []
    for n in range(minimo, maximo + 1):
        numeros.append(str(n))
    return int(ler_opcao(mensagem, numeros))
