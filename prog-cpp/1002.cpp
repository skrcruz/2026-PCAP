/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1002 - Area do Circulo
 * Autor     : Samuel Ribeiro da cruz
 * LIAC      : Le o raio R (real). Calcula a area com pi = 3.14159 e
 *             imprime "A=area" com quatro casas decimais.
 */
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << "A=" << fixed << setprecision(4) << area << endl;

    return 0;
}