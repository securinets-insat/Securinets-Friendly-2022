// gcc libc0.c -o lib0 -no-pie

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
	printf("Hello!");
	printf("\nShow me what you can do with this: %p\n", &printf);
	gets(buffer);
	return 0;

}
