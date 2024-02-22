#include <iostream>

using namespace std;

int main() {
  int a, b, c = 0;

  cout << "Nombre 1 : ";
  cin >> a;
  cout << "Nombre 2 : ";
  cin >> b;

  int start = (a < b) ? a : b;
  int end = (a < b) ? b : a;
  
  for (int i = start; i <= end; i++) {
    c += i;
  }

  cout << c;
  
  return 0;
}