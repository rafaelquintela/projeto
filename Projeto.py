class Item:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade_vendida):
        self.estoque -= quantidade_vendida

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} - {self.estoque} unidades disponíveis"


class Usuario:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento
        self.carrinho = Cesta()

    def adicionar_item(self, item, quantidade):
        self.carrinho.incluir_item(item, quantidade)

    def visualizar_cesta(self):
        return self.carrinho

    def __str__(self):
        return f"{self.nome} - CPF: {self.documento}"


class Cesta:
    def __init__(self):
        self.itens = []

    def incluir_item(self, item, quantidade):
        if item.estoque >= quantidade:
            item.reduzir_estoque(quantidade)
            self.itens.append((item, quantidade))
        else:
            print(f"Estoque insuficiente de {item.nome}. Disponível: {item.estoque}")

    def calcular_total(self):
        total = sum(item.preco * quantidade for item, quantidade in self.itens)
        return total

    def __str__(self):
        detalhes = "\n".join([f"{item.nome} - {quantidade} unidade(s) - R${item.preco * quantidade:.2f}" for item, quantidade in self.itens])
        total = self.calcular_total()
        return f"Cesta de compras:\n{detalhes}\nTotal: R${total:.2f}"


class Loja:
    def __init__(self):
        self.itens = []
        self.usuarios = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def buscar_item(self, nome):
        for item in self.itens:
            if item.nome.lower() == nome.lower():
                return item
        return None

    def remover_item(self, indice):
        if 0 <= indice < len(self.itens):
            item = self.itens.pop(indice)
            print(f"Item {item.nome} removido do estoque.")
        else:
            print("Índice inválido! Nenhum item removido.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_compra(self, usuario):
        total = usuario.carrinho.calcular_total()
        print(f"\n{usuario.nome}, o total da sua compra é R${total:.2f}")
        print("Agradecemos pela sua compra!")
        usuario.carrinho = Cesta()  # Limpa a cesta após a compra

    def listar_itens(self):
        if not self.itens:
            print("Não há itens no estoque.")
        else:
            for i, item in enumerate(self.itens):
                print(f"{i+1} - {item}")  # Exibe índice junto com a descrição do item


class Interface:
    @staticmethod
    def exibir_menu_principal():
        print("\nMENU DE OPÇÕES")
        print("1 - Cadastrar novo usuário")
        print("2 - Adicionar item ao estoque")
        print("3 - Ver itens no estoque")
        print("4 - Adicionar item à cesta")
        print("5 - Concluir compra")
        print("6 - Remover item do estoque")  # Nova opção
        print("7 - Sair")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def solicitar_nome_item():
        return input("Informe o nome do item: ")

    @staticmethod
    def solicitar_dados_usuario():
        nome = input("Informe o nome do usuário: ")
        documento = input("Informe o CPF do usuário: ")
        return nome, documento

    @staticmethod
    def solicitar_quantidade():
        return int(input("Quantas unidades deseja adicionar? "))

    @staticmethod
    def solicitar_indice_item():
        return int(input("Informe o número do item que deseja remover: ")) - 1  # Subtraímos 1 para ajustar o índice


def executar():
    loja = Loja()

    while True:
        opcao = Interface.exibir_menu_principal()

        if opcao == 1:
            nome_usuario, documento_usuario = Interface.solicitar_dados_usuario()
            usuario = Usuario(nome_usuario, documento_usuario)
            loja.registrar_usuario(usuario)
            print(f"Usuário {nome_usuario} registrado com sucesso!")

        elif opcao == 2:
            nome_item = input("Informe o nome do item: ")
            preco_item = float(input("Informe o preço do item: R$"))
            estoque_item = int(input("Informe a quantidade do item no estoque: "))
            item = Item(nome_item, preco_item, estoque_item)
            loja.adicionar_item(item)
            print(f"Item {nome_item} adicionado ao estoque!")

        elif opcao == 3:
            print("\nItens disponíveis no estoque:")
            loja.listar_itens()

        elif opcao == 4:
            nome_item = Interface.solicitar_nome_item()
            item = loja.buscar_item(nome_item)

            if item:
                quantidade = Interface.solicitar_quantidade()
                if quantidade <= item.estoque:
                    nome_usuario = input("Informe o nome do usuário para adicionar ao carrinho: ")
                    usuario = next((u for u in loja.usuarios if u.nome == nome_usuario), None)
                    if usuario:
                        usuario.adicionar_item(item, quantidade)
                        print(f"{quantidade} unidade(s) de {item.nome} adicionada(s) ao carrinho de {nome_usuario}.")
                    else:
                        print("Usuário não encontrado!")
                else:
                    print(f"Estoque insuficiente! Temos apenas {item.estoque} unidades.")
            else:
                print("Item não encontrado!")

        elif opcao == 5:
            nome_usuario = input("Informe o nome do usuário para finalizar a compra: ")
            usuario = next((u for u in loja.usuarios if u.nome == nome_usuario), None)

            if usuario:
                loja.realizar_compra(usuario)
            else:
                print("Usuário não encontrado!")

        elif opcao == 6:  # Remover item do estoque
            print("\nItens no estoque:")
            loja.listar_itens()
            indice = Interface.solicitar_indice_item()
            loja.remover_item(indice)

        elif opcao == 7:
            print("Saindo... Até logo!")
            break


if __name__ == "__main__":
    executar()



