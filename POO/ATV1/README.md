
# Laboratório POO - Atividade 01

## Visibilidade em POO

Execução da atividade 01 do laboratório de POO exigidida pelo docente Patrick Brito afim de compor a nota da Avaliação Bimestral 1 (AB1).

Clique [aqui](POOATV1.pdf) para ter acesso ao pdf da atividade.

## Questões
**10**. Na classe Telegrama, crie o método `mostrar2()`, que instancia dois objetos: um do tipo `Carta` e outro do tipo `Telegrama`; em seguida, imprima o valor do atributo data de ambos os objetos. O que aconteceu? Como você poderia corrigir o problema? Justifique através de um comentário no código.

#### Erro:
<p align="center">
  <img src="https://github.com/user-attachments/assets/c7f874c7-fdc9-4875-8130-09e28c3684dd">
</p>

**Reposta**: Não é possível consultar de forma direta o atributo data da instância da classe `carta`, pois seu atributo está `protected`, portanto incapaz de ser consultado dessa forma. Para solucionar, criei, na classe `Carta` um método público chamado `getData()` capaz de retorna o seu dado data. Fiz o mesmo para a classe `Telegrama` por questões de boas práticas.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e167df04-8807-46e6-a14b-6540c5be53d4">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4890d8ac-8506-4fe0-8098-e8fec18262fb">
</p>

***

**12**. Na classe Inicial, crie o método `main()`, que instancie um objeto do tipo Carta e imprima na tela os valores dos atributos do objeto. O que aconteceu? Como você poderia corrigir o problema? Justifique através de um comentário no código.

#### Erro:

<p align="center">
  <img src="https://github.com/user-attachments/assets/a1736b35-6bcd-4df9-8364-4f757cba4eeb">
</p>

**Resposta**: Ocorreu um erro de visibilidade no atributos da instância de `Carta`, pois os atributos de `Carta` têm a visibilidade `protected` (data) e de `standard` (nome e anexo), portanto invisíveis para o arquivo `Inicial.java`. Para evitar o erro, bastou usar o método público `mostra()` já existente na classe `Carta`.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9898c9cb-1f94-4a8c-88b5-36a0131c1bab">
</p>
