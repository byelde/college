Erro inesperado:    
        No construtor de telegrama, não era possível realizar a operação 
            this.nome = nome;
    onde "this.nome" se refere ao atributo "nome" passado pela super 
    classe "Documento" no pacote "pacote1" e apenas "nome" se refere ao 
    parametro passado para o construtor.
        O erro acontecia devido ao fato do atributo "nome", oriundo da
    super classe "Documento", ter a visibilidade de pacote e não poder
    ser "alcançado" no pacote "pacote2".
        Para corrigir, criei, em "Documento", um método protegido chamado
    "setNome" capaz de definir o atributo nome da classe "Documento"
    em todas as classes orginadas nela, mesmo que esteja em outro
    pacote.

Tópico 10:
        Não é possível consultar de forma direta o atributo data da instância
    da Classe carta, pois seu atributo está "protegido", portanto incapaz de
    ser consultado dessa forma. Para solucionar, criei, na classe "Carta" um
    método público chamado "getData()" capaz de retorna o seu dado "data".
    Fiz o mesmo para a classe "Telegrama" por questões de boas práticas.

Tópico 11:
        Ocorreu um erro de tipo, pois a classe "Carta", inicialmente, não 
    está visível para o arquivo "Inicial.java" por estarem em pacotes 
    diferentes. Para corrigir isso, bastou apenas importar a classe "Carta"
    do pacote "pacote1".
