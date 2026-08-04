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
from modulos import ler_opcao


NOME_DO_DONO = 'Samuel'
OPCOES = ['0', '1']
while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe o Número')
    print('0 - Sair do Fliperama')
    linha()
    opcao = ler_opcao('escolha uma opção: ', OPCOES)

    if opcao == '0':
        print('Até a próxima!')
        break
    elif opcao == '1':
        jogar_adivinhe()
    else:
        print('Opção inválida! Tente novamente.')