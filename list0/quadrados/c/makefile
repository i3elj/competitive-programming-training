make: src/main.c lib/func.c
	gcc -c src/main.c -o build/obj/main.o
	gcc -c lib/func.c -o build/obj/func.o
	gcc -o build/bin/main build/obj/func.o build/obj/main.o
	@echo ""
	./build/bin/main
