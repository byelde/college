from typing import override

from emprestimo.spec.dt.DTUsuario import DTUsuario
from limite.spec.dt.DTCliente import DTCliente
from emprestimo.spec.req.ILimiteReq import ILimiteReq
from limite.spec.prov.ILimiteOps import ILimiteOps


class _Adapter(ILimiteReq): # O "_" simula que a classe é de visibilidade de pacote
    """
        ATENÇÃO: uso INTERNO ao pacote ``conectorEmprestimoLimite.impl``.

        Ao mesmo tempo que atua como uma classe implementável do
        tipo ILimiteReq do componente Emprestimo, A classe Adapter
        atua como um "tradutor" entre as interfaces, convertendo a
        interface de uma classe em outra interface esperada pelo cliente.
        Além disso, métodos para conversão de tipos de dados
    """

    def __init__(self, limite_ops: ILimiteOps):
      self.__limite_ops = limite_ops


    @override
    def estimarLimite(self, usuario: DTUsuario) -> float:
      """
      Adapta a operação 'estimarLimite' de ILimiteReq para o tipo ILimiteOps.

      Esta função converte a chamada de estimativa de limite da interface ILimiteReq
      em um formato compatível com ILimiteOps, permitindo a interoperabilidade.

      Args:
          usuario (str): ID ou objeto do usuário para o qual o limite será estimado.

      Returns:
          float: valor do limite estimado.

      Raises:
          ValueError: Se o usuário for inválido.
          TypeError: Se a conversão entre interfaces falhar.
      """
      cliente: DTCliente = self.__usuarioToCliente(usuario)
      return self.__limite_ops.calcularLimite(cliente)


    @staticmethod
    def __usuarioToCliente(usuario: DTUsuario) -> DTCliente:
      """
      Converte um objeto DTUsuario em um DTCliente, extraindo os rendimentos.

      Este método estático realiza a adaptação de um objeto do tipo DTUsuario
      para um objeto DTCliente, utilizando o atributo 'rendimentos' como base
      para a criação do novo objeto.

      Args:
          usuario (DTUsuario): Objeto contendo os dados do usuário, inclui rendimentos.

      Returns:
          DTCliente: Objeto do tipo Cliente criado a partir dos rendimentos do usuario.

      Raises:
          TypeError: Se 'cliente.rendimentos' não for um valor numérico ou conversível para float.
          ValueError: Se 'cliente.rendimentos' for um valor inválido (ex.: negativo).
      """
      return DTCliente(float(usuario.rendimentos))