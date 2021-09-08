// To run it is Ctrl + Option + N
/*

#include <iostream>

// using namespace std;
using std::cout; // Replaces std:: prefix for cout only

 int main() 
{
    cout << "Hello World";
} 

*/

// A namespace is a method provided in C++ that allows us to 
// group or structure related entities inside one category.

// #include <header_file> or "header_file"

/*
#include <stdio.h>

int main( void )
{
    printf( "Howdy World!" );

    return 0;
}

*/


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

/*
int main()
{
int x; 
cout << "Type a number: "; // Type a number and press enter
cin >> x; // Get user input from the keyboard
cout << "Your number is: " << x; // Display the input value
}
*/

/*
ESCAPE SEQUENCES
\n is return and new line
\t is tab (8 spaces)
\" is double quote
\' is single quote
\\ is backslash
\0 is null character
*/

// <data type> indentifier1,indentifier2,indentifier3
// int age, iq, shoe_size;

// <data type> indentifier = <literal>
// <data type> indentifier = <constant>
// int sum = 0;
// int Dad_Age = Retirement_Age;
// int My_Age = 18;
// int num_dependents, staff salary = base_salary;
// 