/*
Дан список из 𝑁 (𝑁≤2∗105) элементов,которые принимают целые значения от 0 до 100.
Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.

Примечание
Сложность работы программы должна быть O(n). 
Использование встроенной сортировки(sort, sorted), алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!
*/

#include <iostream>
#include <vector>
using namespace std;

void CountSort(vector<int> &A) {
    int n = A.size();

    vector<int> counter(101);
    for (int i = 0; i < n; i++) {
        counter[A[i]] += 1;
    }
    A.clear();
    int len = 0;
    for (int num = 0; num < 101; num++) {
        for (int i = 0; i < counter[num]; i++){
            A.push_back(num);
        }

    }

    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }


}

int main() {
    vector <int> A;
    int x;
    while (cin >> x){
        A.push_back(x);
    }


    CountSort(A);

    return 0;
}