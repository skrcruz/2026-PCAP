# Conserto 4: trecho do "Pedra-Papel-Tesoura" (Aula 17)
jogada = input("pedra, papel ou tesoura? ").lower().strip() #faltava o .lower.strip para mudar o texto para o modo adequado para o a máquina receber
if jogada == "pedra" or jogada == "papel" or jogada == "tesoura":
    print("Jogada valida:", jogada)
else:
    print("Jogada invalida!")