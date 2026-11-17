# Fliperama em C (MeuApp v3.0)

## O que é
Fliperama de terminal em C com menu, cadastro de jogadores e o jogo "Adivinhe o Número" (de 1 a 100), feito para a disciplina 2026-PCAP.
É a versão em C do meu programa em Python (`jogadores.py`), com os jogadores salvos em arquivo entre uma execução e outra.

## Como compilar e rodar
```bash
gcc -Wall fliperama.c -o fliperama
./fliperama
```

## Arquivos
- `fliperama.c`: programa completo (menu, cadastro, jogo, leitura e gravação do arquivo).
- `jogadores.csv`: um jogador por linha, sem cabeçalho; a 1ª coluna guarda o apelido e a 2ª o número de partidas jogadas (ex.: `samuel,3`).

## Python x C: o que mudou

| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guardar um jogador | `jogadores.append(novo)` (L.45) | `strcpy(apelidos[qtd], novo)` (L.86) |
| comparar apelidos | `==` (L.79) | `strcmp(...) == 0` (L.62) |
| abrir sem arquivo | `exists(ARQUIVO)` (L.144) | `fopen == NULL` (L.152) |

## O que o C me obrigou a decidir
No Python a lista crescia sozinha e as strings tinham qualquer tamanho. No C tive de fixar `CAPACIDADE` (50 jogadores) e `TAM_APELIDO` (20 letras) nas linhas 15 e 16, e limitar a leitura com `%19s` (L.52) para o apelido caber no vetor.

## Autoavaliação

| Critério | Conceito que espero "C" | Onde se prova (arquivo e linha) |
| 1. Estrutura, compilação e Git | | `fliperama.c` (cabeçalho L.1-17, `main` L.173) |
| 2. Cadastro: menu, funções e vetores | | `fliperama.c`: `mostrar_menu` L.162, `cadastrar` L.69, `listar` L.92, vetores L.174-175 |
| 3. Jogo e partidas | | `fliperama.c`: `jogar_adivinhe` L.104, contagem de partidas L.116 |
| 4. Persistência | | `fliperama.c`: `salvar` L.134, `carregar` L.148 |
| 5. Documentação e comparação | | `README.md` (tabela Python x C) |

usei o claude ai para me ajudar a achar as linhas do python pro readme e para escrever algumas partescd .