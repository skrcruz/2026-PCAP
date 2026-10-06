/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1041
Autor       : Samuel Ribeiro da Cruz
LIAC        : recebe um numero e devolve a tabuada
*/

#include <stdio.h>

int main() {
    int n, i;
    
    scanf("%d", &n);
    
    for (i = 1; i <= 10; i++) 
    {
        printf("%d x %d = %d\n", i, n, i * n);
    }
    
    return 0;
}


