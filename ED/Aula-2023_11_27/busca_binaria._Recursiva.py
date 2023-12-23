from math import ceil

def busca_bin_rec( vetor, indexInit, indexFinal, buscado, comparacoes = 0 ):

    index = ceil((indexFinal + indexInit)/2);

    if ( vetor[index] == buscado ):

        comparacoes += 1;
        print(f"Array de tamanho: {len(vetor)}");
        print(f"Valor encontrado no index {index}");
        print(f"Quantidade de comparações: {comparacoes}");
        return True;

    elif ( indexInit > indexFinal ):

        comparacoes += 2;
        print(f"Array de tamanho: {len(vetor)}");
        print("Valor não encontrado");
        print(f"Quantidade de comparações: {comparacoes}");
        return False;

    elif ( vetor[index] < buscado ):
        comparacoes += 3;
        busca_bin_rec( vetor, index+1, indexFinal, buscado, comparacoes);

    else:
        busca_bin_rec( vetor, indexInit, index-1, buscado, comparacoes);

    

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
            busca_bin_rec( vetor, 0, len(vetor) - 1, valor );