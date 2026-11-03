/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1234 - Sentenca Dancante
Autor       : Samuel Ribeiro da Cruz
LIAC        : Le linhas de texto ate o fim da entrada. Alterna maiusculas e minusculas comecando por maiuscula, sem contar os espacos na alternancia, e imprime a linha resultante.

*/
#include <iostream>
#include <string>
using namespace std;

int main() {
    string frase;
    int i;
    bool maiuscula;

    while (getline(cin, frase)) {
        maiuscula = true;
        for (i = 0; i < (int)frase.size(); i++) {
            if (frase[i] == ' ') {
                continue;
            }
            if (maiuscula) {
                frase[i] = toupper(frase[i]);
            } else {
                frase[i] = tolower(frase[i]);
            }
            maiuscula = !maiuscula;
        }
        cout << frase << endl;
    }

    return 0;
}