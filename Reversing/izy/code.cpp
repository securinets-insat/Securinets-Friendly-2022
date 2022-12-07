#include <iostream>
using namespace std;
  
string encrypt(string text, int s)
{
    string result = "";
  
    for (int i=0;i<text.length();i++)
    {
        if (isupper(text[i])){
            result += char(int(text[i]+s-65)%26 +65);
        }
    else{
        result += char(int(text[i]+s-97)%26 +97);
    }
  
    }
    return result;
}
  
void reverseStr(string& str)
{
    int len = str.length();
    int n = len-1;
    int i = 0;
    while(i<=n){
        //Using the swap method to switch values at each index
        swap(str[i],str[n]);
        n = n-1;
        i = i+1;
  }

}
// Driver program to test the above function
int main()
{
    int s = 16;
    string text;
    cout << "Password : ";
    cin >> text;
    string check = encrypt(text,s);
    reverseStr(check);
    string flag = "sdyqwqoucoujqjehomyyymqIJUDYHKSUI";
    if ( check == flag){
    cout << "great job !"<< endl;

    }else{
    cout << "No Worries , Try again" << endl;
    }
    return 0;
}
