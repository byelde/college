from typing import Dict, override

from emprestimo.impl._FacadeEmprestimoOps import _FacadeEmprestimoOps
from emprestimo.spec.prov.IManager import IManager

class _Manager(IManager): # O "_" simula que a classe é de visibilidade de pacote

  """
  ATENÇÃO: Esta classe é destinada APENAS para uso interno do pacote
  ``emprestimo.impl``. Não deve ser instanciada ou chamada diretamente por
  código externo.

  Responsável por administrar as interfaces fornecidas e requeridas,
  atuando como um representante do componente ``emprestimo``.

  Attributes:
      __providedInterfaces (Dict[str, object]): Map de interfaces fornecidas.
      __requiredInterfaces (Dict[str, object]): Map de interfaces requeridas.
  """

  def __init__(self):
    self.__providedInterfaces: Dict[str, object] = dict()
    self.__requiredInterfaces: Dict[str, object] = dict()
    self.__providedInterfaces["IEmprestimoOps"] = _FacadeEmprestimoOps(self)
    self.__requiredInterfaces["ILimiteReq"] = None

  @override
  def getProvidedInterfaces(self) -> [str]:
    return self.__providedInterfaces.keys()
    pass

  @override
  def getRequiredInterfaces(self) -> [str]:
    return self.__requiredInterfaces.keys()
    pass

  @override
  def getProvidedInterface(self, interface_name: str) -> object:
    return self.__providedInterfaces[interface_name]
    pass

  @override
  def setRequiredInterface(self, interface_name: str, interface_object: object) -> None:
    self.__requiredInterfaces[interface_name] = interface_object
    pass

  @override
  def getRequiredInterface(self, interface_name: str) -> object:
    return self.__requiredInterfaces[interface_name]
    pass


