// squareref.cpp

#include <iostream> 
using namespace std;

void squareRef(double &num) 
{
     num *= num;
}

int main()
{
    double val = 4;
    squareRef(val);
    cout << val << endl;
}