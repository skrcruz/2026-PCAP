/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1041
Autor       : Samuel Ribeiro da Cruz
LIAC        : recebe um numero e devolve todos os valores pares até ao quadrado
*/

#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);

    for (i = 2; i <= n; i = i + 2) {
        printf("%d^2 = %d\n", i, i * i);
    }

    return 0;
}
