// try-parse.cpp

#include <iostream> 
#include <string>
using namespace std;

bool tryParse(string s, int &n) 
{
    try {
        n = stoi(s, nullptr, 10);
        return true;
    }
    catch(exception e) {
        return false;
    }
}

int main()
{
    string values[] = {"", "160519", "9432.0", "16,667",
                            "   -322   ", "+4302", "(100);", "01FA" };

    for (int i = 0; i < 8; i++) {
        string value = values[i];
        int number;

        if (tryParse(value, number))
            cout << "Converted " << value << " to " << number << endl;
        else
            cout << "Attempted conversion of " << value << " failed" << endl;
    }

    return 0;
}