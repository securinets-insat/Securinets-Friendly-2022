// gcc main.c -o main -z relro -z now -fstack-protector

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void login(){
    char flag[50];
    FILE* f = fopen("./flag.txt", "r");
    if(f == NULL){
        printf("If you see this, please contact an admin.\n");
        exit(0);
    }
    fgets(flag, 50, f);
    printf("%s\n", flag);
    close(f);
}

int main(){
    char username[25];
    char password[25];

    printf("Username: ");
    gets(username);

    if(strcmp(username, password) == 0){
        login();
    }
    exit(0);
}