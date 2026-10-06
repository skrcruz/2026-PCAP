/*
Problema 1011 Beecrowd
2026.09.22
Samuel Ribeiro da cruz
*/

/*
int == inteiros Positivos e negativos == %d
float == casas decimais P e N ==
Double == casas decimais precisas == %lf*/

#include <stdio.h>

int main(){
    double r=0, v=0;
    scanf("%lf", &r);
    v = (4.0/3)*3.14159*(r*r*r);
    printf("VOLUME = %.3lf\n", v);
    return 0;
}