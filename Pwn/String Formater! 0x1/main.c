//gcc main.c -o main -z relro -z now -fstack-protector -no-pie
#include <stdio.h>
#include <stdlib.h>

void secretFlag(){
    char *flag;
    flag = getenv("FLAG");
}

void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int main(){
    setup();
    
    char msg[50];
    fgets(msg, 50, stdin);
    printf(msg);
}