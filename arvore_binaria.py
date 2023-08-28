from queue import Queue
class Arvore_Binaria:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir_esquerda(self, valor):
        if self.esquerda == None:
            self.esquerda = Arvore_Binaria(valor)
            
        else:
            novo_no = Arvore_Binaria(valor)
            novo_no.esquerda = self.esquerda
            self.esquerda = novo_no
            
    def inserir_direita(self, valor):
        if self.direita == None:
            self.direita = Arvore_Binaria(valor)
            
        else:
            novo_no = Arvore_Binaria(valor)
            novo_no.direita = self.direita
            self.direita = novo_no        
     
    def pre_order(self):
       print(self.valor)
       if self.esquerda:
        self.esquerda.pre_order()
        
       if self.direita:
        self.direita.pre_order()
        
    def in_order(self):
        if self.esquerda:
            self.esquerda.in_order()
        print(self.valor)

        if self.direita:
            self.direita.in_order()
            
    def pos_order(self):
        if self.esquerda:
            self.esquerda.pos_order()

        if self.direita:
            self.direita.pos_order()
        print(self.valor)
        
    def bfs(self):
        fila = Queue()
        fila.put(self)

        while not fila.empty():
            no_atual = fila.get()
            print(no_atual.valor)

            if no_atual.esquerda:
                fila.put(no_atual.esquerda)

            if no_atual.direita:
                fila.put(no_atual.direita)    
  
# Criando uma árvore binária
raiz = Arvore_Binaria(1)
raiz.inserir_esquerda(2)
raiz.inserir_direita(3)
raiz.esquerda.inserir_esquerda(4)
raiz.esquerda.inserir_direita(5)
raiz.direita.inserir_esquerda(6)
raiz.direita.inserir_direita(7)

# Testando as travessias
print("Pre-order Traversal:")
raiz.pre_order()

print("\nIn-order Traversal:")
raiz.in_order()

print("\nPost-order Traversal:")
raiz.pos_order()

print("\nBFS Traversal:")
raiz.bfs()   
        
#Teste
#Arvore = Arvore_Binaria('a')
#print(Arvore.valor)
#print(Arvore.esquerda)
#print(Arvore.direita)      
        

            
        