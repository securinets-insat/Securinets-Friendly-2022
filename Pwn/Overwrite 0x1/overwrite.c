#include<stdio.h>
#include<stdlib.h>

int main(){

	char input[56];
	int target;

	puts("Do you have something to say?");
	read(0,input,64);
        if(target == 0xdeadbeef){
		system("/bin/sh");
	}
	return 0;
}
