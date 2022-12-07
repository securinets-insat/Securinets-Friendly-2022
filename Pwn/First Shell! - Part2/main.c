// gcc main.c -o main -z relro -z now -fstack-protector

#include <stdio.h>
#include <stdlib.h>

int main(){
    system("/bin/sh");
}