class ListaDinamica:
    
    def __init__(self):
        self.inicio = None
    
    def mostrar(self):
        
        if self.inicio == None:
            print("A lista está vazia.")
        else:
            item_atual = self.inicio
            while True:
                print(item_atual.nome, ":", item_atual.nota)
                if item_atual.proximo == None:
                    break
                item_atual = item_atual.proximo 
    
    def addInicio(self, nome:str, nota:float):
        item_atual = Aluno(nome, nota)
        item_atual.proximo = self.inicio
        self.inicio = item_atual
    
    def addFim(self, nome:str, nota:float):
        if self.inicio == None:
            self.inicio = Aluno(nome, nota)
        
        else:
            item_atual = self.inicio
            
            while item_atual.proximo != None:
                item_atual = item_atual.proximo 
            item_atual.proximo = Aluno(nome, nota)
        
    def estaVazio(self):
        return self.inicio == None
    
    def buscarNome(self, nome:str):
        item_atual = self.inicio
        lista_achados = ListaDinamica()
        
        while item_atual != None:
            if item_atual.nome == nome:
                lista_achados.addFim(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo 
        
        if lista_achados.estaVazio():
            print("Nome não encontrado no banco de dados.")
            return -1
        else:
            return lista_achados
    
    def buscarNota(self, nota:float):
        item_atual = self.inicio
        lista_achados = ListaDinamica()
        
        while item_atual != None:
            if item_atual.nota == nota:
                lista_achados.addFim(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo 
            
        if lista_achados.estaVazio():
            print("Nota não encontrado na banco de dados.")
            return -1
        else:
            return lista_achados
    
    def retirarNome(self, nome:str):
        
        item_atual = self.inicio
        encontrado = False
        
        while item_atual:
            if self.inicio.nome == nome: # Caso o primeiro item seja alvo, o início passará ser o segundo item.
                encontrado = True
                self.inicio = self.inicio.proximo
            if item_atual.proximo and item_atual.proximo.nome == nome:
                encontrado = True
                item_atual.proximo = item_atual.proximo.proximo
            else:
                item_atual = item_atual.proximo
        
        if not encontrado:
            print("Nome não encontrado no banco de dados.")
      
    def retirarNota(self, nota:float):
        
        item_atual =  self.inicio
        encontrado = False
        
        while item_atual:
            if self.inicio.nota == nota: # Caso o primeiro item seja alvo, o início passará ser o segundo item.
                encontrado = True
                self.inicio = self.inicio.proximo
            if item_atual.proximo and item_atual.proximo.nota == nota:
                encontrado = True
                item_atual.proximo = item_atual.proximo.proximo
            else:
                item_atual = item_atual.proximo
                
        if not encontrado:
            print("Nota não encontrada na base de dados.")
   
    def esvaziar(self):
        if self.estaVazio():
            return(print("Lista já vazia."))
        else:
            self.inicio = None
        
        
class Aluno:
    def __init__(self, nome:str, nota:float):
        self.nome, self.nota = nome, nota
        self.proximo = None