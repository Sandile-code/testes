#include <stdio.h>
int main()
{
    int voto;
    int cand_a = 0, cand_b = 0, cand_c = 0, cand_d = 0;
    int vot_nul = 0, branco=0;
    
    printf("-----------------------------------Eleição presidencial----------------------\n");
    printf("LULA | 1 | BOLSONARO | 2 |  ENEIAS | 3 | JANGO | 4 |\n");
    printf("VOTO NULO | 5 | VOTO EM BRANCO | 6 |\n");
    printf("------------------------------------------------------------------------------\n");
    

    do{
        printf("Digite o número do presidente que você deseja votar ");
        scanf("%d", &voto);
        
        
        switch(voto){
            case 1:
                cand_a++;
                break;
            case 2:
                cand_b++;
                break;
            case 3:
                cand_c++;
                break;
            case 4:
                cand_d++;
                break;
            case 5:
                vot_nul++;
                break;
            case 6:
                branco++;
                break;
            default:
                printf("Número inválido, digite de 1 a 6.\n");
        }
    }
    
    while( voto != 0);
    printf("-------------------Resultado Final---------------\n");
    printf("_________________________________________________\n");
    printf("LULA recebeu %d votos, BOLSONARO recebeu %d votos\n", cand_a, cand_b);
    printf("ENEIAS recebeu %d votos, JANGO recebeu %d votos\n", cand_c, cand_d);
    printf("_________________________________________________\n");
    printf("Nesta eleição tivemos %d votos brancos e %d votos nulos", branco, vot_nul);
    return 0;


}