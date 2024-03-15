class ListaDinamica:
    def __init__(self):
       self.inicio, self.inicio = None, None
    
    def mostrar(self, reverse:bool = False):
        if self.inicio == None:
            print("A lista está vazia.")
            return
        
        if not reverse:
            
            item_atual = self.inicio
            print(f"{item_atual.nome}:{ item_atual.nota}")
            item_atual = item_atual.proximo 
            
            while item_atual != self.inicio:
                print(f"{item_atual.nome}:{ item_atual.nota}")                
                item_atual = item_atual.proximo 
                
        else:
            
            item_atual = self.fim
            print(f"{item_atual.nome}:{ item_atual.nota}")
            item_atual = item_atual.anterior 
            
            while item_atual != self.fim:
                print(f"{item_atual.nome}:{ item_atual.nota}")
                item_atual = item_atual.anterior
       
    def addInicio(self, nome:str, nota:float):
        
        if self.inicio == None:
            self.fim = self.inicio = Aluno(nome, nota)
            self.inicio.proximo = self.inicio.anterior = self.fim
            self.fim.proximo = self.fim.anterior = self.inicio

        else:
            novo_item = Aluno(nome, nota)
            novo_item.proximo = self.inicio
            self.inicio.anterior = novo_item
            self.inicio = novo_item
            self.inicio.anterior = self.fim
            self.fim.proximo = self.inicio
    
    def addFim(self, nome:str, nota:float):
        if self.inicio == None:
            self.fim = self.inicio = Aluno(nome, nota)
            self.inicio.proximo = self.inicio.anterior = self.fim
            self.fim.proximo = self.fim.anterior = self.inicio

        else:
            novo_item = Aluno(nome, nota)
            novo_item.anterior = self.fim
            self.fim.proximo = novo_item
            self.fim = novo_item
            self.fim.proximo = self.inicio
            self.inicio.anterior = self.fim
               
    def addListaFim(self, array:list):
        for item in array:
            self.addFim(item.nome, item.nota)               
      
    def comprimento(self):
        
        if self.inicio == None:
            return 0
        
        item_atual = self.inicio
        tamanho = 1
        item_atual = item_atual.proximo 
        
        while item_atual != self.inicio:
            tamanho += 1              
            item_atual = item_atual.proximo
            
        return tamanho
    
    def vetorizar(self):
        vetor = []
        
        if self.inicio == None:
            return vetor
        
        item_atual = self.inicio
        vetor.append(item_atual)
        item_atual = item_atual.proximo 
        
        while item_atual != self.inicio:
            vetor.append(item_atual)            
            item_atual = item_atual.proximo
            
        return vetor
       
    def estaVazio(self):
        return self.inicio == None
    
    def buscarNome(self, nome:str):
        
        if self.inicio == None:
            print("Lista vazia")
            return
        
        lista_achados = ListaDinamica()
        item_atual = None
        
        while item_atual != self.inicio:
            
            if not item_atual:
                item_atual = self.inicio 
            
            if item_atual.nome == nome:
                lista_achados.addFim(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo 
        
        if lista_achados.estaVazio():
            print("Nome não encontrado no banco de dados.")
            return -1
        else:
            return lista_achados
    
    def buscarNota(self, nota:float):
        if self.inicio == None:
            print("Lista vazia")
            return
        
        lista_achados = ListaDinamica()
        item_atual = None
        
        while item_atual != self.inicio:
            
            if not item_atual:
                item_atual = self.inicio 
            
            if item_atual.nota == nota:
                lista_achados.addFim(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo 
            
        if lista_achados.estaVazio():
            print("Nota não encontrada no banco de dados.")
            return -1
        else:
            return lista_achados
    
    def retirarNome(self, nome:str):
        
        if self.estaVazio():
            return(print("Lista vazia."))
        
        item_atual, encontrado = None, False
        
        while True:
            if not item_atual:
                item_atual = self.inicio

            if item_atual.nome == nome:
                encontrado = True
        #       remover se estiver no começo
                if item_atual == self.inicio:
                    self.inicio = self.inicio.proximo
                    self.inicio.anterior = self.fim
                    self.fim.proximo = self.inicio
                    
        #       remover se estiver no fim
                elif item_atual == self.fim:
                    self.fim = self.fim.anterior
                    self.fim.proximo = self.inicio
                    self.inicio.anterior = self.fim
                    
        #       remover se for uma lista unitária
                elif self.fim == self.inicio:
                    self.inicio = self.fim = None
                    
        #       remover se estiver no meio
                else:
                    item_atual.anterior.proximo = item_atual.proximo
                    item_atual.proximo.anterior = item_atual.anterior
                    
            if item_atual == self.fim:
                break
                    
            item_atual = item_atual.proximo
            
        if not encontrado:
            print("Nome não encontrado no banco de dados.")
                 
    def retirarNota(self, nota:float):
        
        if self.estaVazio():
            return(print("Lista vazia."))
        
        item_atual, encontrado = None, False
        
        while True:
            if not item_atual:
                item_atual = self.inicio

            if item_atual.nota == nota:
                encontrado = True
        #       remover se estiver no começo
                if item_atual == self.inicio:
                    self.inicio = self.inicio.proximo
                    self.inicio.anterior = self.fim
                    self.fim.proximo = self.inicio
                    
        #       remover se estiver no fim
                elif item_atual == self.fim:
                    self.fim = self.fim.anterior
                    self.fim.proximo = self.inicio
                    self.inicio.anterior = self.fim
                    
        #       remover se for uma lista unitária
                elif self.fim == self.inicio:
                    self.inicio = self.fim = None
                    
        #       remover se estiver no meio
                else:
                    item_atual.anterior.proximo = item_atual.proximo
                    item_atual.proximo.anterior = item_atual.anterior
                    
            if item_atual == self.fim:
                break
                    
            item_atual = item_atual.proximo
            
        if not encontrado:
            print("Nota não encontrada no banco de dados.")

    def esvaziar(self):
        if self.estaVazio():
            return(print("Lista já vazia."))
        else:
            self.fim = self.inicio = None
        
        
class Aluno:
    def __init__(self, nome:str, nota:float):
        self.nome, self.nota = nome, nota
        self.proximo = None
        self.anterior = None

lista = ListaDinamica()
array = [Aluno("Gabs", 10), Aluno("Eduardo", 10), Aluno("Kenandja", 10)]
lista.addListaFim(array)
lista.mostrar()
print(lista.comprimento())
print(lista.vetorizar())