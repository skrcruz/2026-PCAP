
/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1067
Autor       : Samuel Ribeiro da Cruz
LIAC        : recebe um valor X e imprime todos os numeros impares de 1 ate X
*/

#include <stdio.h>

int main() {
    int x, i;

    scanf("%d", &x);

    for (i = 1; i <= x; i++) {
        if (i % 2 == 1) {
            printf("%d\n", i);
        }
    }

    return 0;
}