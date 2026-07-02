# Entrada:
1 - int(input("Sua jogada de 1 a 5:"))
2 - input("Par ou impar?:")
3 - as entradas se repetem

# Saída:
1 - print("Jogada inválida!")
2 - print("Placar -> Você:", pontos_jogador, "Máquina:", pontos_maquina)
3 - print("--- Rodada", rodada, "---")

# Operadores:
1 - aposta == "par":
2 - aposta == "impar":
3 - (jogada_jogador + jogada_maquina) % 2 == 0:

# Sub-rotinas:
1 - random.randint(1, 5)
2 - def quem_venceu(soma, aposta):
3 - 

# Condição:
1 - if soma % 2 == 0:
        paridade = "par"
2 -  else:
        paridade = "impar"
3 - if aposta == "par":
            pontos_jogador = pontos_jogador + 1

# Repetição:
1 - for rodada in range(1,6):
2 - 
3 - 

# Variáveis:
1 - pontos_jogador = 0
2 - pontos_maquina = 0
3 - soma = jogada_maquina + jogada_jogador % 2