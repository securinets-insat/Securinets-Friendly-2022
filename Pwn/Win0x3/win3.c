// gcc win1.c -o win11

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void win(){
	system("/bin/sh");
}

void setup(){
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main(){
	setup();

	char buffer[80];
	printf("A simple ret2win challenge. %p",&win);
	puts("\nInput: ");
	gets(buffer);
	return 0;
}
