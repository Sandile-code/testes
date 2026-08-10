class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def __str__(self):
        return f"{self.nome} - R${self.preco} Qtd:{self.quantidade}"

    def __eq__(self, outro):
        return self.codigo == outro.codigo

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def __len__(self):
        return len(self.produtos)

    def __getitem__(self, key):
        return self.produtos[key]

    def __str__(self):
        return "\n".join(str(produto)for produto in self.produtos)

    def __add__(self, other):
        novo_carrinho = Carrinho()
        novo_carrinho.produtos = self.produtos + other.produtos
        return novo_carrinho

class Dinheiro:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return Dinheiro(self.valor + other.valor)