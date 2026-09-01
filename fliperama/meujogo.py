#
# ARQUIVO: meujogo.py (pasta fliperama)
# Disciplina:Pensamento Computacional, Algoritmos e Programacao (2026-PCAP)
#
# Aula: 23 o jogo autoral do meu fliperama
# Autor: [Samuel Ribeiro da Cruz]
# Conceitos: Reuso de modulo proprio, funcao sem retorno, entrada validada, contagem de partidas
#
import random
from telas import linha, titulo


def jogar_meujogo():
    '''
    Você pergunta algo e ele responde: sim, não ou talvez
    '''
    titulo('VIDENTE')

    respostas = ["Sim", "Não", "Talvez"]

    while True:
        pergunta = input("\nFaça uma pergunta (ou digite 'sair'): ")

        if pergunta.lower() == "sair":
            print("Até mais!")
            break

        resposta = random.choice(respostas)

        print(" Resposta:", resposta)
        linha()
    linha()