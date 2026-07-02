# Entrada:
1 - input("Sua jogada: ").lower().strip()
2 - a entrada se repete nas outras rodadas
3 - 

# Saída:
1 - print("--- Rodada", rodada, "---")
2 - print("Inválida! Você perde a rodada.")
3 -  print("Empate!")

# Operadores:
1 - pontos_maquina = pontos_maquina + 1
2 - pontos_maquina == 3:
3 - elif quem == "jogador":

# Sub-rotinas:
1 - resultado(jogada_jogador, jogada_maquina)
2 - random.choice(opcoes)
3 - range(1, 6):

# Condição:
1 -  if jogada_jogador not in opcoes:
        print("Inválida! Você perde a rodada.")
        pontos_maquina = pontos_maquina + 1
2 - else:
        quem = resultado(jogada_jogador, jogada_maquina)
3 - elif quem == "jogador":
            print("Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1

# Repetição:
1 - for rodada in range(1, 6):
2 - if pontos_maquina == 3:
        print("A máquina ganhou!")
        break
3 - if pontos_jogador == 3:
        print("O jogador ganhou!")
        break

# Variáveis:
1 - opcoes = ["pedra", "papel", "tesoura", "lagarto", "spock"]
2 - pontos_jogador = 0
3 - pontos_maquina = 0