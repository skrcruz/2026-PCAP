/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1153
Autor       : Samuel Ribeiro da Cruz
LIAC        : recebe um valor N e calcula e imprime o fatorial de N
*/

#include <stdio.h>

int fatorial(int n) {
    int i, resultado = 1;

    for (i = 2; i <= n; i++) {
        resultado = resultado * i;
    }
    return resultado;
}

int main() {
    int n;

    scanf("%d", &n);

    printf("%d\n", fatorial(n));

    return 0;
}