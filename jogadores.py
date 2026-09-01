from os.path import exists
from telas import titulo, linha
from modulos import ler_opcao, ler_texto

ARQUIVO = 'jogadores.csv'


#
# ARQUIVO : jogadores.py (pasta fliperama)
# Disciplina: Pensamento Computacional, Algoritmos e Programacao (2026-PCAP)
# Aula : 22 MeuApp v2.0: o cadastro de jogadores
# Autor : Samuel Ribeiro da Cruz
# revisado : Aula 23 - validacao de campo vazio e documentação
# Conceitos: Registro como lista de campos, cadastro como lista
# 1 de listas, cadastrar, listar, buscar, alterar,excluir, persistencia em arquivo.csv
#
#
# O QUE ESTE ARQUIVO E
#
#
#  A quarta gaveta do projeto. O telas.py cuida do que APARECE,
#  o modulos.py cuida do que o programa PERGUNTA, o placar.py 
#  cuida de quantas partidas cada jogo teve, e o jogadores.py 
#  cuida de QUEM jogou.
#
# O REGISTRO
#
#Cada jogador e uma lista de tres campos, sempre nesta ordem:
#indice -> apelido | 1 -> nome 2 -> partidas
#E o cadastro e uma lista dessas listas.


def cadastrar(jogadores):
    '''
    Pergunta apelido e nome e acrescenta um jogador ao cadastro.
    
    Nao devolve nada: o cadastro muda no lugar.
    '''
    titulo('NOVO JOGADOR')

    apelido = ler_texto('Apelido (sem espacos): ').lower()
    nome = ler_texto('Nome completo')

    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastrado.')
    linha()


def listar(jogadores):
    titulo('top 10 jogadores')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastrado ainda.')
    else:
        ranking = sorted (jogadores, key=lambda j: int(j[2]), reverse=True)

    for i in range(len(ranking[:10])):
        print(str(i + 1).rjust(2) + '.' + ranking[i][0].ljust(6) + ' | ' +
              ranking[i][1].ljust(18) + ' | ' + ranking[i][2].rjust(3) + ' partidas')


    linha()


def buscar(jogadores, apelido):
    '''
    Procura um apelido no cadastro e diz ONDE ele esta.
    
    Parametros:
        jogadores (list) - o cadastro inteiro
        apelido   (str) - o apelido procurado, em minusculas
        
    Retorno:
        int - a posicao do jogador na lista, ou -1 se não achar
    '''
    for i in range(len(jogadores)):
        if jogadores[i][0] == apelido:
            return i

    return -1


def alterar(jogadores):
    listar(jogadores)

    apelido = input('Apelido de quem vai mudar de nome: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguem com esse apelido.')
    else:
        print('nome atual: ' + jogadores[i][1])
        jogadores[i][1] = ler_texto('Nome novo: ')
        print('Pronto. Agora e ' +  jogadores[i][1] + '.')

    linha()


def excluir(jogadores):
    '''
    pergunta o jogador que você quer excluir
    
    se o jogador estiver cadastrado ele apaga de jogadores.csv permanentemente

    pede a confirmação antes
    '''
    listar(jogadores)

    apelido = input('Apelido de quem vai sair do cadastro: ').strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print('Não achei ninguém com esse apelido.')
    else:
        print('Vou apagar o cadastro de ' + jogadores[i][1] + '.')
        print('[1] Confirmar')
        print('[2] Deixar como está')
        certeza = ler_opcao('Sua escolha', ['1', '2'])

        if certeza == '1':
            jogadores.pop(i)
            print('Cadastro apagado.')
        else:
            print('Nada foi apagado')

    linha()


def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, 'w')

    for jogador in jogadores:
        arquivo.write(jogador[0] + ',' + jogador[1] + ',' + jogador[2] + '\n')

    arquivo.close()


def carregar_jogadores():
    if not exists(ARQUIVO):
        return []
    
    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    lidos = []
    for linha_lida in linhas:
        campos = linha_lida.strip().split(',')
        lidos.append(campos) 

    return lidos     


def menu_jogadores(jogadores):
    while True:
        titulo('CADASTRO DE JOGADORES')
        print('[1] Cadastrar jogador')
        print('[2] Listar jogadores')
        print('[3] Alterar nome')
        print('[4] Excluir jogador')
        print('[0] Voltar ao fliperama')
        linha()

        opcao = ler_opcao('sua escolha', ['0', '1', '2', '3', '4'])

        if opcao == '0':
            break
        elif opcao == '1':
            cadastrar(jogadores)
        elif opcao == '2':
            listar(jogadores)
        elif opcao == '3':
            alterar(jogadores)
        else:
            excluir(jogadores)