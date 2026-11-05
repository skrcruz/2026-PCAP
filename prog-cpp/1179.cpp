/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1179 - Array Fill IV
 * Autor     : Samuel Ribeiro da Cruz
 * LIAC      : Le 15 inteiros e separa em dois vectors (pares e impares).
 *             Sempre que um vector chega a 5 elementos, imprime e esvazia.
 *             No final, imprime o que sobrou: primeiro os impares, depois
 *             os pares.
 */
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void mostrar(vector<int> &v, string nome) {
    int i, qtd = v.size();

    for (i = 0; i < qtd; i++) {
        cout << nome << "[" << i << "] = " << v[i] << endl;
    }
}

int main() {
    vector<int> pares, impares;
    int x, i;

    for (i = 0; i < 15; i++) {
        cin >> x;
        if (x % 2 == 0) {
            pares.push_back(x);
            if (pares.size() == 5) {
                mostrar(pares, "par");
                pares.clear();
            }
        } else {
            impares.push_back(x);
            if (impares.size() == 5) {
                mostrar(impares, "impar");
                impares.clear();
            }
        }
    }

    mostrar(impares, "impar");
    mostrar(pares, "par");

    return 0;
}