/*
На прямой расположены стойла, в которые необходимо расставить коров так, 
чтобы минимальное расcтояние между коровами было как можно больше.

Входные данные
В первой строке вводятся числа 𝑁 (2<𝑁<10001) – количество стойл и 𝐾 (1<𝐾<𝑁) – количество коров. 
Во второй строке задаются 𝑁 натуральных чисел в порядке возрастания – координаты стойл (координаты не превосходят 10^9)

Выходные данные
Выведите одно число – наибольшее возможное допустимое расстояние.
*/

#include <iostream>
#include <vector>


using namespace std;

bool good(const vector<int>& boxes, int k, int r) 
{
    int cows_count = 1;
    int last_box = boxes[0];
    for (int i = 1; i < boxes.size(); ++i) {
        if (boxes[i] - last_box >= r) {
            cows_count++;
            last_box = boxes[i];
        }
    }
    return cows_count >= k;
}

int main() 
{
    int n, k;
    cin >> n >> k;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) 
    {
        cin >> a[i];
    }

    int l = 0;
    int r = a[n - 1] - a[0] + 1;

    while (r - l > 1) {
        int m = (l + r) / 2;
        if (good(a, k, m)) 
            l = m;
        else 
            r = m;
    
    }

    cout << l << endl;

    return 0;
}