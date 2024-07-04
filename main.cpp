#include <iostream>
using namespace std;
int main()
{
    int a,fact=1;
    cout<<"Input: ";
    cin>>a;
    
    for(int i=1;i<=a;i++)
    {
        fact=fact*i;
    }
    
    cout<<fact;
    return 0;
}