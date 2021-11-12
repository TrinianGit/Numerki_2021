CC = g++ -w

.PHONY: all clean

all: Zadanie_A.x Zadanie_B.x Zadanie_C.x Zadanie_D.x Zadanie_E.x

%.x: %.cpp
	$(CC) -o $@ $<

clean:
	$(RM) *.x
	$(RM) *.data