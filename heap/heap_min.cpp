/*
Задача отличается от задачи «Пирамида (максимум)» исключительно тем, что надо извлекать не максимум, а минимум.

Напишите программу, которая будет обрабатывать последовательность запросов таких видов:

CLEAR — сделать пирамиду пустой (если в пирамиде уже были какие-то элементы, удалить все). 
Действие происходит только с данными в памяти, на экран ничего не выводится.

ADD n — добавить в пирамиду число n. Действие происходит только с данными в памяти, на экран ничего не выводится.

EXTRACT — вынуть из пирамиды минимальное значение. Следует и изменить данные в памяти, 
и вывести на экран или найденное минимальное значение, или, если пирамида была пустой, слово "CANNOT" (большими буквами).

Входные данные
Во входных данных записано произвольную последовательность запросов CLEAR, ADD и EXTRACT — каждый в отдельной строке, 
согласно вышеописанному формату.

Суммарное количество всех запросов не превышает 200000.

Выходные данные
Для каждого запроса типа EXTRACT выведите на стандартный выход (экран) его результат (в отдельной строке).
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinHeap
{
    private:
        vector<int> heap;
        
        void shiftUp(int i)
        {
            int p = (i - 1) / 2;
            while (heap[i] < heap[p])
            {
                swap(heap[i], heap[p]);
                i = (i - 1) / 2;
                p = (i - 1) / 2;
            }
        }
        
        void shiftDown(int i)
        {
            while (i * 2 + 1 < heap.size())
            {
                int left = 2 * i + 1;
                int right = 2 * i + 2;
                if (left >= heap.size())
                    return;
                if (right == heap.size())
                    right = left;
                int j = heap[right] < heap[left] ? right : left;
                if (heap[j] < heap[i])
                    swap(heap[i], heap[j]);
                i = j;
            }
        }
        
        public:
            void clear()
            {
                heap.clear();
            }
            
            void insert(int x)
            {
                heap.push_back(x);
                shiftUp(heap.size() - 1);
            }
            
            int extract()
            {
                int removed = heap[0];
                heap[0] = heap.back();
                heap.pop_back();
                shiftDown(0);
                return removed;
            }
            
            bool isEmpty() const
            {
                return heap.empty();
            }
};


int main()
{
    MinHeap h;
    int x;
    string command;
    
    while (cin >> command)
    {
        if (command == "CLEAR")
            h.clear();
        else if (command == "ADD")
        {
            cin >> x;
            h.insert(x);
        }
        else
        {
            if (h.isEmpty())
                cout << "CANNOT" << endl;
            else
                cout << h.extract() << endl;
        }
    }
    return 0;
}
