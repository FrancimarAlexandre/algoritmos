#include <iostream>

using namespace std;

int mcmR(int n, int m, int i = 1)
{
    if ((n * i) % m == 0)
    {
        return n * i;
    }
    return mcmR(n, m, i + 1);
}

int mcmI(int n, int m, int i = 1)
{
    while (true)
    {
        if ((n * i) % m == 0)
        {
            return n * i;
        }
        i += 1;
    }
}
int main()
{
    cout << mcmR(2, 12) << endl;
    cout << "\n"
         << endl;
    cout << mcmI(32, 13) << endl;

    return 0;
}