from typing import override

from limite.spec.dt.DTCliente import DTCliente
from limite.spec.prov.ILimiteOps import ILimiteOps

class _FacadeLimiteOps(ILimiteOps): # O "_" simula que a classe é de visibilidade de pacote

  """
  Facade que implementa a interface ILimiteOps.

  ATENÇÃO: Esta classe é APENAS para uso interno do pacote
  ``limite.impl``. Não deve ser chamada diretamente por
  código externo.

  Implementa a interface ILimiteOps atuando como um facade.
  """

  @override
  def calcularLimite(self, cliente: DTCliente) -> float:
    limite: float = cliente.salario * 0.29
    return limite if limite >= 0 else 0