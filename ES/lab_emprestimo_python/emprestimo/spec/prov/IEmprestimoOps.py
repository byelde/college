from abc import ABC, abstractmethod
from emprestimo.spec.dt.DTUsuario import DTUsuario

class IEmprestimoOps(ABC): # A herança a ABC representa que a classe é abstrata
  """
  Interface para operações de empréstimo.

  Esta classe abstrata serve como substituto para o conceito de interface
  em Python, que não é nativamente suportado como construção de linguagem.

  Note:
      Todas as classes que implementam esta interface devem fornecer uma
      implementação concreta do método `liberarEmprestimoAutomatico`.
  """

  @abstractmethod
  def liberarEmprestimoAutomatico(self, cliente: DTUsuario) -> float:
    """Método abstrato para liberação automática de empréstimo.

    Args:
        cliente (DTUsuario): Record contendo os dados do cliente. Deve
                          incluir pelo menos as informações de rendimentos.

    Returns:
        float: Valor do empréstimo a ser liberado. Retorna 0.0 se o empréstimo
              não for aprovado.

    Raises:
        NotImplementedError: Se a classe filha não implementar este método
        ValueError: Se os dados do cliente forem inválidos ou insuficientes
        TypeError: Se o tipo dos parâmetros for incorreto

    Note:
        - O valor retornado deve ser sempre positivo ou zero
    """