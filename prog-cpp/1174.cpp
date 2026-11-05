/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1174 - Selecao em Vetor I
 * Autor     : Samuel Ribeiro da Cruz
 * LIAC      : Le 100 numeros reais num vector e imprime cada posicao cujo
 *             valor e menor ou igual a 10, com uma casa decimal.
 */
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    vector<double> a;
    double x;
    int i, qtd;

    for (i = 0; i < 100; i++) {
        cin >> x;
        a.push_back(x);
    }

    qtd = a.size();
    cout << fixed << setprecision(1);
    for (i = 0; i < qtd; i++) {
        if (a[i] <= 10) {
            cout << "A[" << i << "] = " << a[i] << endl;
        }
    }

    return 0;
}