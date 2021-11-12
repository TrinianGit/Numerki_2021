// Example for C++ Interface to Gnuplot

// requirements:
// * gnuplot has to be installed (http://www.gnuplot.info/download.html)
// * for Windows: set Path-Variable for Gnuplot path (e.g. C:/program files/gnuplot/bin)
//             or set Gnuplot path with: Gnuplot::set_GNUPlotPath(const std::string &path);


#include <iostream>
#include <cmath>
#include "gnuplot_i.hpp" //Gnuplot class handles POSIX-Pipe-communikation with Gnuplot

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__TOS_WIN__)
 #include <conio.h>   //for getch(), needed in wait_for_key()
 #include <windows.h> //for Sleep()
 void sleep(int i) { Sleep(i*1000); }
#endif


#define SLEEP_LGTH 2  // sleep time in seconds
#define NPOINTS    50 // length of array

void wait_for_key(); // Programm halts until keypress

using namespace std;

int main(int argc, char* argv[])
{
        Gnuplot g1 ("lines");

        g1.set_title("Wykresy");
        g1.cmd("set multiplot");
        g1.set_xrange(57, 129);
        g1.cmd("set size 1, 0.33");
        g1.cmd("set origin 0, 0.7");
        g1.cmd("plot 'btc.data' using 1:2 title 'BTC' with lines");
        g1.set_title("");
        g1.cmd("set size 0.99, 0.33");
        g1.cmd("set origin 0.01, 0.4");
        g1.cmd("plot 'eth.data' using 1:2 title 'ETH' with lines");
        g1.set_xlabel("Dni");
        g1.cmd("set size 0.98, 0.33");
        g1.cmd("set origin 0.02, 0.1");
        g1.cmd("plot sin(x) title 'sin(x)'");
        g1.cmd("unset multiplot");

        wait_for_key();


    return 0;
}



void wait_for_key ()
{
#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__TOS_WIN__)  // every keypress registered, also arrow keys
    cout << endl << "Press any key to continue..." << endl;

    FlushConsoleInputBuffer(GetStdHandle(STD_INPUT_HANDLE));
    _getch();
#elif defined(unix) || defined(__unix) || defined(__unix__) || defined(__APPLE__)
    cout << endl << "Press ENTER to continue..." << endl;

    std::cin.clear();
    std::cin.ignore(std::cin.rdbuf()->in_avail());
    std::cin.get();
#endif
    return;
}
