// gcc main.c -o main -no-pie

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char input[50];

	puts("Can you send the special letters?");
	read(0,input,50);

    if(strcmp(input, "\x7f\xff\xef\xbe\xad\xde") == 0){
        system("/bin/sh");
	}
	return 0;
}
