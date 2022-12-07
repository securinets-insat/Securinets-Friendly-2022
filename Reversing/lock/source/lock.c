#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <string.h>

void win() {
	puts("     .--------.\n" \
	     "    / .------. \\\n" \
	     "   / /        \\ \\\n" \
	     "   | |        | |\n" \
	     "   | |        | |\n" \
	     "  ____________| |_\n" \
	     ".'  _         | | '.\n" \
	     "|  /_\\        |_|  |\n" \
	     "'._____ ____ _____.'\n" \
	     "|     .'____'.     |\n" \
	     "'.__.'.' UN '.'.__.'\n" \
	     "'.__  |LOCKED|  __.'\n" \
	     "|   '.'.____.'.'   |\n" \
	     "'.____'.____.'____.'\n" \
	     "'.________________.'\n" \
	);
	
	FILE *fp = fopen("./flag.txt", "r");
	if (fp == NULL) {
		puts("[!] If this happened while on the server please contact an admin.");
		exit(1);
	}
	printf("flag: ");

	while (!feof(fp)) {
		printf("%c", fgetc(fp));
	}

	fclose(fp);
}

void setup() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
	int unsigned t = ((time(NULL) >> 4) << 4) + rand();
	srand(t);
}

int main() {
	setup();

	char username[0x10];
	unsigned int password = 0, sum = rand();
	memset(username, 0, 0x10);

	puts("     .--------.\n" \
	     "    / .------. \\\n" \
	     "   / /        \\ \\\n" \
	     "   | |        | |\n" \
	     "  _| |________| |_\n" \
	     ".' |_|        |_| '.\n" \
	     "'._____ ____ _____.'\n" \
	     "|     .'____'.     |\n" \
	     "'.__.'.'    '.'.__.'\n" \
	     "'.__  |LOCKED|  __.'\n" \
	     "|   '.'.____.'.'   |\n" \
	     "'.____'.____.'____.'\n" \
	     "'.________________.'\n" \
	);
	printf("User: ");
	int len = read(0, username, 0x10);
	*(username + (len - 1)) = '\0';

	for (int i = 0; i < strlen(username); i++) {
		sum += username[i];
	}

	printf("Pass: ");
	scanf("%d", &password);

	if (password == sum)
		win();
	else
		puts("[!] STILL LOCKED.");

	return 0;
}
