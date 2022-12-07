#include<stdio.h>
#include<stdlib.h>

void setup(){
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main(){
	setup();
	char buffer[80];
	puts("What can you do now?\n");
	gets(buffer);
	return 0;

}
