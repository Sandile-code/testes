#include <stdio.h>
int main()
{
	int anos;
	float taxa_a, taxa_b, pop_a, pop_b;

	pop_a = 90000000;
	pop_b = 200000000;
	taxa_a = 0.03;
	taxa_b = 0.015;
	anos = 0;

	while(pop_a <= pop_b) {
		pop_a = pop_a + (pop_a * taxa_a);
		pop_b = pop_b + (pop_b * taxa_b);
		anos+= 1;
	}
 printf("Será em %d anos que a cidade A se igualará ou superará B", anos);
 return 0;
}