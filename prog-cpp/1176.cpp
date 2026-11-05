/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1176 - Fibonacci em Vetor
 * Autor     : Samuel Ribeiro da Cruz
 * LIAC      : Preenche um vector com os 61 primeiros termos de Fibonacci
 *             (de 0 a 60). Le T casos e, para cada N lido, imprime Fib(N).
 */
#include <iostream>
#include <vector>
using namespace std;

void preencher(vector<unsigned long long> &fib) {
    int i;

    fib.push_back(0);
    fib.push_back(1);
    for (i = 2; i <= 60; i++) {
        fib.push_back(fib[i - 1] + fib[i - 2]);
    }
}

int main() {
    vector<unsigned long long> fib;
    int t, n, caso;

    preencher(fib);

    cin >> t;
    for (caso = 0; caso < t; caso++) {
        cin >> n;
        cout << "Fib(" << n << ") = " << fib[n] << endl;
    }

    return 0;
}
