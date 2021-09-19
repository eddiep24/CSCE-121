#include <iostream>
using namespace std;

int factorials(int x){
    if(x==1){
        return 1;
        }
    else
        {
        return x * factorials(x-1);
        }
}

int main()
{
    int y;
    cout << "What number do you want to find the factorial of?" << endl;
    cin >> y;
    cout << factorials(y) << endl;
}  
