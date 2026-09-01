import random

#
# Arquivo   : parimpar.py
# autor     : Samuel Ribeiro da Cruz
# Data      : 26.08.26
# conceitos :
#
from telas import titulo

def jogar_parouimpar():
    titulo('PAR OU IMPAR')
    jogada_maquina = random.randint(1, 5)
    #registra a jogada do jogador
    jogada_jogador = 0
    #registra se você escolheu par ou impar
    soma = jogada_maquina + jogada_jogador % 2
    pontos_jogador = 0
    pontos_maquina = 0


    def quem_venceu(soma, aposta):
        if soma % 2 == 0:
            paridade = "par"
        else:
            paridade = "impar"
        if paridade == aposta:
            return "jogador"
        else:
            return "maquina"   
    
    for rodada in range(1,4):
        print("--- Rodada", rodada, "---")
        #registra um número aleatório de 1 a 5 dado pela máquina
        jogada_maquina = random.randint(1, 5)
        #registra a jogada do jogador
        jogada_jogador = int(input("Sua jogada de 1 a 5:"))
        entrada = input("Par ou impar?:")
        jogada = entrada.lower().strip()
        #válida se a jogada esta nas opções
        aposta = ["par", "impar"]
        #registra se você escolheu par ou impar
        soma = jogada_maquina + jogada_jogador % 2
        if (jogada_jogador + jogada_maquina) % 2 == 0:
            print("par")
            if aposta == "par":
                pontos_jogador = pontos_jogador + 1
            else:
                pontos_maquina = pontos_maquina + 1
        else:
            print("ímpar")
            if aposta == "impar":
                pontos_jogador = pontos_jogador + 1
            else:
                pontos_maquina = pontos_maquina + 1

        if jogada not in aposta:
            print("Jogada inválida!")