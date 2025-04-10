from limite.impl._Manager import _Manager
from limite.spec.prov.IManager import IManager
from abc import ABC

class ComponentFactory(ABC):
  """
  Fábrica abstrata para criação e gerenciamento de instâncias de _Manager do
  componente ``limite``.

  Esta classe atua como um Singleton, garantindo que apenas uma única
  instância de _Manager seja criada.

  Attributes:
      _manager (_Manager): Instância única do gerenciador de componente.
                          None se nenhuma instância foi criada ainda.

  Note:
      Esta classe é abstrata (indicado por ABC) e não deve ser instanciada
      diretamente.
  """
  _manager: IManager = None

  @staticmethod
  def createInstance() -> IManager:
    """
    Cria ou retorna a instância única de _Manager.

    Implementa o padrão Singleton para garantir que apenas uma instância
    de _Manager exista.

    Returns:
        _Manager: Instância única do gerenciador de interfaces.

    Note:
        Este método é thread-safe por natureza em Python para criação única,
        mas não garante thread-safety para operações subsequentes no _Manager.
    """
    if not ComponentFactory._manager:
      ComponentFactory._manager = _Manager()
    return ComponentFactory._manager
