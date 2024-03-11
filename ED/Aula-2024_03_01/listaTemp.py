class  Lista:
    def __init__(self):
        self.inicio = None
    
    
    def mostrarLista(self):
        itemAtual = self.inicio
        while True:
            print(itemAtual.dado)
            if itemAtual.prox == None:
                break
            itemAtual = itemAtual.prox
            
            
    def addFim(self, item):
        itemAtual = self.inicio
        while True:
            if itemAtual.prox == None:
                itemAtual.prox = Item(item)
                break
            itemAtual = itemAtual.prox
            
            
    def addInic(self, dado):
        itemAtual = Item(dado)
        itemAtual.prox = self.inicio
        self.inicio = itemAtual
        
        
    
class Item:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        
lista = Lista()
lista.addInic("Blabla")
lista.addFim("lalala")
lista.mostrarLista()

        