// mean.cpp

#include <iostream> 
using namespace std;

double arrayMean(double a[], int n)
{
    // Find sum of array element
    double sum = 0;
    for (int i=0; i<n; i++)
       sum += a[i];
 
    return sum/n;
}

int main()
{
    double numbers[] = {10.0, 2.0, 4.0, 7.0, 9.0, 3.0, 9.0, 8.0, 6.0, 7.0};
    cout << arrayMean(numbers, 10) << endl;

    return 0;
}