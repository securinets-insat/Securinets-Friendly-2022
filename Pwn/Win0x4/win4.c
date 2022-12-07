#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void win(int a){
	if (a == 0xcafebabe){
		system("/bin/sh");
	}
}


int main(){
	char buffer[80];
	puts("Input:");
	gets(buffer);
	return 0;
}
