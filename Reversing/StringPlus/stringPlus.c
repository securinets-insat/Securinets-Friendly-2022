#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>  


void encrypt(char* flag, char* ans) {
    for(int i = 0; i < strlen(flag); i++) {
        char car = (char)(((int)(flag[i]) ^ 0x22) % 256);
        ans[i] = car;
    }
}

int main(int argc, char* argv[]) {

    printf("Hello again, welcome in the 4th challenge in the CTF ! \n"); 
    printf("Give me the right Username and Flag ! \n"); 
    char username[20], flag[50];
    printf("Username : ");  
    scanf("%s", username); 
    if (strcmp("Ironbyte-N0s", username) == 0) {
        printf("Good Job Username is right ! \n"); 
        printf("Flag :"); 
        scanf("%s", flag);
        char ans[50]; 
        encrypt(flag, ans); 
        if (strcmp("qgawpklgvqYlMQ}kQ}MWP}iKLE_", ans) == 0) 
            printf("Congratulations, you can validate with that flag !"); 
        else 
            printf("Oops, you gave me the wrong flag, try again?");
    } else {
        printf("Oops username is wrong, try again ! ");
    }
    return 0;
}