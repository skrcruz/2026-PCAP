# ==============================================================
# ARQUIVO    : main.py  (pasta fliperama)
# Disciplina : Pensamento Computacional, Algoritmos e Programacao
#              (2026-PCAP)
# Aula       : 20 
# Autor      : [Samuel Ribeiro da Cruz]
# Data:      : 2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================

# importar funções de arquivos
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parouimpar
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores, buscar
from meujogo import jogar_meujogo

NOME_DO_DONO = 'Samuel'
OPCOES = ['0', '1', '2', '3', '4', '5']

NOMES_DOS_JOGOS = ['adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Vidente']
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

def mostrar_placar():
    titulo('placar')
    for i in range(4):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('2 - Pedra-Papel-Tesoura')
    print('3 - Par ou Impar')
    print('4 - Vidente')
    print('5 - Jogadores')
    print('0 - Sair do Fliperama')
    linha()
    opcao = ler_opcao('escolha uma opção: ', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        print('Até a próxima!')
        break

    if opcao =='5':
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1
        vezes_jogado[indice] = vezes_jogado[indice] + 1

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao =='3':
            jogar_parouimpar()
        elif opcao =='4':
            jogar_meujogo()
        else:
            print('Opção inválida! Tente novamente.')

    input('Pressione Enter para voltar ao menu...')