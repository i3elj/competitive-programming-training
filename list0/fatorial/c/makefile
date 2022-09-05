make: src/main.c lib/func.c
	make clean
	mkdir build/obj build/bin -p
	gcc -c src/main.c -o build/obj/main.o
	gcc -c lib/func.c -o build/obj/func.o
	gcc -o build/bin/main build/obj/func.o build/obj/main.o

clean:
	rm -rf build/obj/
	rm -rf build/bin/

run:
	./build/bin/main
