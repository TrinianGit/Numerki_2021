#include <iostream>
#include <cmath>
#include <fstream>
#include "gnuplot_i.hpp"

using namespace std;

float pow_rep_float(float x){
    float result = pow(x, 5);
    result = result - (137.0/60.0) * pow(x, 4);
    result = result + (15.0/8.0) * pow(x, 3);
    result = result - (17.0/24.0) * pow(x, 2);
    result = result + (9.0/8.0) * x;
    result = result - (1.0/120.0);
    return result;
}

float multi_rep_float(float x){
    float result = x - (137.0/60.0);
    float result2 = x * result + (15.0/8.0);
    float result3 = x * result2 - (17.0/24.0);
    float result4 = x * result3 + (9.0/8.0);
    float result5 = x * result4 - (1.0/120.0);
    return result5;
}

double pow_rep_double(double x){   
    double result = pow(x, 5);
    result = result - (137.0/60.0) * pow(x, 4);
    result = result + (15.0/8.0) * pow(x, 3);
    result = result - (17.0/24.0) * pow(x, 2);
    result = result + (9.0/8.0) * x;
    result = result - (1.0/120.0);
    return result;
}

double multi_rep_double(double x){
    double result = x - (137.0/60.0);
    __sync_synchronize();
    double result2 = x * result + (15.0/8.0);
    __sync_synchronize();
    double result3 = x * result2 - (17.0/24.0);
    __sync_synchronize();
    double result4 = x * result3 + (9.0/8.0);
    __sync_synchronize();
    double result5 = x * result4 - (1.0/120.0);
    __sync_synchronize();
    return result5;
}

int main(){

    Gnuplot g1 ("");
    Gnuplot g2 ("");

    double f0 = 2.0/3.0;
    double g0 = 2.0/3.0;

    float F0 = 2.0/3.0;
    float G0 = 2.0/3.0;

    ofstream plik ("dat.data");

    for (int i = 0; i < 1000; i++){
        plik << i << " " << f0 - g0 << endl;
        f0 = pow_rep_double(f0);
        g0 = multi_rep_double(g0);
    }
    g1.cmd("plot 'dat.data' using 1:2 title 'Double Precision'");

    sleep(2);

    ofstream plik2 ("dat.data");
    
    for (int i = 0; i < 1000; i++){
        plik2 << i << " " << F0 - G0 << endl;
        F0 = pow_rep_float(F0);
        G0 = multi_rep_float(G0);
    }

    g2.cmd("plot 'dat.data' using 1:2 title 'Float Precision'");

    wait_for_key();
}