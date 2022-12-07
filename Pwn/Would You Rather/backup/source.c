#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wchar.h>

struct note {
	char author[0x20];
	char title[0x20];
	char content[0x400];
};

void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void menu() {
	puts("1. Write A Note");
	puts("2. Try To Guess The Flag");
	puts("3. Forfeit");
}

int read_int32() {
        int num;
        printf("> ");
        scanf("%d", &num);
        return num;
}

void writeAnote() {
	struct note myNote;
	printf("Author: ");
	read(0, myNote.author, 0x20);
	printf("Title: ");
	read(0, myNote.title, 0x20);
	printf("Content: ");
	read(0, myNote.content, 0x400);
	printf("Author: %s\n", myNote.author);
	printf("Title: %s\n", myNote.title);
	printf("Content: %s\n", myNote.content);
}

void tryToGuess() {
	char flag[0x100];
	char guess[0x100];
	FILE *fp = fopen("./flag.txt", "r");
	if (fp == NULL)
		exit(1);
	int size = fread(&flag, 2, 0x100, fp);
	*(strchr(flag, '\n')) = '\0';
	fclose(fp);
	printf("So what's your guess? ");
	read(0, guess, size - 1);
	if (!strncmp(flag, guess, size - 1))
		puts("Nice Guessing Skills!");
	else
		puts("Bad Guessing Skills :(");
}

int main() {
	int choice;
	setup();

	while (1) {
		menu();
		choice = read_int32();
		switch (choice) {
			case 1:
				writeAnote();
				break;
			case 2:
				tryToGuess();
				break;
			case 3:
				return 0;
			default:
				puts("Invalid Choice!");
		}
	}
}

