#include <iostream>

using namespace std;

int get_sum(int a, int b) {
  int c = 0;

  int start = (a < b) ? a : b;
  int end = (a < b) ? b : a;
  
  for (int i = start; i <= end; i++) {
    c += i;
  }

  cout << "sum : " << a << " to " << b << " = " << c;
  
  return c;
}

int main() {
  
  get_sum(56, 68);
  
  return 0;
}