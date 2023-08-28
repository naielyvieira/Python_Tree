class No:
    def __init__(self, valor = None):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class Arvore_Binaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(valor, self.raiz)
            
    def _inserir(self, valor, raiz):
        if raiz.esquerda is None:
            raiz.esquerda = No(valor)
        elif raiz.direita is None:
            raiz.direita = No(valor)
        else:
            if raiz.esquerda.direita is None:
                self._inserir(valor, raiz.esquerda)
            else:
                self._inserir(valor, raiz.direita)
                
                
