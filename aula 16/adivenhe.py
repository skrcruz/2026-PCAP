#disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
#Projeto : Jogo "Adivinhe o número" 
#Arquivo : adivinhe.py
#autor : Samuel RIbeiro da Cru
#data : 28/05/2026

import random

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + "):"))

        if palpite == numero_secreto:
            print("Acertou!")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
        
        chances = chances - 1
        print("Chances restantes:", chances)

    return acertou

#niveis guardados em uma lista de listas
niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10],
]

#menu de escolha de nivel
print("Escolha o nível de dificuldade:")
print("1 - Fácil              (1 a 10, 3 chances)")
print("2 - Médio              (1 a 100, 5 chances)")
print("3 - Impossível         (1 a 1000, 10 chances)")
opcao = int(input("Digite 1, 2 ou 3:"))

#a opção 1 está na posição 0 da lista, por isso o ajuste
nivel = niveis[opcao - 1]

#iniciamos o jogo com a configuração do jogo escolhido
print("Você escolheu o nível:", nivel[0])
venceu = jogar(nivel[1], nivel[2])

if not venceu:
    print("Fim de jogo! Tente um nível mais fácil.")
