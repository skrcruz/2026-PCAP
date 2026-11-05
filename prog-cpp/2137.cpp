/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2137 - Biblioteca do Severo
 * Autor     : Samuel Ribeiro da Cruz
 * LIAC      : Le N e depois N codigos de livros num vector. Ordena em ordem
 *             crescente e imprime cada codigo com 4 digitos, um por linha.
 *             Repete ate o fim da entrada.
 */
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

void mostrar(vector<int> &v) {
    int i, qtd = v.size();

    for (i = 0; i < qtd; i++) {
        cout << setfill('0') << setw(4) << v[i] << endl;
    }
}

int main() {
    vector<int> codigos;
    int n, x, i;

    while (cin >> n) {
        codigos.clear();
        for (i = 0; i < n; i++) {
            cin >> x;
            codigos.push_back(x);
        }

        sort(codigos.begin(), codigos.end());
        mostrar(codigos);
    }

    return 0;
}