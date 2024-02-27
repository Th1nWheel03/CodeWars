#include <iostream>

using namespace std;

int mobius(long long int n) {
  long long count = 1;
  auto isDivisible = [&] (auto x) {
    if (n % x == 0) {
      count++;
      n /= x;
    }
    return n % x == 0;
  };
  
  if (isDivisible(2)) return 0;  
  for (int i = 3; i * i <= n; i += 2) if (isDivisible(i)) return 0; 
  return count % 2 ? -1 : 1;
}

int main() {
    cout << mobius(10);
    return 0;
}