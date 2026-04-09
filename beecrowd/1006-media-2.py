'''
problema 1006 beecrowd
Estudantes: Samuel Ribeiro da Cruz
Data; 2026.04.09
'''

#objetivo; calcular a média de 3 notas com pesoso diferentes

#análise LIAC
#Entrada:A entrada serão as 3 notas da média
#operação:Calcula o peso das notas e soma 
#Saída:Mostra a média já pronta, que é tudo dividido por 10

A = float(input())
#recebe a nota 1
B = float(input())
#recebe a nota 2
C = float(input())
#recebe a nota 3
MEDIA = (A * 2 + B * 3 + C * 5) / 10
#é a váriavel que calcula a nota já pronta
print(f"MEDIA = {MEDIA:.1f}")
#mostra a média das notas