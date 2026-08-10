#include <stdio.h>
int main ()
{
    printf("tabela de conversão de polegadas para centímetros\n");
    printf("Polegadas        |  Centímetros          \n");
    for (int pol = 1; pol <= 20; pol++){
        float cm = pol * 2.54;

        printf("  %-15d|    %.2f cm\n", pol, cm);
    }
    return 0;
}