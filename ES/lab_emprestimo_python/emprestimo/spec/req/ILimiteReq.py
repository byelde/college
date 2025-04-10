from abc import ABC, abstractmethod # Importando classes e métodos abstratos
from emprestimo.spec.dt.DTUsuario import DTUsuario


class ILimiteReq(ABC): # A herança a ABC representa que a classe é abstrata
  """
  Interface para requisição de limites de crédito.

  Esta classe serve como uma construção de interface em Python, que não possui
  suporte nativo a interfaces, utilizando ABC (Abstract Base Class) para
  forçar a implementação dos métodos definidos.
  """

  @abstractmethod
  def estimarLimite(self, usuario: DTUsuario) -> float:
    """
    Calcula o limite de crédito disponível para um usuário.

    Args:
        usuario (DTUsuario): Record contendo os dados do usuário, incluindo:
                           - Rendimentos (obrigatório)

    Returns:
        float: Valor do limite de crédito estimado em unidades monetárias.
              Retorna 0.0 se não for possível conceder crédito.

    Raises:
        NotImplementedError: Se a classe concreta não implementar este método
        ValueError: Se os dados do usuário forem inválidos ou insuficientes
        TypeError: Se o tipo dos parâmetros for incorreto
    """
    pass