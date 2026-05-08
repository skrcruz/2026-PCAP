"""
problema 1051 beecrowd
data: 2026.05.07
estudante: Samuel Ribeiro da Cruz
"""

#objetivo: analisar uma quantidade e descobrir a porcentagem de imposto a ser cobrada

#analise LIAC
#entrada: valor do imposto de redna(variavel flutuante ou decimal)
#operações: if elif e else para ver o valor do número e cobrar o imposto
#saída:o valor a ser cobrado de imposto

renda = float(input())
#recebe o valor da renda
imp = 0
#é o valor inicial do imposto
x = renda
#é a variavel diferença entre a renda e a faixa de impostos
if renda > 4500:
    imp += ((renda - 4500) * 0.28)
    x = (x - (renda - 4500))
if renda > 3000:
    imp += ((x - 3000) * 0.18)
    x = (x - (x - 3000))
if renda > 2000:
    imp += ((x - 2000) * 0.08)
    x = (x - (x - 2000))
if renda < 2000:
    print("Isento")
else:
    print(f"R$ {imp:.2f}")
#calcula o imposto de renda