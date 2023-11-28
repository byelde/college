def busca_seq( vetor, buscado ):

    comparacoes = 0;
    encontrado = False;

    for i, valor in enumerate( vetor ):
        comparacoes += 1;
        if valor == buscado:
            encontrado = True
            break;

    print(f"Array de tamanho: { len( vetor ) }");

    if encontrado == False:
        print(f"Valor não encontrado");
    else:
        print(f"Valor encontrado no índice: { i }");
        
    print(f"Quantidade de comparações: { comparacoes }\n");


if __name__ == "__main__":

    vetores = [
        [14, 21, 5, 45, 12, 3, 86, 98, 46, 53, 24, 2, 1, 15, 90, 47],
        [1, 2, 3, 5, 12, 14, 15, 21, 24, 45, 46, 47, 53, 86, 90, 98]
    ];

    valoresBuscados = [14, 46, 90, 50];

    for idVetor, vetor in enumerate(vetores):
        for valor in valoresBuscados:
            print( "-=" * 20 );
            print(f"\n Valor { valor } buscado no vetor { idVetor+1 }. \n");
            busca_seq( vetor, valor );

    # Eficiência - Busca Sequencial
    # Melhor caso: O(1) - O valor é encontrado na primeira tentativa;
    # Pior caso: O(n) - É necessário percorrer todos os dados;
    # Caso médio: O(n+1/2) - É necessário chegar ao termo central;