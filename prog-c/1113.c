/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1041
Autor       : Samuel Ribeiro da Cruz
LIAC        : verifica a ordem dos números 
*/

#include <stdio.h>

int main() {
    int x, y;
    
    scanf("%d %d", &x, &y);
    
    while (x != y) {
        if (x < y) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
        scanf("%d %d", &x, &y);
    }
    
    return 0;
}
