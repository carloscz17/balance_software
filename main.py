def exportacaoTxt(listaProduto):
    with open("CADTXT.txt", "w") as arquivo: #função e renomeando para arquivo
        for produto in listaProduto: #montagem do txt com produtos da lista
            produto_line = f"{produto['codigo']:06d}{produto['tipo']}{produto['descricao'][:22].ljust(22)}{produto['preco']:07}000"
            arquivo.write(produto_line + '\n') #criando arquivo do produto
def main():
    listaProduto = [] #lista

    while True:
        print("============= Mercado FCPB =============")
        codigo = int(input("Código do produto -> "))
        tipo = input("Qual tipo do produto? P(PREÇO) | U(UNIDADE) -> ")

        if tipo not in ['P', 'U']:
            print("Tipo de produto inválido!")
            break

        descricao = input("Descrição do produto -> ")
        preco = float(input("Preço do produto -> "))

        produto = {
            "codigo": codigo,
            "tipo": tipo,
            "descricao": descricao,
            "preco": int(preco * 100) #conversão
        }

        print("===========================")
        print("Código -> ", codigo)
        print("Tipo -> " + tipo)
        print("Descrição -> "+ descricao)
        print("Preço ->", preco)
        print("Produto adicionado ao carrinho com sucesso!\n===========================")

        listaProduto.append(produto) #adicionando item na lista

        prosseguirComprando = input("Adicionamos seu item ao carrinho, deseja continuar comprando? S ou N -> ").upper()
        if prosseguirComprando != 'S':
            break
    exportacaoTxt(listaProduto) #fora do while, para quando terminar de fazer a adição dos itens criar o arquivo txt com os itens adicionados.
    print("===========================")
    print("Arquivo CADTXT.txt criado com sucesso, todos seus itens estão adicionados.")
    print("Volte sempre!")
    print("===========================")

main()