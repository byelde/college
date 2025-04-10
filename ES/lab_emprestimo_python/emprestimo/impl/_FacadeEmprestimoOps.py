from typing import override, Type

from emprestimo.spec.dt.DTUsuario import DTUsuario
from emprestimo.spec.prov.IEmprestimoOps import IEmprestimoOps
from emprestimo.spec.prov.IManager import IManager
from emprestimo.spec.req.ILimiteReq import ILimiteReq


class _FacadeEmprestimoOps(IEmprestimoOps): # O "_" simula que a classe é de visibilidade de pacote

  """
  Facade interno para operações de empréstimo.

  ATENÇÃO: Esta classe é APENAS para uso interno do pacote
  ``emprestimo.impl``. Não deve ser chamada diretamente por
  código externo.

  Implementa a interface IEmprestimoOps atuando como um facade.

  Attributes:
      __manager (IManager): Gerenciador de interfaces para obtenção de dependências
      __intReq (ILimiteReq): Interface para requisição de limites, inicializada como tipo
  """

  def __init__(self, manager: IManager) -> None:
    self.__manager: IManager = manager
    self.__intReq: ILimiteReq = Type[ILimiteReq]


  @override
  def liberarEmprestimoAutomatico(self, cliente: DTUsuario) -> float:
    """
    Args:
        cliente (DTUsuario): Cliente contendo informações de rendimentos

    Returns:
        float: Valor do empréstimo liberado (90% do limite estimado)

        None: Em caso de falha

    Raises:
        ValueError: Se não for possível converter os rendimentos para float
        TypeError: Se os tipos dos parâmetros forem incorretos

    Note:
        - Faz tratamento automático de números com vírgula decimal
        - Imprime mensagens de log durante o processamento
        - Retorna None implicitamente em caso de falha (com log de erro)
    """


    try:
      rendimento: float = 0.0

      try:
        rendimento = float(cliente.rendimentos)

      except:
        print("Tratamento 1...")
        rendimento = float(cliente.rendimentos.replace(",","."))
        print("Erro tratado com sucesso!")


      if (rendimento > 1000):
        self.__intReq = self.__manager.getRequiredInterface("ILimiteReq")
        limite: float = self.__intReq.estimarLimite(cliente)
        return limite * 0.9

    except (ValueError, TypeError) as err:
      print("NUMERO ERRADO!!!", err)

