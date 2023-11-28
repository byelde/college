def busca_bin( vetor, buscado ):

    import math

    indexInit = 0;
    indexFinal = len(vetor)-1;
    comparacoes = 0;

    print(f"Array de tamanho: {len(vetor)}");

    while (indexFinal != indexInit):

        index = math.ceil((indexFinal + indexInit)/2);

        if ( vetor[index] == buscado):
            comparacoes += 1;
            print(f"Valor encontrado no Index: {index}");
            break;

        elif ( vetor[index] < buscado ):
            comparacoes += 2;
            indexInit = index+1;
        
        else:
            comparacoes += 3;
            indexFinal = index-1;

    else:
        print("Valor não encontrado");

    print(f"Quantidade de comparações: {comparacoes}");
        

def bubbleSort( vetor ):
    tam = len( vetor );

    for rep in range( tam-1 ):

        alterado = False;

        for idValor in range( tam-1 ):

            if ( vetor[idValor] > vetor[idValor+1] ):
                vetor[idValor], vetor[idValor+1] = vetor[idValor+1], vetor[idValor];
                alterado = True;
        
        if not alterado:
            break;

if __name__ == "__main__":

    vetores = [
        [14, 21, 5, 45, 12, 3, 86, 98, 46, 53, 24, 2, 1, 15, 90, 47],
        [1, 2, 3, 5, 12, 14, 15, 21, 24, 45, 46, 47, 53, 86, 90, 98]
    ];

    valoresBuscados = [14, 46, 90, 50];

    bubbleSort( vetores[0] );

    for idVetor, vetor in enumerate(vetores):
        for valor in valoresBuscados:
            print( "-=" * 20 );
            print(f"\n Valor { valor } buscado no vetor { idVetor+1 }. \n");
            busca_bin( vetor, valor );

    # Eficiência - Busca Binária
    # Melhor caso: O(1);
    # Pior caso: O(log n);
    # Caso médio: O(Log n);