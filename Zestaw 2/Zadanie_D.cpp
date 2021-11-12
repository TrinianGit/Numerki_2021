#include <iostream>
#include <cstring>
#include <cmath>
#include <fstream>
#include <limits>
#include <cmath>
#include <float.h>
#include "gnuplot_i.hpp"

using namespace std;

ofstream plik ("dat.data");


void float_precision(float z){

    float het = 1.0;
    float c = 4.0 + 4 * z * FLT_EPSILON;
    float cprev = 4.0 + 4.0 * (z+1) * FLT_EPSILON;
    float a = 1.0;
    float b = 4.0;
    float delta = b*b - 4*a*c;
    float deltaprev = b*b - 4*a*cprev;

    float x = (-b + sqrt(delta))/(2*a);
    float prev = (-b + sqrt(deltaprev))/(2*a);

    plik << z << " " << abs(prev - x) << endl;

}


void double_precision(double z){
    
    double dx = 4.0 + DBL_EPSILON;
    double c = 4.0 + 4.0 * z * DBL_EPSILON;
    double cprev = 4.0 + 4.0 * (z+1) * DBL_EPSILON;
    double a = 1.0;
    double b = -4.0;
    double delta = b * b - 4.0 * a * c;
    double deltaprev = b * b - 4.0 * a * cprev;

    double x = (-b + sqrt(delta))/(2*a);
    double xprev = (-b + sqrt(deltaprev))/(2*a);

    plik << z << " " << abs(x - xprev) << endl;

    
}


int main(){
    
    
    Gnuplot g1 ("");
    Gnuplot g2 ("");

    for (int i = -248; i < 0; i++){
        double_precision ((double) i);
    }
    g1.cmd("plot 'dat.data' using 1:2 title 'Double Precision'");

    sleep(5);

    ofstream plik2 ("dat.data");
    
    for (int i = -248; i < 0; i++){
       float_precision ((float) i);
    }
    g2.cmd("plot 'dat.data' using 1:2 title 'Float Precision'");
    wait_for_key();
}