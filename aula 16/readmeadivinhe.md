entrada:
1 - int(input("Digite 1, 2 ou 3:"))
2 - int(input("Seu palpite (1 a " + str(maximo) + "):"))
3 -

saída:
1 - print("Escolha o nível de dificuldade:")
2 - print("1 - Fácil              (1 a 10, 3 chances)")
3 - print("Você escolheu o nível:", nivel[0])

operadores:
1 - if palpite == numero_secreto
2 - elif palpite < numero_secreto:
3 - nivel = niveis[opcao - 1]

sub-rotinas:
1 - def jogar(maximo, chances):
2 - randint(1, maximo)
3 - while chances > 0 and not acertou:

condição:
1 - if palpite == numero_secreto:
            print("Acertou!")
            acertou = True
2 - elif palpite < numero_secreto:
            print("Muito baixo!")
3 - else:
            print("Muito alto!")

repetição:
1 - while chances > 0 and not acertou:
2 - 
3 - 

varíaveis:
1 - numero_secreto = random.randint(1, maximo)
2 - niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10],
]

3 - chances = chances - 1
