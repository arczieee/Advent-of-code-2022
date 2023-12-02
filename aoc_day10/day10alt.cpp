#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

// signal strength = cycle number * value of x
using namespace std;

string myText;

ifstream fileReader("test.txt");

int countCycle = 0;
int registerVal = 1;

int result = 0;

string delimiter = " ";
string token,temp;
int foundAt = 0;
int i = 0;
int row = 0;
int column = 0;



int main(){

    int a[6][40];
    for (int i=0;i<6;i++)
    {   
        for(int j=0;j<40;j++)
        {   
            a[i][j]=0;
        }
    }
    while (getline(fileReader,myText))
    {
        //cout << myText << endl;

        if(myText.rfind("noop") != string::npos)
        {
            cout << "sprite = " << column << "\t register value = " << registerVal << endl;
            //if((registerVal>(countCycle-2))&&(registerVal<(countCycle+2)))
            if((registerVal>(column-2))&&(registerVal<(column+2)))
            {
                a[row][column] = 1;
                
            }

            countCycle++;
            column++;

            if ((countCycle == 39)||(countCycle == 79)||(countCycle == 119)||(countCycle == 159)||(countCycle == 199)||(countCycle == 239))
            {
                cout << "reset    " << countCycle << endl;
                row++;
                column = 0;
                cout << row << endl;
            }
        }
        else
        {
            cout << "sprite = " << column << "\t register value = " << registerVal << endl;
            temp = "";
            i = myText.find(delimiter);
            while (i < myText.length())
            {
                temp = temp+myText.at(i);
                i++;
            }
            //if((registerVal>(countCycle-2))&&(registerVal<(countCycle+2)))
            if((registerVal>(column-2))&&(registerVal<(column+2)))
            {
                a[row][column] = 1;
            }

            countCycle++;
            column++;

            if ((countCycle == 39)||(countCycle == 79)||(countCycle == 119)||(countCycle == 159)||(countCycle == 199)||(countCycle == 239))
            {
                cout << "reset    " << countCycle << endl;
                row++;
                column = 0;
                cout << row << endl;
            }
            //if((registerVal>(countCycle-2))&&(registerVal<(countCycle+2)))
            if((registerVal>(column-2))&&(registerVal<(column+2)))
            {
                a[row][column] = 1;
            }

            countCycle++;
            column++;

            if ((countCycle == 39)||(countCycle == 79)||(countCycle == 119)||(countCycle == 159)||(countCycle == 199)||(countCycle == 239))
            {
                cout << "reset    " << countCycle << endl;
                row++;
                column = 0;
                cout << row << endl;
            }

            registerVal = registerVal+stoi(temp);
        }
    }

    for (int i=0;i<6;i++)
    {
        for(int j=0;j<40;j++)
        {
            cout << a[i][j];
        }
        cout << "\n";
    }

    cout << "Register value after six cycles = "<< result <<endl;

    return 0;
}