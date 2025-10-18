#include <iostream>

union FloatUnsigned {
    unsigned Unsigned;
    float Float;
}flu;

int main(){
    std::cin >> flu.Float;
    unsigned int n = flu.Unsigned;
    auto mask = 1u << 31;
    for(;mask > 0;mask = mask >> 1){
        std::cout << ((n & mask) != 0);
        if (mask == (1u << 31) || mask == (1u << 23)) {
            std::cout << " ";
        }
    }
    std::cout << std::endl;


    // Расшифровка согласно IEEE 754
    unsigned int sign = (n >> 31) & 1;
    unsigned int exponent = (n >> 23) & 0xFF;
    unsigned int mantissa = n & 0x7FFFFF;
    std::cout << sign << ' ';
    mask = 1u << 7;
    for (;mask > 0;mask = mask >> 1){
        std::cout << ((exponent & mask) != 0);
    }
    std::cout << ' ';
    mask = 1u << 22;
    for (;mask > 0;mask = mask >> 1){
        std::cout << ((mantissa & mask) != 0);
    }

}
