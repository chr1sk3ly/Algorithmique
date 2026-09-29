CC = gcc
CFLAGS = -Wall -Wextra -Iinclude

SRC = main.c $(wildcard src/*.c)
OBJ = $(SRC:%.c=obj/%.o)
EXEC = programme

$(EXEC): $(OBJ)
	$(CC) $^ -o $@

obj/%.o: %.c $(wildcard include/*.h)
	mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)

.PHONY: clean
