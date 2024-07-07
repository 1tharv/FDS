#include <iostream>
using namespace std;

int main()
{
    int num,i=2;
    cin>>num;
    
    if(num<2)
    {
        cout<<"Not Prime";
    }
    
    else
    {
        while(i <= num)
        {
            if(i==num)
            {
            cout<<"Prime number";
            break;
            }
            else if(num %i == 0)
            {
                cout<<"Not Prime number";
                break;
            }
            
            i=i+1;
            
        }
        
    }
}
