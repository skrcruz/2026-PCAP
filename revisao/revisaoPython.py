# 1. váriaveis
# guarda os dados que são enviados para a máquina (usa o sinal de =)
numero = 3

# 2. operadores
# fazem operações com os números dados a máquina, que poder ser váriaveis ou não, pode ser 
"""
+ soma
- subtração
* multiplicação
/ divisão
// divisão inteira
% resto
** potenciação
== igual
> menor que
< maior que
>= menor igual
<= maior igual
!= diferente"""
print (1 > 3)

# 3. entrada de dados
# é o modo que a máquina recebe os dados do usuário que esta utilizando o programa, podendo ser string,inteiros,flutuantes ou booleanos (esse valor pode ser guardado em uma váriavel)
numero2 = int(input("diga um número de 1 a 10:"))

# 4. saida de dados
# é a reposta de computador para o usuário, sempre é string.
print("um numero")

# 5. estrutura de repetição
# repete o código sem precisar reescreve-lo várias vezes. pode ser por uma condição, com o while ou um número exato de repetições com for
for s in range(2):
    print ("👍")

# 6. estrutura de condição
# verifica se a informação condiz ou não com o que o código está requerindo, usa if, elif, else
if 1 <= numero2 <= 3:
    print("✅​")
elif 4 <= numero2 <= 7:
    print("🍁")
else:
    print("🪉")


#código juntando tudo
numeronormal = int(input("escreva um número normal:")) # variável e entrada de dados

for s in range(numeronormal): # estrutura de condição
    print(f"você fez eu escrever {numeronormal} vezes") #saída de dados

if numeronormal < 30: #estrutura de condição e operadores
    print("isso foi bom​​🤓​")
else:
    print("isso não foi bom​🙄​​")