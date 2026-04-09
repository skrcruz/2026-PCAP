'''
problema 1019 beecrowd
Estudantes: Samuel Ribeiro da Cruz
Data; 2026.04.09
'''

#Objetivo; Converter Segundos em um tempo em horas, minutos e segundos.

#Analise LIAC
#Entrada:A Entrada será o número em segundos
#Operações:Irá fazer o cálculo para converter apenas segundos nas outras unidades
#Saída:Mostra o resultado já calculado no formato horas:minutos:segundos

N = int(input())
#recebe o número de segundos

h = N // 3600
#faz o cálculo das horas

N = N % 3600
# são os segundos que sobraram após calcular as horas

m = N // 60
#calcula os minutos sendo dos segundos que sobraram das horas

s = N % 60
#são os segundos que sobram após retirar os minutos

print(f"{h}:{m}:{s}")