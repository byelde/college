from abc import ABC, abstractmethod # Importando classes e métodos abstratos
from limite.spec.dt.DTCliente import DTCliente


class ILimiteOps(ABC):
  """
    A classe abstrata irá representar o conceito de
    Interface já que o python não possui o possui.
  """
  @abstractmethod # A flag torna o metodo abstrato
  def calcularLimite(self, cliente:DTCliente) -> float:
    """
    Calcula o limite de crédito baseado no salário do cliente.

    Args:
        cliente (DTCliente): Record contendo os dados do cliente, que deve
                           incluir obrigatoriamente o atributo 'salario'.

    Returns:
        float: valor do limite de crédito calculado (29% do salário).
               Retorna 0.0 caso o cálculo resulte em valor negativo.

    Raises:
        AttributeError: Se o objeto cliente não possuir o atributo 'salario'
        TypeError: Se o salário não for um valor numérico

    Note:
        - Valores negativos são automaticamente convertidos para 0.0
    """
    pass