/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1041
Autor       : Samuel Ribeiro da Cruz
LIAC        : recebe uma senha fixa e verifica se ela é 2002
*/

#include <stdio.h>

int main() {
    int senha;

    scanf("%d", &senha);

    while (senha!= 2002) {
        printf("Senha Invalida\n");
        scanf("%d", &senha);
    }

    printf("Acesso Permitido\n");

    return 0;
}