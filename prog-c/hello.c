/* Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Samuel Ribeiro da Cruz
*/

// importa biblioteca padrão de entrada e saída (printf)
#include <stdio.h>

// dedfino a função principal do tipo int
int main(){
    // printf == Saída --> Mostra na Tela
    // "entre aspas == texto"
    //comando se encerra com ;
    printf("Hello World!\n");

     // Receber 2 valores somar e mostrar o resultado
    // cria as  váriveis
    int A=0, B=0;
    printf("Digite um valor: ");
    //recebe um valor
    scanf("%d", &A);
    printf("digite outro valor: ");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma: %d\n", soma);

    //indica que chegou ao fim da função == retornando 0
    return 0;
}

/*
Para compilar ==
gcc <nome-do-arquivo> -o nome-d-programa

para executar ==
./nome-do-programa
*/