'''
 Problema 1011 beecrowd
 Estudante: Samuel Ribeiro da Cruz
 data: 2026.04.07
 '''

 #calcular o volume da esfera dado o raio da esfera.

 #Analise LIAC
#entrada: o raio dado para a operação
#processamente: A formula do calculo do volume da esfera, que é 4/3 x pi x raio ao cubo
#saída: a saída é a o resultado da operação, escrito VOLUME = (resultado), que é o volume da esfera

R = int(input(""))
#R é o valor do raio, recebido por input e transformado em um valor númerico por int
V = (4.0/3) * 3.14159 * R ** 3
#V é a operação
print(f"VOLUME = {V:.3f}")
#é o comando de saída para dar o resultado da operação e uma parte do bloco (:.3f) para ter apenas 3 digitos após a virgula.