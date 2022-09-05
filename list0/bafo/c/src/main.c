/* BAFO - Bafo
   Um jogo de bafo consiste em virar cartas com a palma da mão, ganha quem virar
   mais cartas. No nosso caso, o jogo de bafo será constituido de três partidas
   sendo que cada partida possui N rodadas.

   Entrada
       A entrada é composta por:
       * uma linha determinando quantas rodadas têm aquela partida.
       * N linhas contendo dois números, Ex: 1 2. Que significam quantas
         figurinhas foram viradas pelos jogadores.
       Ex: 3
           1 2
           5 0
           3 3

   Saída
       A saída deve conter o ID de cada jogador e quantos pontos cada um fez,
       assinalando, também, quem foi o ganhador

   Restrições
       1 ≤ N ≤ 1000
*/

#include "../lib/lib.h"
#include <stdio.h>

int main(int argc, char **argv) {
  Player player_one;
  Player player_two;

  printf("Player One name: ");
  scanf("%s", player_one.name);
  getchar();
  player_one.score = 0;

  printf("Player two name: ");
  scanf("%s", player_two.name);
  getchar();
  player_two.score = 0;

  for (int i = 0; i < GAMES; i++) {
    int number_of_rounds;
    printf("Please, inform the number of rounds: ");
    scanf("%d", &number_of_rounds);

    int temp = 0;
    for (int i = 0; i < number_of_rounds; i++) {
      scanf("%d", &temp);
      player_one.score += temp;
      scanf("%d", &temp);
      player_two.score += temp;
    }

    printf("Jogo %d\n", i + 1);

    if (player_one.score > player_two.score) {
      printf("Player %s, won\n", player_one.name);
    } else if (player_one.score == player_two.score) {
      printf("Draw!\n");
    } else {
      printf("Player %s, won\n", player_two.name);
    }
  }

  return 0;
}
