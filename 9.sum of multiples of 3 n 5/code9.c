// coded by Prince!
// sum of multiples of 3 and 5 of
// natural numbers less than 100

#include <stdio.h>

int main(){

	int sum = 0;
	for(int i=1; i<1000; i++)
		if(i%3 == 0 || i%5 == 0)
			sum += i;
	printf("The sum is %d\n", sum);
	return 0;

}