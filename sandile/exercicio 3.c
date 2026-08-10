#include <stdio.h>
int main ()
{
    float NumAtual, soma, NumAnterior = 0;
    int contador = 0;
 
    printf("Digite uma sequência de números crescentes: ");
    scanf("%f", &NumAtual);

    soma = NumAtual;
    contador = 1;
    NumAnterior = NumAtual;
    
    while (1){
       printf("Digite o proximo número: ");
       scanf("%f", &NumAtual);
       
       if (NumAnterior > NumAtual){
           break;
       }
       soma += NumAtual;
       contador++;
       NumAnterior=NumAtual;
    }
    printf("Soma: %.0f\n", soma);
    printf("Quantidade de numeros: %d\n", contador);
    
    if (contador > 0) {
        printf("Media aritmetica: %.2f\n", soma / contador);
    }
    return 0;
}