
int get_sum(int a, int b) {
  int c = 0;
  int start = (a < b) ? a : b;
  int end = (a < b) ? b : a;
  
  for (int i = start; i <= end; i++) {
    c += i;
  }
  
  return c;
}