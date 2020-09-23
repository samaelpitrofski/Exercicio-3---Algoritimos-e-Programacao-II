from No import No

class Pilha: 
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def vazio(self):
        if self.tamanho == 0:   # Verifica se a pilha está vazia.
            return True  
        return False
        

    def adicionar(self, valor):
        no = No(valor)                      #No recebe o input do main
        if self.vazio():                       #Se a pilha estiver vazio o primeiro item a entrar nela é o valor inserido
            self.primeiro = no
        else:
            auxiliar = self.primeiro            #Caso a pilha não estaja vazia ele inseri o valor digita sobre o valor anterior, tornando o como primeiro
            self.primeiro = no
            no.proximo = auxiliar
        self.tamanho += 1                   #Concatena cada vez que adicionar um valor na pilha

    def imprimirpilha(self):
        if self.vazio():
            print('A Pilha está vazia')                  #Se a lista está vazia mostra um o erro
        else:
            auxiliar = self.primeiro                     #caso contrario ele print a lista em ordem de cadastro
            while(auxiliar):
                print(str(auxiliar.dado))
                auxiliar = auxiliar.proximo

                
    def remover(self):
        if self.vazio():                #verifica se está vazia
            print('Pilha vazia')
        else:
            auxiliar = self.primeiro.proximo            #Pega o ultimo valor inserido e exclui da lista
            self.primeiro = auxiliar
            self.tamanho -= 1                           #Pega o tamanho e diminui 1
        '''
            print("A pilha após exclusão: ")           #print da pilha após excluir, mesma funcao de imprimir
            imprimirpilha(self)
        '''
        
    

    