#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>


void encrypt(char* flag, char* ans) {
    for(int i = 0; i < strlen(flag); i++) {
        char car = (char)(((int)(flag[i]) ^ 0x23) % 256);
        ans[i] = car;
    }
}

int main(int argc, char* argv[]) {

    char ans[50];
    char flag[50]; 
    printf("Hello again, welcome in the second challenge in the CTF ! \n"); 
    printf("Again would you give me the flag ?\n");
    fgets(flag, 50, stdin);
    encrypt(flag, ans);
    if (strcmp("pf`vqjmfwpXdLLGG|iLA^)", ans) == 0)
        printf("Congratulations, you can validate with that flag !"); 
    else 
        printf("Oops, you gave me the wrong flag, try again?");

    return 0;
}