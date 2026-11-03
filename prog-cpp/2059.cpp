/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 2059 - Par ou Impar?
Autor       : Samuel Ribeiro da Cruz
LIAC        : Le P, J1, J2, R e A. Se o Jogador 1 pediu para dobrar e o Jogador 2 recusou, o Jogador 1 ganha. Caso contrario, a paridade de J1 + J2 decide o vencedor conforme a escolha de P.

*/
#include <iostream>
using namespace std;

int main() {
    int p, j1, j2, r, a;

    cin >> p >> j1 >> j2 >> r >> a;

    if (r == 1 && a == 0) {
        cout << "Jogador 1 ganha!" << endl;
    } else if (((j1 + j2) % 2 == 0) == (p == 1)) {
        cout << "Jogador 1 ganha!" << endl;
    } else {
        cout << "Jogador 2 ganha!" << endl;
    }

    return 0;
}