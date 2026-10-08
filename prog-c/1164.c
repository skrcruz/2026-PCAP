/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1164
Autor       : Samuel Ribeiro da Cruz
LIAC        : recebe um valor e faz um calculo para decidir se é um número perfeito
*/

#include <stdio.h>

int eh_perfeito(int n) {
    int i, soma = 0;

    for (i = 1; i < n; i++) {
        if (n % i == 0) {
            soma = soma + i;
        }
    }
    return soma == n;
}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);
        if (eh_perfeito(x)) {
            printf("%d eh perfeito\n", x);
        } else {
            printf("%d nao eh perfeito\n", x);
        }
    }

    return 0;
}
