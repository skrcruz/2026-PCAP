'''
problema beecrowd 1017
Data: 26.04.23
Estudantes: Samuel Ribeiro da Cruz
'''

#objetivo: receber dois interios e transformar em um valor decimal de quantos litros foram gastos

#analise LIAC:
#entrada: entrarão dois valores interios, sinalizando as horas percorridas e a velocidade média
#operações: primeiro multiplicar os 2 valores da entrada e dividi-los por 12
#saída: saira o resultado de litros que foram precisos para realizar está viagem

horas = int(input())
#recebe o valor de horas percorridas
kmh = int(input())
#recebe a velocidade média
kms = (horas * kmh)
#faz a equação da distancia percorrida
print(f"{kms/12:.3f}")
#mostra o resultado da operação