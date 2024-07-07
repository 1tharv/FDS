#include<iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Input: ";
    cin>>n;
    
    string letters[10]={"one","two","three","four","five","six","seven","eight","nine","greater than nine"};
    
    if(n<=9)
    {
        cout<<letters[n-1];
    }
    
    else
    {
        cout<<letters[9];
    }
}