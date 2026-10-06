/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1041
Autor       : Samuel Ribeiro da Cruz
LIAC        : le os valores e faz a conta para verificar se é um triangulo
*/

#include <stdio.h>

int main() {
    float a, b, c;

    scanf("%f %f %f", &a, &b, &c);

    if (a < b + c && b < a + c && c < a + b) {
        printf("Perimetro = %.1f\n", a + b + c);
    } else {
        printf("Area = %.1f\n", ((a + b) * c) / 2);
    }

    return 0;
}