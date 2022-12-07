#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
	system("/bin/sh");
}

void setup() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

void menu() {
	puts("1. Add some #TODO notes.");
	puts("2. Look at #TODO notes.");
	puts("3. Quit.");
	printf("> ");
}

int main() {
	setup();

	char buffer[10][0x20];
	int choice, index; 

	while (1) {
		menu();
		scanf("%d", &choice);
		getchar();
		
		switch (choice) {
			case 1:
				printf("Index: ");
				scanf("%d", &index);
				getchar();
				printf("TODO: ");
				read(0, buffer[index], (0x20 * 11) - (index * 0x20));
				break;
			case 2:
				printf("Index: ");
				scanf("%d", &index);
				getchar();
				printf("[%d] %s\n", index, buffer[index]);
				break;
			case 3:
				return 0;
			default:
				puts("Invalid Choice!");
		}
	}

}
