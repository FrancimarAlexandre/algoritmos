#include <iostream>

using namespace std;

int mdcR(int n, int m)
{
    if (!m)
    {
        return n;
    }
    return mdcR(m, n % m);
}

int mdcI(int n, int m)
{
    int t;
    while (m)
    {
        t = n % m;
        n = m;
        m = t;
    }
    return n;
}

int main()
{
    cout << mdcR(75, 30) << endl;
    cout << "\n"
         << endl;
    cout << mdcI(75, 30) << endl;
    return 0;
}