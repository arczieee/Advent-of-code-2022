#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

// signal strength = cycle number * value of x
using namespace std;

string myText;

ifstream fileReader("input.txt");

int countCycle = 0;
int registerVal = 1;
string token;
int result = 0;

int main(){

    while (getline(fileReader,myText))
    {
        cout << myText << endl;

        if(myText.compare(string("noop")))
        {
            countCycle++;
            if ((countCycle == 20)||(countCycle == 60)||(countCycle == 100)||(countCycle == 140)||(countCycle == 180)||(countCycle == 220))
            {
                result = result+countCycle*registerVal;
            }
        }
        else
        {
            token = myText.substr(0,myText.find(" "));
            countCycle++;
            if ((countCycle == 20)||(countCycle == 60)||(countCycle == 100)||(countCycle == 140)||(countCycle == 180)||(countCycle == 220))
            {
                result = result+countCycle*registerVal;
            }
            countCycle++;
            registerVal = registerVal + stoi(token);
        }
    }

    cout << "Register value after six cycles = "<< registerVal <<endl;

    return 0;
}