#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

char key[10] = "monji";
void encrypt(char* flag, int ans[100]) {
    for(int i = 0; i < strlen(flag); i++) 
        ans[i] = ((int)(flag[i]) ^ (int)(key[i % strlen(key)])) % 256;  
}

int main(int argc, char* argv[]) {

    int ans[100];
    char flag[100]; 
    printf("Hello again, welcome in the final challenge in the CTF ! \n"); 
    printf("Again would you give me the flag ?\n");
    printf("Flag : ");
    scanf("%s", flag);
    encrypt(flag, ans);
    int bytes[100] = {62,42,45,63,59,36,33,43,62,58,22,32,27,24,54,58,0,28,1,26,5,0,30,25,54,58,6,2,6,54,15,10,49,43,4,12,21,7,4,14,16}; 
    int ok = 0; 
    for (int i = 0; i < strlen(flag) && !ok; i++) {
        if ((int)(flag[i]) != (bytes[i] ^ (int)(key[i % strlen(key)])) )
            ok = 1;
    }
    if (!ok)
        printf("Congratulations, you can validate with that flag !"); 
    else 
        printf("Oops, you gave me the wrong flag, try again?");

    return 0;
}