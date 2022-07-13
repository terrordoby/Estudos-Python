# Mini Sistema de Controle de Estoque

alimentos = 50    ### estoque mínimo 
bebidas = 75      ### estoque mínimo 
limpeza = 30      ### estoque mínimo 


## Verificar se no final do expediente temos a quantidade mínima de estoque !! 

produto = input('Digite o nome do produto ')
categoria = input('Digite a categoria do produto ')
quantidadeAtual = input('Digite o estoque atual do produto ')

if produto and categoria and quantidadeAtual:

    if (categoria == 'alimentos' and int(quantidadeAtual) < alimentos):
        print('Solicitar {} à equipe de compras, temos apenas {} em estoque'.format(produto, alimentos))
    elif (categoria == 'bebidas' and int(quantidadeAtual) < bebidas):
        print('Solicitar {} à equipe de compras, temos apenas {} em estoque'.format(produto, bebidas))
    elif (categoria == 'limpeza' and int(quantidadeAtual) < limpeza):
        print('Solicitar {} à equipe de compras, temos apenas {} em estoque'.format(produto, limpeza))

else:
    print('Preencha todas as informações')






