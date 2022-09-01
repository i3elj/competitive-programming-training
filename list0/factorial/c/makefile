make: src/main.c lib/lib.c
	gcc -c src/main.c -o build/obj/main.o
	gcc -c lib/lib.c -o build/obj/lib.o
	gcc -o build/bin/main build/obj/lib.o build/obj/main.o

clean:
	rm -rf build/obj/*
	rm -rf build/bin/main
