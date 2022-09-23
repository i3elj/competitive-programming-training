""" PAR - Par ou ímpar
		Muitas crianças gostam de decidir todas as disputas através do famoso jogo de
		Par ou Ímpar. Nesse jogo, um dos participantes escolhe Par e o outro Ímpar.
		Após a escolha, os dois jogadores mostram, simultaneamente, uma certa quantidade
		de dedos de uma das mãos. Se a soma dos dedos das mãos dos dois jogadores for
		par, vence o jogador que escolheu Par inicialmente, caso contrário vence o que
		escolheu Ímpar.

	Tarefa
		Dada uma seqüência de informações sobre partidas de Par ou Ímpar (nomes dos 		
		jogadores e números que os jogadores escolheram), você deve escrever um programa
		para indicar o vencedor de cada uma das partidas.

	Entrada
		A entrada é composta de vários conjuntos de testes. A primeira linha de um 		
      conjunto de testes contém um inteiro N, que indica o número de partidas de Par 		
      ou Ímpar que aconteceram. As duas linhas seguintes contêm cada uma um nome de 		
      jogador. Um nome de jogador é uma cadeia de no mínimo um e no máximo dez letras 		
      (maiúsculas e minúsculas), sem espaços em branco. As N linhas seguintes contêm 		
      cada uma dois inteiros A e B que representam o número de dedos que cada jogador 		
      mostrou em cada partida (0 <= A <= 5 e 0 <= B <= 5). Em todas as partidas, o 		
      primeiro jogador sempre escolhe Par. O final da entrada é indicado por N = 0.

		Exemplo de entrada:
			3
			Pedro
			Paulo
			2 4
			3 5
			1 0
			2
			Claudio
			Carlos
			1 5
			2 3
			0
	Saída
		Para cada conjunto de teste da entrada, seu programa deve produzir a saída da 		
      seguinte forma. A primeira linha deve conter um identificador do conjunto de 		
		teste, no formato "Teste n", onde n é numerado seqüencialmente a partir de 1. 		
		As próximas N linhas devem indicar o nome do vencedor de cada partida. A próxima
		linha deve ser deixada em branco. A grafia mostrada no Exemplo de 3 Saída, 		
		abaixo, deve ser seguida rigorosamente.

	Exemplo de Saída
		Teste 1
		Pedro
		Pedro
		Paulo

		Teste 2
		Claudio
		Carlos
"""

def rodada():
    name = str(input("Name1: "))
    name2 = str(input("Name2: "))

    num = int(input("Num1: "))
    num2 = int(input("Num2: "))
    res = num + num2

    if res % 2 == 0 :
        return name
    else:
        return name2

def main():
    teste1 = []
    matches = int(input("Matches: "))
    for i in range(matches):
        teste1.append(rodada())

    print("\nTeste 1:")
    for vencedores in teste1:
        print(vencedores)

if __name__=="__main__":
    main()
