/*
Problema 1005 Beecrowd
2026.09.22
Samuel Ribeiro da cruz
*/

#include <stdio.h>

int main(){
    double A=0, B=0, m=0;
    scanf("%lf", &A);
    scanf("%lf", &B);
    m = ((A*3.5)+(B*7.5))/11;
    printf("MEDIA = %.5lf\n", m);
    return 0;
}