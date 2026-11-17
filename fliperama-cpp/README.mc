# Fliperama em C++ (MeuApp v4.0)

## O que e
Programa de terminal que simula um fliperama: tem um menu, cadastro de jogadores e o jogo "Adivinhe o Numero", que conta quantas partidas cada jogador terminou.
Ele veio do fliperama.c, escrito em C, que foi reescrito em C++ na Aula 32 usando vector, string e referencias.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: codigo-fonte completo do programa (menu, cadastro, jogo e leitura/gravacao do arquivo).
- jogadores.csv: uma linha por jogador, com duas colunas separadas por virgula: o apelido e o numero de partidas.

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 86) | apelidos.push_back(novo) (l. 98) |
| comparar apelidos | strcmp(...) == 0 (l. 62) | == (l. 58) |
| a funcao que cadastra | int cadastrar(..., int qtd) (l. 69) | void cadastrar(... &apelidos, ...) (l. 87) |

## O que o C++ decidiu por mim
Em C eu controlava o tamanho dos vetores e o contador qtd na mao, e o vector cresce sozinho com push_back e sabe seu proprio tamanho.
Em C eu comparava texto com strcmp e copiava com strcpy, e em C++ o string permite usar == e = como com numeros.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | b | fliperama.cpp compila com g++ -Wall e o projeto esta versionado no Git (pasta fliperama-cpp) |
| 2. Cadastro: vectors e referencia | b | fliperama.cpp, l. 87 (vector<string> &apelidos, vector<int> &partidas) e l. 98 (push_back); l. 93 rejeita apelido repetido |
| 3. Jogo e partidas | b | fliperama.cpp, l. 115 (jogar_adivinhe), l. 127 (rand) e l. 143 (soma a partida so quando o jogo termina) |
| 4. Persistencia | b | fliperama.cpp, l. 65 (salvar), l. 74 (carregar), l. 163 (carregar ao iniciar) e l. 179 (salvar ao sair) |
| 5. Documentacao e comparacao | b | README.md: tabela "C x C++" com as linhas dos dois arquivos |