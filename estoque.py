estoque = {
   "camisa" : 50,
   "calça" : 15,
   "boné": 25,
   "tênis naik" : 30
    }
# mostrar o estoque rsrs
print("estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} : {quantidade}")
    # pedir dados pro user
    nome_produto = input("\nInforme o nome do produto vendido: ")
    quantidade_vendida = int(input("\nInforme a quantidade vendida: "))
    #atualizar estoque
    if nome_produto in estoque:
        if quantidade_vendida <= estoque[nome_produto]:
         estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
         print("Venda realizada com sucesso :D")
    else:
        print("Produto não encontrado")