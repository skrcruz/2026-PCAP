# Conserto 6: menu de escolhas
jogos = ["Adivinhe o Numero", "Pedra-Papel-Tesoura", "Par ou Impar"]
opcao = int(input("Escolha o jogo (1, 2 ου 3): "))
print("Voce escolheu:", jogos [opcao - 1]) # precisa do -1 pois o python começa a contar as listas do 0 e não do 1