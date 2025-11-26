#include <iostream>

using namespace std;

int fatRerc(int n)
{
    if (n == 1 || n == 0)
    {
        return 1;
    }
    return fatRerc(n - 1) * n;
}
int fatItera(int n)
{
    int result = 1;
    for (int i = 1; i < (n + 1); i++)
    {
        result = result * i;
    }
    return result;
}
int main()
{
    int n = 5;
    cout << fatRerc(n);
    cout << "\n"
         << endl;
    cout << fatItera(n);

    return 0;
}