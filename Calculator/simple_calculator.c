#include <stdio.h>  

int main(){

    float x, y, z;
    char operator;

    printf("Enter the first number:");
    scanf(" %f", &x);

    printf("Enter the desired operator:");
    scanf(" %c", &operator);

    printf("Enter the second number:");
    scanf(" %f", &y);

    if (operator == '+')
    z = x + y,
    printf("%.2f %c %.2f eqauls %.2f", x, operator, y, z);

    else if (operator == '-')
    z = x - y,
    printf("%.2f %c %.2f eqauls %.2f", x, operator, y, z);
    
    else if (operator == '*')
    z = x * y,
    printf("%.2f %c %.2f eqauls %vf", x, operator, y, z);

    else if (operator == '/')
    z = x / y,
    printf("%.2f %c %.2f eqauls %.2f", x, operator, y, z);

    else
    printf("You have entered and invalid operator");

    return 0;
}
