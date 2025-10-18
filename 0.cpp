#include <iostream>

int main(){
    for (unsigned int n = 1; n < 1000000000; n *= 10){
        auto mask = 1u << 31;
        std::cout << n << ' ';
        for(;mask > 0;mask = mask >> 1){
            std::cout << ((n & mask) != 0);
        }
        std::cout << std::endl;
    }

    return 0;
}
