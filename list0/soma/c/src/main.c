#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int size, result = 0;
  printf("Input: ");
  scanf("%d", &size);

  int *array = calloc(size, sizeof(int));

  for (int i = 0; i < size; i++) {
    scanf("%d", array + i);
  }
  for (int i = 0; i < size; i++) {
    result += *(array + i);
  }

  printf("Output: %d\n", result);
  free(array);
  return 0;
}
