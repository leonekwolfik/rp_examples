// pass-by-value.cpp

#include <iostream> 
using namespace std;
void f(int fx)
{
    cout << "Start  f(x):  fx=" << fx << endl;
    fx = 10;
    cout << "End    f(x):  fx=" << fx << endl;
}

int main()
{
    int x = 5;
    cout << "Before f(x):  x=" << x << endl;
    f(x);
    cout << "After  f(x):  x=" << x << endl;
    
    return 0;
}