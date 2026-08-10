#include <stdio.h>
int main()
{
    int num, numfinal, fatorial;
    
    printf("Digite um número para ser feito o fatorial\n");
    scanf("%d", &num);
    
    numfinal = num;
    fatorial = 1;
    
    if(num < 0){
        printf("Não existe fatorial de número negativo");
        return 0;
    }
    else while ( num > 0 ){
        fatorial *= num;
        num--;
    }
    
    printf("O fatorial de %d é %d", numfinal, fatorial);
    return 0;

}