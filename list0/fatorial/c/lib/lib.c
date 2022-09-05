int factorial(int n) {
  int result = 1;
  for (int i = n; i > 0; i--, n--) {
    result = result * n;
  }
  return result;
}
