#Disciplina : Pensamento Comptacional, Algoritmos e Programação (PCAP)
#Projeto : Jogo "Pedra-Papel-Tesoura"
#Arquivo : ppt.py
#Autor : Samuel Ribeiro da Cruz
#Data : 16.06.2026

import random

opcoes = ["pedra", "papel", "tesoura"]
jogada_maquinha = random.choice(opcoes)

entrada = input("Sua jogada (pedra, papel ou tesoura): ")
jogada_jogador = entrada.lower().strip()

if jogada_jogador not in opcoes:
    print("Jogada inválida! Digite pedra, papel ou tesoura.")
else:
    print("Você jogou:", jogada_jogador)
    print("A máquina jogou:", jogada_maquinha)