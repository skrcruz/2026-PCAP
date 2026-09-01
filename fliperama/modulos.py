# ==============================================================
# ARQUIVO    : modulos.py  (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 20 
# Autor      : [Samuel Ribeiro da Cruz]
# Data:      : 2026.08.04
# Conceitos  : reaproveitamento, validação, função que chama função
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


def ler_texto(mensagem):
    resposta = input(mensagem + ': ').strip()
    while resposta == '':
        print('Não pode ficar em branco! tente de novo.')
        resposta = input(mensagem + ': ').strip()
    return resposta
