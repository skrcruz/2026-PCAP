'''
problema 1007 beecrowd
data: 26.04.16
estudante: Samuel Ribeiro da Cruz
'''

#objetivo: calcular quantos km por litro o carro fez em uma viagem tendo o valor de km e de l

#analise LIAC
#entrada:de entrada se recebe os kilomentros e os litros
#operadores:consumo = km/l
#saída:mostra o consumo já calculado

km = int(input())
#recebe o valor inteiro de kms 

l = float(input())
#recebe um valor decimal de litros

consumo = km / l

print(f"{consumo:.3f} km/l")
#mostra o consumo já calculado com 3 digitos após a virgula