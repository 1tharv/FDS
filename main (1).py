def verify(string):
    n=len(string)
    x=0
    y=n-1
    for i in range(n-1):
        if(string[x] != string[y]):
            print("Given String is not a Palindrome")
            return False
        y=y-1
        x=x+1
    return True
    
def main():
    string=(input("Enter a String: "))
    ans=verify(string)
    if(ans==True):
        print("Given String is Palindrome")

main()