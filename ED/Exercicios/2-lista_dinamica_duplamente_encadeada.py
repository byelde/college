class ListaDinamica:
    def __init__(self):
        self.inicio = None
    
    def mostrar(self, reverse = False):
        if self.inicio == None:
            print("A lista está vazia.")
            
        if not reverse:
            
            item_atual = self.inicio
            
            while True:
                print(f"{item_atual.nome}:{ item_atual.nota}")
                
                if item_atual.proximo == None:
                    break
                item_atual = item_atual.proximo 
                
        else:
            
            item_atual = self.inicio
            
            while item_atual.proximo != None:
                item_atual = item_atual.proximo
            
            while item_atual:
                print(f"{item_atual.nome}:{ item_atual.nota}")
                item_atual = item_atual.anterior
                
            
    
    def addInicio(self, nome, nota):
        
        if self.inicio == None:
            self.inicio = Aluno(nome, nota)
        else:
            novo_item = Aluno(nome, nota)
            novo_item.proximo = self.inicio
            self.inicio.anterior = novo_item
            self.inicio = novo_item
    
    def addFim(self, nome, nota):
        if self.inicio == None:
            self.inicio = Aluno(nome, nota)
        
        else:
            item_atual = self.inicio
            
            while item_atual.proximo != None:
                item_atual = item_atual.proximo 
            item_atual.proximo = Aluno(nome, nota)
            item_atual.proximo.anterior = item_atual
        
    def estaVazio(self):
        print(self.inicio == None)
    
    def buscarNome(self, nome):
        item_atual = self.inicio
        lista_achados = ListaDinamica()
        
        while item_atual != None:
            if item_atual.nome == nome:
                lista_achados.addFim(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo 
            
        return lista_achados
    
    def buscarNota(self, nota):
        item_atual = self.inicio
        lista_achados = ListaDinamica()
        
        while item_atual != None:
            if item_atual.nota == nota:
                lista_achados.addFim(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo 
            
        return lista_achados
    
    def retirarNome(self, nome):
        
        item_atual =  self.inicio
        
        while item_atual:
            if self.inicio.nome == nome: # Caso o primeiro item seja alvo, o início passará ser o segundo item.
                self.inicio = self.inicio.proximo
                self.inicio.anterior = None
            if item_atual.proximo and item_atual.proximo.nome == nome:
                item_atual.proximo = item_atual.proximo.proximo
                item_atual.proximo.anterior = item_atual
            else:
                item_atual = item_atual.proximo
            
    def retirarNota(self, nota):
        
        item_atual =  self.inicio
        
        while item_atual:
            if self.inicio.nota == nota: # Caso o primeiro item seja alvo, o início passará ser o segundo item.
                self.inicio = self.inicio.proximo
                self.inicio.anterior = None
            if item_atual.proximo and item_atual.proximo.nota == nota:
                item_atual.proximo = item_atual.proximo.proximo
                item_atual.proximo.anterior = item_atual
            else:
                item_atual = item_atual.proximo
   
    def esvaziar(self):
        self.inicio = None
        
        
class Aluno:
    def __init__(self, nome, nota):
        self.nome, self.nota = nome, nota
        self.proximo = None
        self.anterior = None