#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void win(){

	system("/bin/sh");

}


int main(){

	char buffer[100];
	puts("Can you win?");
	puts("Give me something");
	gets(buffer);
	return 0;

}
