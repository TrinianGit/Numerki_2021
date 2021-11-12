CFLAGS = -ggdb
DEFINES = -DDEBUGGA
INCLUDES = 
LIBS = -lstdc++
SINUS = Sinus.o
WYKRESY = Wykresy.o
CC=g++

.cpp.o:
	$(CC) -c $(CFLAGS) $(DEFINES) $(INCLUDES) $<

all::	Sinus Wykresy

gnuplot_i.o:	gnuplot_i.hpp
Sinus.o:	Sinus.cpp

Sinus.x: $(SINUS)
	$(CC) -o $@ $(CFLAGS) $(SINUS) $(LIBS)
Wykresy.x: $(WYKRESY)
	$(CC) -o $@ $(CFLAGS) $(WYKRESY) $(LIBS)

clean: 
	rm -f *.[o] "Sinus" "Wykresy"
