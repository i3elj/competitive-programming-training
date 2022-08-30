#include <stdio.h>
#include "../lib/func.h"

int main(int argc, char** argv) {
  int num;
  printf("input: ");
  scanf("%d", &num);
  printf("%d\n", to_the_power(num));
  return 0;
}
