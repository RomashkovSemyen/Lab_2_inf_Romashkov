#include <iostream>

int main(){
    std::cout << std::fixed;
    std::cout.precision(2);
    for (float i = 16776000.0; i < 10000000000000000000000.0; i += 1.0){
        std::cout << i << std::endl;
    }
}
//на 16777216.00 зацикливание
