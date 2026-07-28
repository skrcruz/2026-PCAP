# Correção para idade exata (18 anos)
idade = int(input("Sua idade: "))
if idade == 18: # aqui estava o erro, tinha um recebe ao invés de igual
    print("Voce tem exatamente 18 anos!")
else:
    print("Voce nao tem 18 anos.")
