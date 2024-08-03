
# Laboratório POO - Atividade 01

## Visibilidade em POO

Execução da atividade 01 do laboratório de POO exigidida pelo docente Patrick Brito afim de compor a nota da Avaliação Bimestral 1 (AB1).

[Arquivo da atividade]

## Questões
**10**. Na classe Telegrama, crie o método `mostrar2()`, que instancia dois objetos: um do tipo `Carta` e outro do tipo `Telegrama`; em seguida, imprima o valor do atributo data de ambos os objetos. O que aconteceu? Como você poderia corrigir o problema? Justifique através de um comentário no código.

**Reposta**: Não é possível consultar de forma direta o atributo data da instância da Classe carta, pois seu atributo está `protected`, portanto incapaz de ser consultado dessa forma. Para solucionar, criei, na classe `Carta` um método público chamado `getData()` capaz de retorna o seu dado data. Fiz o mesmo para a classe `Telegrama` por questões de boas práticas.

***

**11**. Na classe Inicial, crie o método `main()`, que instancie um objeto do tipo Carta e imprima na tela os valores dos atributos do objeto. O que aconteceu? Como você poderia corrigir o problema? Justifique através de um comentário no código.

**Resposta**: Ocorreu um erro de tipo, pois a classe `Carta`, inicialmente, não está visível para o arquivo `Inicial.java` por estarem em pacotes diferentes. Para corrigir isso, bastou apenas importar a classe `Carta` do pacote `pacote1`.