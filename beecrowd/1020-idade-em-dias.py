'''
problema 1020 beecrowd
Estudantes: Samuel Ribeiro da Cruz
Data; 2026.04.09
'''

#objetivo ler um idade em dias e converta-la para anos, mês e dia

#Analise LIAC
#Entrada:O número de dias que será convertido para anos, meses e dias
#operação:terei que dividir a quantidade de dais por 365, mandar o restante para ser dividido por 30 e o que sobrar da divisão por 30 para os dias
#SAída:fala quantos anos, meses e dias

D = int(input())
#recebe o número de dias

a = D // 365
#a é a quantidade de anos que foi convertida de dias para anos

D = D % 365 
#vê quantos dias sobraram do ano

m = D // 30
#ccalcula os dias que sobraram em meses

d = D % 30
#mostra os dias que sobraram dos meses

print(f"{a} ano(s)")
#mostra os anos

print(f"{m} mes(es)")
#mostra os meses

print(f"{d} dia(s)")
#mostra os dias