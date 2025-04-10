from conectorEmprestimoLimite.impl.ComponentFactory import ComponentFactory as ComponentFactoryCon
from emprestimo.impl.ComponentFactory import ComponentFactory as ComponentFactoryEmp
from limite.impl.ComponentFactory import ComponentFactory as ComponentFactoryLim

from emprestimo.spec.prov.IManager import IManager as IManagerEmp
from limite.spec.prov.IManager import IManager as IManagerLim
from conectorEmprestimoLimite.impl.IManager import IManager as IManagerCon

from limite.spec.prov.ILimiteOps import ILimiteOps

from emprestimo.spec.dt.DTUsuario import DTUsuario
from emprestimo.spec.prov.IEmprestimoOps import IEmprestimoOps


def execucao():

    # CONFIGURAÇÃO ARQUITETURAL =========================================================================
    com_emp: IManagerEmp = ComponentFactoryEmp.createInstance()
    com_lim: IManagerLim = ComponentFactoryLim.createInstance()
    limite_ops: ILimiteOps|object = com_lim.getProvidedInterface("ILimiteOps")
    com_con: IManagerCon = ComponentFactoryCon.createInstance(limite_ops=limite_ops)
    usuario: DTUsuario = DTUsuario("1500.50")

    com_emp.setRequiredInterface("ILimiteReq", com_con.getProvidedInterface("ILimiteOps"))
    # ===================================================================================================


    obj_emprestimos_ops:IEmprestimoOps|object = com_emp.getProvidedInterface("IEmprestimoOps")
    print(obj_emprestimos_ops.liberarEmprestimoAutomatico(usuario))

if __name__ == '__main__':
    execucao()
