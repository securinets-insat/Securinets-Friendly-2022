// gcc main.c -o main -z relro -z now -no-pie

#include<stdio.h>
#include<stdlib.h>

int main(){

	char input[56];
	int target = 0xfa7e;

	puts("Show me how to overflow!");
	gets(input);
    printf("Your target is: %x\n", target);

    if(target != 0xfa7e){
        system("/bin/sh");
	}
	return 0;
}
