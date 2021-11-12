#include <iostream>
#include <limits>
#include <cstring>

using namespace std;

int main (){

    string tryb;
    float x;
    double y;

    cout << "Czy chcesz zobaczyc obsluge przekroczenia granicy float lub double? (jesli tak wpisz odpowiedni typ zmiennej): ";
    cin >> tryb;

    cout << "Przekroczenie float od gory: " << numeric_limits<float>::max() + numeric_limits<float>::max() << endl;
    cout << "Przekroczenie float od dolu: " << -numeric_limits<float>::max() - numeric_limits<float>::max() << endl;
    cout << endl;
    cout << "Przekroczenie double od gory: " << numeric_limits<double>::max() + numeric_limits<double>::max() << endl;
    cout << "Przekroczenie double od dolu: " << -numeric_limits<double>::max() - numeric_limits<double>::max() << endl;
    
    if (tryb == "float")  x = numeric_limits<float>::max() * 2;
    else if (tryb == "double") y = numeric_limits<double>::max() * 2;

    if (x > numeric_limits<float>::max()) {
        throw out_of_range("float x");
    }
    if (y > numeric_limits<double>::max()) {
        throw out_of_range("double y");
    }

    return 0;
}