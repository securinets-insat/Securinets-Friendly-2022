 #include <stdio.h>

// Create an integer variable that will store the number we get from the user
//
//
int main(){
char s[29];

printf("Password \n");

scanf("%s", &s);
int sum=0;
for (int i=0; i<29;i++){
    sum=sum+(int)s[i];
}
if((sum==2657 )&&
(((int)s[26] + (int)s[24] +(int)s[15] + (int)s[13] + (int)s[4] + (int)s[2] + (int)s[0] + (int)s[28]) == 803)&&
(((int)s[11]^(int)s[12])==((int)s[11]^(int)s[18]))&&
(((int)s[11]^(int)s[12])==((int)s[11]^(int)s[24]))&&
(((int)s[14]+(int)s[15])==((int)s[16]+(int)s[17]))&& 
((int)s[13]==(int)'w')&&
(((int)s[22]*(int)s[21])==((int)s[22]*(int)s[22]))&&
(((int)s[14]-1)==(int)s[21])&&
((int)s[19]== 115)&&
(((int)s[19]+(int)s[23])==(2*(int)s[19]-3))&&
(((int)s[29-4]-(int)s[29-3])==((int)s[29-4]-(int)s[29-4]))&&
(((int)s[29-4]-(int)s[29-3])==((int)s[29-4]-(int)s[29-4]))&&
((int)s[29-3]==(int)s[29-2])&&
(((int)s[2]*(int)s[3])==5695)&&
(((int)s[2]^(int)s[3])==(((int)s[4]^(int)s[5])-5))&&
(((int)s[4]^(int)s[5]^(int)s[6]) == 85)&&
(((int)s[6]^(int)s[7]^(int)s[8])==95)&&
(((int)s[8]+(int)s[9]+(int)s[10])==((((int)s[10]^(int)s[11]^(int)s[12])+((int)s[12]^(int)s[13]^(int)s[14])+19)*2+42))&&
(((((int)s[17]^(int)s[18]^(int)s[19])+(int)s[1])+17)==((int)s[16]^(int)s[15]^(int)s[16]))&&
(((int)s[19]+(int)s[20])==223)&&
((int)s[0]==83)&&
((int)s[1]==69)&&
((int)s[2]==67)&&
((int)s[10]==123)&&
(((int)s[20]-8)==100)&&
((((int)s[28]+(int)s[0]-8))==((int)s[27]+(int)s[1]+9))&&
(((int)s[26]+(int)s[25]+(int)s[0]-27)==((int)s[25]+(int)s[24]+(int)s[0]))&&
(((int)s[23]+(int)s[24]-(int)s[22]-(int)s[21]-(int)s[20])==-3)&&
(((int)s[22]-(int)s[21]+(int)s[20]-(int)s[19])== -7)&&
(((int)s[4]+(int)s[5])==155)&&
(((int)s[5]+(int)s[6])==151)&&
(((int)s[6]+(int)s[7])==147)&&
(((int)s[11]+(int)s[12]+6)==((int)s[10]+(int)s[9]))&&
(((int)s[9]+(int)s[12]-7)== ((int)s[13]+(int)s[14]))){

printf("GOOD JOB !! \n");

}else{

printf("No Worries , Try Again \n");

}


}
