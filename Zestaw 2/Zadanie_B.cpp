#include <iostream>
#include <cstring>
#include <vector>
#include <fstream>
#include "gnuplot_i.hpp"


using namespace std;

float float_precision(float m){
    float dx = 1.0 / m;
    float x = 0.0;

    for (float i = 1.0; i <= m; i++){
        x += dx;
    }
    return abs(1.0 - x);
}

double double_precision(double m){
    double dx = 1.0 / m;
    double x = 0.0;

    for (double i = 1.0; i <= m; i++){
        x += dx;
    }
    return abs(1.0 - x);
}


int main(){
    string tryb;
    cout << "Wybierz tryb wpisujac 'float' lub 'double': ";
    cin >> tryb;
    Gnuplot g1 ("lines");
    ofstream plik ("dat.data");
    if (!strcmp(tryb.c_str(), "double")){
        double m = 2048;
        for (double i = 1.0; i <= m; i++ ){
            plik << i << " " << double_precision(i) << endl;
        }
        g1.cmd("plot 'dat.data' using 1:2 title 'Double Precision'");
        cin.get();
        wait_for_key();
    }
    else if (!strcmp(tryb.c_str(), "float")){
        float m = 2048;
        for (float i = 1.0; i <= m; i++ ){
            plik << i << " " << float_precision(i) << endl;
        }
        g1.cmd("plot 'dat.data' using 1:2 title 'Float Precision'");
        cin.get();
        wait_for_key();
    }

    return 0;
}