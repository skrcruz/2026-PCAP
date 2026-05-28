"""
problema 1035 beecrowd
data: 2026.05.07
estudante: Samuel Ribeiro da Cruz
"""

#problema: fazer um esquema de números com as váriaveis

#analise LIAC
#entrada: 4 números inteiros
#operações: se B > C and A > D and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0
#saída: mostra se os números foram aceitos ou não

A, B, C, D = map(int, input().split())
#recebe as váriaveis 

if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
#faz a operação e ve se está correta
else:
    print("Valores nao aceitos")
#mostra se não estiver correta