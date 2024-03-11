class ListaDinamica:
    def __init__(self):
        self.inicio = None
    
    def itens(self):
        
        if self.inicio == None:
            print("A lista está vazia.")
        else:
            item_atual = self.inicio
            while True:
                print(item_atual.nome, ":", item_atual.nota)
                if item_atual.proximo == None:
                    break
                item_atual = item_atual.proximo 
    
    def addInicio(self, nome, nota):
        item_atual = Aluno(nome, nota)
        item_atual.proximo = self.inicio
        self.inicio = item_atual
    
    def addFim(self, nome, nota):
        if self.inicio == None:
            self.inicio = Aluno(nome, nota)
        
        else:
            item_atual = self.inicio
            
            while item_atual.proximo != None:
                item_atual = item_atual.proximo 
            item_atual.proximo = Aluno(nome, nota)
        
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
            if item_atual.proximo and item_atual.proximo.nome == nome:
                item_atual.proximo = item_atual.proximo.proximo
            else:
                item_atual = item_atual.proximo
            
    def retirarNota(self, nota):
        
        item_atual =  self.inicio
        
        while item_atual:
            if self.inicio.nota == nota: # Caso o primeiro item seja alvo, o início passará ser o segundo item.
                self.inicio = self.inicio.proximo
            if item_atual.proximo and item_atual.proximo.nota == nota:
                item_atual.proximo = item_atual.proximo.proximo
            else:
                item_atual = item_atual.proximo
   
    def esvaziar(self):
        self.inicio = None
        
        
class Aluno:
    def __init__(self, nome, nota):
        self.nome, self.nota = nome, nota
        self.proximo = None