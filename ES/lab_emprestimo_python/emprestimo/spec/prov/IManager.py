from abc import ABC, abstractmethod # Importando classes e métodos abstratos

class IManager(ABC): # A herança a ABC representa que a classe é abstrata
  """
  Responsável por administrar as interfaces fornecidas e requeridas,
  atuando como um representante do componente ``emprestimo``.
  """

  @abstractmethod # A flag torna o metodo abstrato
  def getProvidedInterfaces(self) -> [str]:
    """
    Retorna os nomes das interfaces fornecidas pelo componente.

    Returns:
        List[str]: lista de chaves das interfaces disponíveis.
    """


  @abstractmethod  # A flag torna o metodo abstrato
  def getRequiredInterfaces(self) -> [str]:
    """
    Retorna os nomes das interfaces requeridas pelo componente.

    Returns:
        List[str]: lista de chaves das interfaces necessárias.
    """


  @abstractmethod  # A flag torna o metodo abstrato
  def getProvidedInterface(self, interface_name: str) -> object:
    """
    Obtém, pelo nome, uma interface fornecida pelo componente.

    Args:
        interface_name (str): Nome da interface desejada.

    Returns:
        object: implementação da interface solicitada.

    Raises:
        KeyError: Se a interface não existir no dicionário.
    """


  @abstractmethod  # A flag torna o metodo abstrato
  def setRequiredInterface(self, interface_name: str, interface_object: object) -> None:
    """
    Define uma interface requerida pelo componente.

    Args:
        interface_name (str): nome da interface.
        interface_object (object): implementação da interface.
    """


  @abstractmethod # A flag torna o metodo abstrato
  def getRequiredInterface(self, interface_name: str) -> object:
    """
    Retorna, utilizando o nome, uma interface requerida pelo componente.

    Args:
        interface_name (str): Nome da interface desejada.

    Returns:
        object: implementação da interface solicitada.

    Raises:
        KeyError: Se a interface não existir no dicionário.
    """