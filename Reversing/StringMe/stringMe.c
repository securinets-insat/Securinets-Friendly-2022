#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>  

int main(int argc, char* argv[]) {
    
    printf("Hello again, welcome in the third challenge in the CTF ! \n"); 
    printf("Again would you give me the flag ?\n"); 
    printf("Flag : "); 
    char flag[100]; 
    scanf("%s", flag);
    if (strcmp(flag, "SECURINETS{NICEEEEEE_STR1NG_1S_TH7_BEST7}") == 0)
        printf("Congratulations, you can validate with that flag !"); 
    else 
        printf("Oops, you gave me the wrong flag, try again?");

    return 0;
}