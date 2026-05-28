#disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
#Projeto : Jogo "Adivinhe o número" 
#Arquivo : adivinhe.py
#autor : Samuel RIbeiro da Cru
#data : 28/05/2026

import random

#sorteamos um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

#pedimos um palpite
palpite = int(input("Digite um número de 1 a 10:"))

#comparamos o palpite com o número secreto
if palpite == numero_secreto:
    print("Acertou! O número era", numero_secreto)
elif palpite < numero_secreto:
    print("Muito baixo! Tente um número maior.")
else:
    print("Muito alto! Tente um número menos.")