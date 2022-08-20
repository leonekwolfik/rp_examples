// square.cpp

#include <iostream> 
using namespace std;

double square(double num) 
{
    return num * num;
}

int main()
{
    int val = 4;
    cout << square(val) << endl;

    return 0;
}