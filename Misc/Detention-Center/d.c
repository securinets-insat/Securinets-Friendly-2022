#include<stdio.h>

int main(){
	int d;
	while((d=getchar())!=27) {
		printf("%c", d);
	}
	printf("Securinets{Dis_Defenseless_Detention}");
	return(0);
}
