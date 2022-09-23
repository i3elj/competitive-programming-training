def main():
	isprime = lambda n : [x for x in range(1,n+1) if n % x == 0] == [1,n]
	num = int(input())
	print(isprime(num))


if __name__ == "__main__":
	main()
