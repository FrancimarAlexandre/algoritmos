#include <iostream>

using namespace std;

int fibonacciRercu(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1 || n == 2)
    {
        return 1;
    }
    return fibonacciRercu(n - 1) + fibonacciRercu(n - 2);
}

int fibonacciIterativo(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1 || n == 2)
    {
        return 1;
    }
    int a = 0;
    int b = 1;
    int c;
    for (int i = 2; i <= n; i++)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
int main()
{

    cout << fibonacciRercu(35) << endl;
    cout << "\n"
         << endl;
    cout << fibonacciIterativo(35) << endl;
    return 0;
}