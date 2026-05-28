#disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
#Projeto : Jogo "Adivinhe o número" 
#Arquivo : adivinhe.py
#autor : Samuel RIbeiro da Cru
#data : 28/05/2026

import random

#preparamos um jogo
numero_secreto = random.randint(1, 10)
chances = 3
acertou = False

#repetimos em quanto houver chances e não tiver acertado
while chances > 0 and not acertou:
    palpite = int(input("Digite um número de 1 a 10:"))

    if palpite == numero_secreto:
        print("Acertou!")
        acertou = True
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")

    chances = chances - 1 #gasta uma chance
    print("Chances restantes:", chances)

#quando o laço termina vemos o que aconteceu
if not acertou:
    print("Suas chances acabaram! O número era", numero_secreto)