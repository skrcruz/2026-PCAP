/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1168 - LED
Autor       : Samuel Ribeiro da Cruz
LIAC        : Le n valores (como string, pois podem ter ate 100 digitos). Soma os LEDs acesos de cada algarismo e imprime no formato "X leds".

*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, i, j, total;
    string valor;
    int leds[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> valor;
        total = 0;
        for (j = 0; j < (int)valor.size(); j++) {
            total += leds[valor[j] - '0'];
        }
        cout << total << " leds" << endl;
    }

    return 0;
}
