'''
 Problema 1011 beecrowd
 Estudante: Samuel Ribeiro da Cruz
 data: 2026.04.07
 '''

#o objetivo é calcular a área do círculo dado o raio, código parecido da atividade 1011.


 #Analise LIAC
#entrada: o raio dado para a operação
#processamente: A formula do calculo da área do círculo, que é pi x raio ao quadrado
#saída: a saída é a o resultado da operação, escrito A=(resultado da operação)

R = int(input(""))
#R é o valor do raio, recebido por input e transformado em um valor númerico por int
V = 3.14159 * R ** 2
#V é a operação
print(f"A={V:.4f}")
#é o comando de saída para dar o resultado da operação e uma parte do bloco (:.4f) para ter apenas 4 digitos após a virgula.