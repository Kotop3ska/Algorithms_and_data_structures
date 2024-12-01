/*Дан список целых чисел. Выведите все элементы этого списка в порядке невозрастания значений.
Выведите новый список на экран. Решите эту задачу при помощи алгоритма сортировки выбором.
Решение оформите в виде функции SelectionSort(A).
В алгоритме сортировки выбором мы находим наибольший элемент в списке и ставим его на первое место, 
затем находим наибольший элемент из оставшихся и ставим его на второе место и т.д.*/


#include <iostream>
#include <vector>
using namespace std;


void SelectionSort(vector<int>& A) {
    int n = A.size();
    int key;
    int ind;
    for (int i = 0; i < n - 1; i++) {
        key = A[i];
        ind = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[ind]) {
                ind = j;
                key = A[j];
            }
        }
        if (i != ind) {
            swap(A[i], A[ind]);
        }

    }
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main() {
    vector <int> A;
    int x;
    while (cin >> x){
        A.push_back(x);
    }


    SelectionSort(A);

    return 0;
}
