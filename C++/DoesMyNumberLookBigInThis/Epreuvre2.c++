#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool narcissistic(int value) {
    int originalValue = value;
    int digits = log10(value) + 1;
    int sum = 0;

    while (value > 0) {
        int digit = value % 10;
        sum += pow(digit, digits);
        value /= 10;
    }

    return sum == originalValue;
}

int main() {
    int num = 153;

    if (narcissistic(num)){
        cout << "Nombre " << num << " => est narcissistic";
    }
    
    else {
        cout << "Nombre " << num << " => n'est pas narcissistic";
    }

    return 0;
}