// gcc win0.c -o win0 -no-pie -m32

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void win(int a){
	if (a == 0xcafebabe){
		system("/bin/sh");
	}
}

void vuln(){
    char buffer[80];
	puts("First of all, use the 'file' command to get info about the binary, check the architecture of the executable, its important");
	puts("Input:");
	gets(buffer);
}

void setup(){
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main(){
	setup();

	vuln();
	return 0;
}
