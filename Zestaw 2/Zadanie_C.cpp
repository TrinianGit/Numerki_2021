#include <iostream>
#include <fstream>
#include <cstring>
#include "gnuplot_i.hpp"

using namespace std;

ofstream plik ("dat.data");
Gnuplot g1 ("");

void float_precision(int top){
    float x = 1.0/3.0;
    for (int i = 1; i <= top; i++){
        x = (4*x) - 1.0;
        plik << i << " " << x << endl;
    }
    g1.cmd("plot 'dat.data' using 1:2 title 'Float Precision'");
    cin.get();
    wait_for_key();
}


void double_precision(int top){
    double x = 1.0/3.0;
    for (int i = 1; i <= top; i++){
        x = 4*x - 1;
        plik << i << " " << x << endl;
    }
    g1.cmd("plot 'dat.data' using 1:2 title 'Double Precision'");
    cin.get();
    wait_for_key();
}

void ldouble_precision(int top){
    long double x = 1.0/3.0;
    for (int i = 1; i <= top; i++){
        x = 4*x - 1;
        plik << i << " " << x << endl;
    }
    g1.cmd("plot 'dat.data' using 1:2 title 'Long Double Precision'");
    cin.get();
    wait_for_key();
}

int main(){
    string tryb;
    cout << "Podaj tryb ('ldouble', 'double' lub 'float'): ";
    cin >> tryb;
    int top;
    if (!strcmp(tryb.c_str(), "double")){
        cout << "Podaj ilosc iteracji: ";
        cin >> top;
        double_precision(top); 
    }
    else if (!strcmp(tryb.c_str(), "float")){
        cout << "Podaj ilosc itereacji: ";
        cin >> top;
        float_precision(top);
    }
    else if (!strcmp(tryb.c_str(), "ldouble")){
        cout << "Podaj ilosc itereacji: ";
        cin >> top;
        ldouble_precision(top);
    }
}