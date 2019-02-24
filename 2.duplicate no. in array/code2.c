//coded by Prince!
//program to find the duplicate number in the array[int]
#include <stdio.h>

int main()
{
	int array[] = {2,2,5,2,5,0},dup; //example
	for(int i=0; i<6; i++) //array size is 6
		for(int j=i+1; j<6; j++)
			if(array[i] == array[j] && dup != array[i]){
				dup = array[i];
				printf("The duplicate number is %d\n", array[i]); //to print only the duplicate number
				break;
			}

	return 0;
}