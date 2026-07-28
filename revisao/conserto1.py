print("=== ADIVINHE O NUMERO ===")
segredo = 7
palpite = int(input("Digite um numero de 1 a 10: ")) #no original falta o int que converte esse valor para inteiro

if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era", segredo)
