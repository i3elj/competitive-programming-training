#include <stdio.h>
#include "../lib/lib.h"

int main() {
  int input = 0;
  scanf("%d", &input);
  printf("the factorial of %d is: %d\n", input, factorial(input));
  return 0;
}
