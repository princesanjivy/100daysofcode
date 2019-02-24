//coded by Prince!
//program to find the length of a string/array
//without built-in functions or libray 

#include <stdio.h>

int main()
{
	char String[] = "100 days of code";
	int len = 0;

	while(String[len] != '\0')
		len++;

	printf("The length of the string is:%d\n", len );
	return 0;
}
//==>swipe for output