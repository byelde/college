def busca_bin( vetor, buscado ):

    import math

    comparacoes = 0;
    indexBuscado = 0;
    meioIndex = 0;
    encontrado = False;
    tam = 0;

    print(f"Array de tamanho: {len(vetor)}");

    while (True):

        tam = len(vetor);

        meioIndex = math.ceil((tam/2))-1;
        if meioIndex == -1:
            break

        if ( vetor[meioIndex] == buscado ):
            indexBuscado += len(vetor[:meioIndex+1])-1;
            comparacoes += 1;
            encontrado = True;
            break;
        
        elif ( vetor[meioIndex] > buscado ):
            comparacoes += 2;
            vetor = vetor[:meioIndex];
        
        else:
            indexBuscado += len(vetor[:meioIndex+1])
            comparacoes += 3;
            vetor = vetor[meioIndex+1:];


    if encontrado == False:
        print(f"Valor não encontrado");
    else:
        print(f"Valor encontrado no índice {indexBuscado}");

    print(f"Quantidade de comparações: {comparacoes}\n");

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