'''
problema 1018 beecrowd
data: 2026.04.30
estudante:Samuel Ribeiro Da Cruz
'''

# Objetivo: Ler um valor monetário e decompô-lo no MENOR número possível
#           de notas (100, 50, 20, 10, 5, 2, 1) 

# --- ANÁLISE (LIAC) ---
# Entrada: um valor monetário inteiro
# Processamento: separar parte inteira
#               usar divisão inteira (//) para descobrir QUANTAS
# unidades cabem
#               e o resto da divisão (%) para guardar o que SOBROU para
# a próxima troca
# Saída: lista formatada de notas, na ordem do maior para o
# menor valor

n = int(input())
print(f"{n}")
n100 = n // 100;  n = n % 100    # quantas notas de 100 cabem; n vira o
# resto
n50  = n //  50;  n = n %  50    # quantas notas de 50 cabem no que sobrou
n20  = n //  20;  n = n %  20    # quantas notas de 20 cabem no que sobrou
n10  = n //  10;  n = n %  10    # quantas notas de 10 cabem no que sobrou
n05  = n //   5;  n = n %   5    # quantas notas de 5  cabem no que sobrou
n02  = n //   2;  n = n %   2    # quantas notas de 2  cabem no que sobrou
n01  = n                         # o que restou são notas de 1 real

# Saída formatada — exatamente como o juiz online espera 
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n05} nota(s) de R$ 5,00')
print(f'{n02} nota(s) de R$ 2,00')
print(f'{n01} nota(s) de R$ 1,00')