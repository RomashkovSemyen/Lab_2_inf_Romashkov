#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

int main(){
    std::ofstream f_float("4_float.csv", std::ios::out);
    std::ofstream f_double("4_double.csv", std::ios::out);
    for (auto n = 1; n < 100000; n++){
        float h1 = M_PI / n;
        float intergal1 = 0;
        for (float x = 0.0; x <= M_PI; x += h1){
            intergal1 += h1 * std::sin(x);
        }
        f_float << std::fixed;
        f_float << std::setprecision(12);
        f_float << n << ' ' << intergal1 << std::endl;

        double h2 = M_PI / n;
        double intergal2 = 0;
        for (double x = 0.0; x <= M_PI; x += h2){
            intergal2 += h2 * std::sin(x);
        }
        f_double << std::fixed;
        f_double << std::setprecision(12);
        f_double << n << ' ' << intergal2 << std::endl;
    }













    return 0;

}
