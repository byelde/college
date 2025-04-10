from typing import Dict, override, List

from conectorEmprestimoLimite.impl.IManager import IManager
from conectorEmprestimoLimite.impl._Adapter import _Adapter
from limite.spec.prov.ILimiteOps import ILimiteOps


class _Manager(IManager): # O "_" simula que a classe é de visibilidade de pacote
  """
  ATENÇÃO: Esta classe é destinada APENAS para uso interno do pacote
  ``conectorEmprestimoLimite.impl``. Não deve ser instanciada ou
  chamada diretamente por código externo.

  Responsável por administrar as interfaces fornecidas e requeridas,
  atuando como um representante do componente ``conectorEmprestimoLimite``.

  Attributes:
      __providedInterfaces (Dict[str, object]): Map de interfaces fornecidas.
      __requiredInterfaces (Dict[str, object]): Map de interfaces requeridas.
  """

  def __init__(self, limite_ops: ILimiteOps):
    self.__requiredInterfaces: Dict[str, object] = dict()
    self.__providedInterfaces: Dict[str, object] = dict()
    self.__providedInterfaces["ILimiteOps"] = _Adapter(limite_ops)


  @override
  def getProvidedInterfaces(self) -> [str]:
    return self.__providedInterfaces.keys()


  @override
  def getRequiredInterfaces(self) -> [str]:
    return self.__requiredInterfaces.keys()


  @override
  def getProvidedInterface(self, interface_name: str) -> object:
    return self.__providedInterfaces[interface_name]


  @override
  def setRequiredInterface(self, interface_name: str, interface_object: object) -> None:
    self.__requiredInterfaces[interface_name] = interface_object


  @override
  def getRequiredInterface(self, interface_name: str) -> object:
    return self.__requiredInterfaces[interface_name]


