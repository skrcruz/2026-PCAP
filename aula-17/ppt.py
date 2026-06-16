#Disciplina : Pensamento Comptacional, Algoritmos e Programação (PCAP)
#Projeto : Jogo "Pedra-Papel-Tesoura"
#Arquivo : ppt.py
#Autor : Samuel Ribeiro da Cruz
#Data : 16.06.2026

import random

# 1) as três jogadas possíveis, guaradadas como texto(strings) numa lista
opcoes = ["pedra", "papel", "tesoura"]

# 2) O computador sorteia uma jogada de dentro da lista
jogada_maquinha = random.choice(opcoes)

# 3) Pedimos a jogada do jogador
jogada_jogador = input("Sua jogada (pedra, papel ou tesoura): ")

# 4) Mostramos as duas jogadas deste primeiro teste
print("Você jogou:", jogada_jogador)
print("A máquina jogou:", jogada_maquinha)