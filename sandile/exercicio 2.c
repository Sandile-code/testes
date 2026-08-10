#include <stdio.h>
int main ()
{
    printf("tabela de conversão de Fahrenheit para Celsius\n");
    printf("Fahrenheit      |  Celsius          \n");
    for (float fahr = 50; fahr <= 150; fahr++){
        float cel = (5.0 / 9.0) * (fahr - 32.0);

        printf("  %-12.0fºF|    %.2fºC\n", fahr, cel);
    }
    return 0;
}