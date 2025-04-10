from typing import Dict, override

from limite.impl._FacadeLimiteOps import _FacadeLimiteOps
from limite.spec.prov.IManager import IManager

class _Manager(IManager):

  """
    ATENÇÃO: Esta classe é APENAS para uso interno do pacote.
    Não deve ser chamada diretamente por código externo.
  """

  def __init__(self):
    self.__providedInterfaces: Dict[str, object] = dict()
    self.__requiredInterfaces: Dict[str, object] = dict()
    self.__providedInterfaces["ILimiteOps"] = _FacadeLimiteOps()

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


