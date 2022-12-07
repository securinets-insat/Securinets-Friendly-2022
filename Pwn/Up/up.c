#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<math.h>

int main(){

	int input;
	unsigned short password;

	puts("What do you need?");
	scanf("%d",&input);

	if(input < 0) password = abs(input);
        else password = input;
	password += 1;

	if(!password) system("/bin/sh");
        else exit(0);

}
