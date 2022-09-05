/* FATORIA2 - Fatorial
   Dado um inteiro N, determine quanto vale N fatorial (escreve-se N!). O fatorial 
   de um número é o produto de todos os números entre 1 e N, inclusive. Por 
   exemplo, 5! = 5 × 4 × 3 × 2 × 1 = 120.

   Entrada
       A entrada é composta por uma única linha que contém o inteiro N.

   Saída
       A saída deve consistir de apenas uma linha contendo o valor de N!.

   Restrições
       0 ≤ N ≤ 12
*/

#include <stdio.h>
#include "../lib/lib.h"

int main() {
  int input = 0;
  scanf("%d", &input);
  printf("the factorial of %d is: %d\n", input, factorial(input));
  return 0;
}
