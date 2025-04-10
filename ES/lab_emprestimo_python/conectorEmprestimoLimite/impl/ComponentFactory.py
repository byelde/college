from abc import ABC

from conectorEmprestimoLimite.impl._Manager import _Manager
from limite.spec.prov.ILimiteOps import ILimiteOps


class ComponentFactory(ABC):
  """
  Fábrica abstrata para criação e gerenciamento de instâncias de _Manager do
  componente ``conectorEmprestimoLimite``.

  Esta classe atua como um Singleton, garantindo que apenas uma única
  instância de _Manager seja criada.

  Attributes:
      _manager (_Manager): Instância única do gerenciador do componente.
                          None se nenhuma instância foi criada ainda.

  Note:
      Esta classe é abstrata (indicado por ABC) e não deve ser instanciada
      diretamente.
  """

  _manager: _Manager = None

  @staticmethod
  def createInstance(limite_ops: ILimiteOps) -> _Manager:
    """
    Cria ou retorna a instância única de _Manager.

    Implementa o padrão Singleton para garantir que apenas uma instância
    de _Manager exista, inicializada com a interface de operações de limite.

    Args:
        limite_ops (ILimiteOps): Implementação concreta da interface ILimiteOps.

    Returns:
        _Manager: Instância única do gerenciador de interfaces.

    Note:
        Este método é thread-safe por natureza em Python para criação única,
        mas não garante thread-safety para operações subsequentes no _Manager.
    """
    if not ComponentFactory._manager:
      ComponentFactory._manager = _Manager(limite_ops)
    return ComponentFactory._manager
