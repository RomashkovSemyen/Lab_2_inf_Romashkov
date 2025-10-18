#include <iostream>

union FloatUnsigned {
    unsigned Unsigned;
    float Float;
}flu;

int main(){
    std::cout << std::fixed;
    std::cout.precision(2);
    for (flu.Float = 10.0; flu.Float < 1000000000000000000.0; flu.Float = flu.Float * 10.0){
        std::cout << flu.Float << ' ';
        unsigned int n = flu.Unsigned;
        unsigned int sign = (n >> 31) & 1;
        unsigned int exponent = (n >> 23) & 0xFF;
        unsigned int mantissa = n & 0x7FFFFF;
        std::cout << sign << ' ';
        auto mask = 1u << 7;
        for (;mask > 0;mask = mask >> 1){
            std::cout << ((exponent & mask) != 0);
        }
        std::cout << ' ';
        mask = 1u << 22;
        for (;mask > 0;mask = mask >> 1){
            std::cout << ((mantissa & mask) != 0);
        }
        std::cout << std::endl;
    }
}
