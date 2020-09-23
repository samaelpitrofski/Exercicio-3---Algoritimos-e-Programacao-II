from Pilha import Pilha

Pilha = Pilha()
menu = '''
+--------------------+
|	    MENU         |		
|   1 - Adicionar    |
|   2 - Remover      |
|   3 - Imprmir      |     
|   4 - Sair         |
+--------------------+
Escolha: '''

while True:
    escolha = (input(menu))

    if escolha == '1':
       	Pilha.adicionar(input('Digite um valor: '))
    elif escolha == '2':
        Pilha.remover()   
    elif escolha == '3':
        Pilha.imprimirpilha()
    elif escolha == '4':
        print("Obrigado por utilizar o Sistema. ")
        break    
    else:
        print('Opção Inexistente')