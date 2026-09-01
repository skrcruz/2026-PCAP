# fliperama do Samuel 

Um fliperama de terminal com quatro jogos, placar que não esquece o cadastro dos jogadores. projeto da disciplina PCAP, 1 ano do Técnico em informática do IFPR.

## O que ele faz

- quatro jogos pelo menu: Adivinhe o número, pedra papel tesoura, par ou ímpar e o vidente
- placar que conta quantas vezes cada jogo foi jogado e continua contando
- cadastro de jogadores: cadastrar, listar, alterar e excluir

## como rodar

cd fliperama/
python 3 main.py

## Os arquivos

- main.py - o gabinete: menu, placar e chamadas
- telas.py - ferramentas visuais
- modulos.py - ferramtneas de lógica: as três funções que perguntam e conferem
- placar.py - quantas partidas cada jogo teve
- jogadores.py - quem são os jogadores
- adivinhe.py, ppt.py, parimpar.py - um arquivo por jogo
placar.csv e jogadores.csv - os dados, que nascem sozinhos

a função ler_texto ficou no modulos.py porque é mais fácil de importar as subrotinas e usa-las

## De onde ele veio

- aula 20: os três jogos viraram um programa só, com módulos e menu
- aula 21: entrou o pedra-papel-tesoura e o placar passou a sobreviver
- aula 22: entrou o cadastro de jogadores, com as quatro operações
- aula 23: campo em branco barrado e projeto documentado

## O que ainda não funciona

- nome com vírgula quebra a linha do arquivo, porque a vírgula é o separador

## Autoavaliacao

Conceito que eu acho que a minha entrega vale: B

### Mapa do projeto: onde esta cada coisa

| O que | Arquivo | Funcao |
|---|---|---|
| Adivinhe o Numero | `adivinhe.py` | `jogar_adivinhe` |
| Pedra-Papel-Tesoura | `ppt.py` | `jogar_ppt` |
| Par ou Impar | `parimpar.py` | `jogar_parimpar` |
| [NOME DO MEU JOGO] | `meujogo.py` | `jogar_meujogo` |
| Cadastro de jogadores | `jogadores.py` | `menu_jogadores` |
| Ranking Top 10 | `jogadores.py` | `listar` |
| Placar que sobrevive | `placar.py` | `salvar_placar`, `carregar_placar` |

### Criterio por criterio: o nivel e a prova

| Criterio | Nivel | Onde esta a prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura e registro | [B] | [jogadores.py] |
| 2. As quatro operacoes | [B] | [jogadores.py] |
| 3. Busca e indice | [B] | [jogadores.py] |
| 4. Persistencia e primeira execucao | [B] | [placar.py e jogadores.py] |
| 5. Documentacao e autoavaliacao | [B] | [readme.md] |
| 6. Jogo autoral e reuso | [B] | [meujogo.py] |

### Usei IA?

usei para me ajudar a conseguir o conceito B e não estava conseguindo registrar 4 jogos no placar
