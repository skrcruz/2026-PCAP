/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1041
Autor       : Samuel Ribeiro da Cruz
LIAC        : le 2 inteiros e diz se são multiplos
*/

#include <stdio.h>

int main() {
    int a, b;

    scanf("%d %d", &a, &b);

    if (a % b == 0 || b % a ==0){
        printf("Sao Multiplos\n");
    } else {
        printf("Nao sao Multiplos\n");
    }

    return 0;
}