// coded by Prince!
// a program to convert string into uppercase without
// using built-in funcitons/libraries

#include <stdio.h>

int main(){

	char string[50];
	int i=0;
	printf("Enter a string: ");
	gets(string);

	while(string[i] != '\0'){
		if(string[i] >= 97 && string[i] <= 122)
			string[i] -= 32;
		i++;
	}
	printf("String in uppercase: %s\n", string); // string in uppercase
	return 0;

}