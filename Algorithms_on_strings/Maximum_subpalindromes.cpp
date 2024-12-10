/*
Дана непустая строка, длина которой не превышает 10^6.
Требуется для каждой позиции  символа в строке найти длину наибольшего палиндрома с центром в этом символе.
Строка состоит из букв английского алфавита, большие и маленькие буквы считаются различными.
Ограничение времени - 1 секунда.

Входные данные
Одна строка длины N, 0 < N ≤ 10^6.

Выходные данные
N чисел, разделенные пробелами.
*/


#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> manacher(const string& text) {
    int n = text.size();
    int c = 0, r = 0;
    vector<int> p(n, 0);

    for (int i = 0; i < n; ++i) {
        int mirror = 2 * c - i;

        if (i < r) {
            p[i] = min(r - i, p[mirror]);
        }

        while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && text[i + p[i] + 1] == text[i - p[i] - 1]) {
            p[i]++;
        }

        if (i + p[i] > r) {
            c = i;
            r = i + p[i];
        }
    }

    return p;
}

int main() {
    string text;
    cin >> text;

    vector<int> result = manacher(text);

    vector<int> palindrome_lengths;
    for (int radius : result) {
        palindrome_lengths.push_back(2 * radius + 1);
    }

    for (int len : palindrome_lengths) {
        cout << len << " ";
    }

    return 0;
}
