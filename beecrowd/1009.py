'''
 Problema 1009 beecrowd
 Estudante: Samuel Ribeiro da Cruz
 data: 2026.04.07
 '''

#fazer um cálculo para dar 15% de comissão pelo preço vendido pelo vendedor, calculando seu salário total = o bônus

#entrada: os valores como saálario e dinheiro das vendas e o nome
#operação: a porcentagem do valor das vendas para adicionar como uma comissão
#saída:o print mostra o total que o vendedor vai ganhar já pronto, somando a comissão com o sálario.

input("")
#recebe o nome de quem vai receber o sálario e o bônus
S = float(input(""))
#S representa o sálario inicial
V = float(input(""))
#V representa o dinheiro das vendas
C = V*15/100
#representa os 15 por cento das vendas
TOTAL = C+S
#TOTAL é o sálario mais a comissão já prontos
print(f"TOTAL = R$ {TOTAL:.2f}")
#Dá o valor total com apenas 2 digitos após a vírgula