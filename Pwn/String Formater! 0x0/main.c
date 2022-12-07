// gcc main.c -o main -z relro -z now -fstack-protector -no-pie
#include <stdio.h>
#include <stdlib.h>

void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

int main(){
    setup();
    
    char flag[50];
    FILE* f = fopen("./flag.txt", "r");
    if(f == NULL){
        printf("If you see this, please contact an admin.\n");
        exit(0);
    }
    fgets(flag, 50, f);
    fclose(f);

    char msg[50];
    fgets(msg, 50, stdin);
    printf(msg);
}