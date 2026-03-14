.PHONY: test clean

main: tests.c main.o
	gcc -o main tests.c main.o

main.o: main.c main.h
	gcc -c main.c

test: main
	./main
	
clean:
	rm -f main
