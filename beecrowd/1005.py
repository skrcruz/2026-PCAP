'''
 Problema 1005 beecrowd
 Estudante: Samuel Ribeiro da Cruz
 data: 2026.04.07
 '''

#o objetivo é cálcular a média de 2 números dados como entrada.

#ENtrada: as duas notas são a entrada, recebidas pelo input
#operação: a média, que tem a operação para fazer a média com as circuntâncias dadas pelo problema
#saída: A média é dada com 5 digitos após o número

A = float(input(""))
#nota 1 recebida como número decimal pelo floar input
B = float(input(""))
#nota 2 recebida como número decimal pelo floar input
M = (3.5 * A + 7.5 * B) / 11
#M é a média já calculada com os fatores de peso já aplicados
print(f"MEDIA = {M:.5f}")
#Já mostra a média escrito Media = (a média) com 5 números após a vírgula