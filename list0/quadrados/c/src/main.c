/*
 * QUADRAD2 - Quadrados (Squares)
 *    Given an integer N, determine how much is N square.
 *
 *  Inputs:
 *    - The input is made by only one test case with just one line which contains the integer N.
 *  Outputs:
 *    - This program must produce just only one line containing the value of N square
 *  Restrictions:
 *    - |N| <= 10.000
 *
 * Obs: use make to run this program
*/

#include <stdio.h>
#include "../lib/func.h"

int main(int argc, char** argv) {
  int num;
  printf("input: ");
  scanf("%d", &num);
  printf("%d\n", to_the_power(num));
  return 0;
}
