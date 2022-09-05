make: src/main.c
	make clean
	mkdir build/obj build/bin -p
	gcc -c src/main.c -o build/obj/main.o
	gcc -o build/bin/main build/obj/main.o

clean:
	rm -rf build/obj/
	rm -rf build/bin/

run:
	./build/bin/main
