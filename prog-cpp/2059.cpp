/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 2059 - Impar, Par ou Roubo
Autor       : Samuel Ribeiro da Cruz
LIAC        : Le p, j1, j2, r e a. Se houve roubo ou acusacao, aplica as regras de roubo; caso contrario a paridade de j1 + j2 decide o vencedor conforme a escolha de p. Imprime "Jogador 1 ganha!" ou "Jogador 2 ganha!".

*/
#include <iostream>
using namespace std;

int main() {
    int p, j1, j2, r, a;

    cin >> p >> j1 >> j2 >> r >> a;

    if (r == 1 && a == 1) {
        cout << "Jogador 2 ganha!" << endl;
    } else if (r == 1 || a == 1) {
        cout << "Jogador 1 ganha!" << endl;
    } else if (((j1 + j2) % 2 == 0) == (p == 1)) {
        cout << "Jogador 1 ganha!" << endl;
    } else {
        cout << "Jogador 2 ganha!" << endl;
    }

    return 0;
}