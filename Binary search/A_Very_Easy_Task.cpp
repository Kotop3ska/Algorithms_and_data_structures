/*
Сегодня утром жюри решило добавить в вариант олимпиады еще одну, Очень Легкую Задачу. 
Ответственный секретарь Оргкомитета напечатал ее условие в одном экземпляре, 
и теперь ему нужно до начала олимпиады успеть сделать еще N копий. 
В его распоряжении имеются два ксерокса, один из которых копирует лист за х секунд, а другой – за y. 
(Разрешается использовать как один ксерокс, так и оба одновременно. Можно копировать не только с оригинала, но и с копии.) 
Помогите ему выяснить, какое минимальное время для этого потребуется.

Входные данные
На вход программы поступают три натуральных числа N, x и y, разделенные пробелом (1 ≤ N ≤ 2∙10^8, 1 ≤ x, y ≤ 10).

Выходные данные
Выведите одно число – минимальное время в секундах, необходимое для получения N копий.
*/

#include <iostream>
using namespace std;

bool good(int cnt, int q, int s, long long t) {
    return t / q + t / s >= cnt;
}

int main() {
    long long n, quick, slow;
    cin >> n >> quick >> slow;

    if (quick > slow) {
        swap(quick, slow);
    }

    long long l = 0;
    long long r = (n - 1) * slow;

    while (r - l > 1) {
        long long m = (l + r) / 2;
        if (!good(n - 1, quick, slow, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << r + quick << endl;
    return 0;
}