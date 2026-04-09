'''
problema 1008 beecrowd
Estudantes: Samuel Ribeiro da Cruz
Data; 2026.04.09
'''

#Objetivo Calcular o sálario de um funcionario com as horas e sálario por hora e registrar seu número.

# Analise LIAC
#entrada:a entrada é o numero do funcionario, as horas trabalhadas e o salario por hora
#Processamento:Faz as horas trabalhadas x salario por horas
#saída:Mostra o número do funcionario e o calculo do sálario já pronto

N = int(input(""))
#Pega o número do funcionario
H = int(input(""))
#pega as horas trabalhadas do funcionario
S = float(input(""))
#recebe o salario por hora

print(f"NUMBER = {N}")
#mostra o número do fúncionario
print(f"SALARY = U$ {H * S:.2f}")
#mostra o sálario já calculado