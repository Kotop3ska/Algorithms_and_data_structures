/*
Дан список целых чисел. Отсортируйте его в порядке неубывания значений. Выведите полученный список на экран.
Решите эту задачу при помощи алгоритма сортировки вставкой.Решение оформите в виде функции InsertionSort(A).
В этой задаче нельзя пользоваться дополнительным списком операциями удаления и вставки элементов.
В алгоритме сортировки вставкой в каждый произвольный момент начальная часть массива уже отсортирована.
В решении имеется цикл for i in range(1, len(A)), внутри которого предположении, что элементы списка A[0],A[1], ..., A[i-1]
уже отсортированы, элемент A[i]добавляется в отсортированную часть списка.Для этого находится позиция, 
в которую необходимо вставить элемент A[i], затем осуществляется циклический сдвиг фрагмента уже отсортированной части.
*/


#include <iostream>
#include <vector>
using namespace std;


void InsertionSort(vector<int>& A) {
    int n = A.size();
    int key;
    int ind;
    int j;
    for (int i = 1; i < n; i++) {
        key = A[i];
        j = i;
        while (j >= 1 and A[j - 1] > key) {
            A[j] = A[j - 1];
            j -= 1;
        }
        A[j] = key;
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


    InsertionSort(A);

    return 0;
}
