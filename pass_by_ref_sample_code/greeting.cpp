// greeting.cpp

#include <iostream> 
#include <string>
using namespace std;

string greet(string name, int &counter)
{
    string greeting = "Hi, " + name + "!";
    counter++;
    return greeting;
}

int main()
{
    int count = 0;

    cout << greet("Alice", count) << endl;
    cout << "Count is " << count << endl;
    cout << greet("Bob", count) << endl;
    cout << "Count is " << count << endl;

    return 0;
}
