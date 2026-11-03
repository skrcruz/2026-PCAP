/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1011 - Esfera
Autor       : Samuel Ribeiro da Cruz
LIAC        : Le o raio R (real). Calcula o volume da esfera com pi = 3.14159 usando (4/3) * pi * R^3. Imprime no formato "VOLUME = volume", com tres casas decimais e espacos em volta do sinal de igual.

*/
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r;
    double volume;

    cin >> r;
    volume = (4 / 3.0) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

   return 0;
}