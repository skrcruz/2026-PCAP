#disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
#Projeto : Jogo "Adivinhe o número" 
#Arquivo : adivinhe.py
# autor : Samuel RIbeiro da Cru
#data : 28/05/2026

import random

#sorteamos um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

#pedimos um palpite
palpite = int(input("Digite um número de 1 a 10:"))

#mostramos o resultado do primeiro teste
print("Você chutou:", palpite)
print("O número ecreto era:", numero_secreto)