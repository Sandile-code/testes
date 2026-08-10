#include <stdio.h>
int main()
{
    ;
    int quantidade, loop, Num, NumAnterior;
    
    printf("Digite a quantidade de números que você deseja digitar ");
    scanf("%d", &quantidade);

    if (quantidade <= 0 ){
        printf("Quantidade inválida");
        return 0;
    }
    printf("Digite o primeiro número: ");
    scanf("%d", &Num);
    
    Num = NumAnterior;
    
    for(loop = 2;  loop <= quantidade; loop++){
        printf("Digite o %d número: ", loop);
        scanf("%d", &NumAnterior);
        
        if(NumAnterior>Num){
            Num = NumAnterior;
        }
    }
    printf("O maior número digitado foi %d", NumAnterior);
    return 0;
    
}