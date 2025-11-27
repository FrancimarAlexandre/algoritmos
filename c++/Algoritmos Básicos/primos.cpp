#include <iostream>
using namespace std;

int primosI(int n)
{
    int divisores = 0;

    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            divisores++;
        }
    }

    if (divisores == 2)
    {
        cout << "o número " << n << " é primo" << endl;
    }
    else
    {
        cout << "o número " << n << " não é primo" << endl;
    }

    return 0; 
}

int main()
{
    primosI(856); 
    return 0;
}
