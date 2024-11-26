
Aluno: Rafael Soares Quintela

Documentação do Sistema de Loja Virtual

Visão Geral
Este sistema simula o gerenciamento de uma loja virtual, permitindo que usuários se cadastrem, adicionem itens ao estoque, gerenciem suas cestas de compras e realizem compras. Além disso, o sistema permite que os administradores vejam o saldo do caixa e o histórico de compras feitas pelos usuários.



O sistema foi dividido em classes que representam diferentes entidades e funcionalidades:
Item: Representa um produto no estoque.
Usuario: Representa um usuário da loja que pode adicionar itens à sua cesta e realizar compras.

Cesta: Representa o carrinho de compras de um usuário.
Loja: Representa a loja em si, contendo os itens em estoque, usuários registrados e o histórico de compras.
Interface: Responsável pela interação com o usuário, exibindo menus e solicitando entradas.

Estrutura de Classes
1. Classe Item
A classe Item representa um produto no estoque da loja.

Atributos:
nome: O nome do item (string).
preco: O preço do item (float).
estoque: A quantidade disponível no estoque (inteiro).
Métodos:
reduzir_estoque(quantidade_vendida): Reduz o estoque do item de acordo com a quantidade vendida.
__str__(): Retorna uma string com informações sobre o item, como nome, preço e quantidade disponível.

2. Classe Usuario
A classe Usuario representa um usuário registrado na loja.
Atributos:
nome: Nome do usuário (string).
documento: Documento de identificação do usuário (string, CPF).
carrinho: Um objeto da classe Cesta que contém os itens que o usuário deseja comprar.
Métodos:
adicionar_item(item, quantidade): Adiciona um item ao carrinho de compras do usuário.
visualizar_cesta(): Exibe o conteúdo atual da cesta do usuário.
__str__(): Retorna uma string com o nome e o CPF do usuário.

3. Classe Cesta
A classe Cesta representa o carrinho de compras de um usuário.
Atributos:
itens: Lista de tuplas, onde cada tupla contém um item e a quantidade comprada desse item.
Métodos:
incluir_item(item, quantidade): Adiciona um item à cesta, se houver estoque suficiente.
calcular_total(): Calcula o total da compra, multiplicando o preço de cada item pela quantidade comprada e somando os valores.
__str__(): Retorna uma string com os detalhes de todos os itens da cesta, incluindo o total da compra.

4. Classe Loja
A classe Loja representa a loja e gerencia os itens em estoque, usuários registrados e o histórico de compras.
Atributos:
itens: Lista de itens no estoque da loja (objetos da classe Item).
usuarios: Lista de usuários registrados na loja (objetos da classe Usuario).
historico_compras: Lista que armazena o histórico de compras, incluindo o usuário e a cesta comprada.
saldo_caixa: Valor total das compras realizadas, representando o saldo do caixa da loja.
Métodos:
adicionar_item(item): Adiciona um item ao estoque.
buscar_item(nome): Retorna um item específico, procurando pelo nome.
remover_item(indice): Remove um item do estoque com base no índice informado.
registrar_usuario(usuario): Registra um usuário na loja.
realizar_compra(usuario): Finaliza a compra de um usuário, somando o valor total da compra ao saldo do caixa e armazenando o histórico.
listar_itens(): Exibe todos os itens disponíveis no estoque.
listar_compras(): Exibe o histórico de compras feitas na loja.
ver_saldo_caixa(): Exibe o saldo atual do caixa da loja.

5. Classe Interface
A classe Interface é responsável pela interação com o usuário por meio de menus e entrada de dados.
Métodos:
exibir_menu_principal(): Exibe o menu principal com as opções disponíveis para o usuário.
solicitar_nome_item(): Solicita o nome de um item.
solicitar_dados_usuario(): Solicita o nome e CPF de um novo usuário.
solicitar_quantidade(): Solicita a quantidade de unidades de um item que o usuário deseja adicionar ao carrinho.
solicitar_indice_item(): Solicita o índice de um item para remoção do estoque.

Fluxo de Execução
O fluxo do programa é controlado pela função executar(), que exibe o menu principal e permite que o usuário escolha uma ação. 

As principais funcionalidades incluem:
Cadastrar novo usuário: Permite registrar um usuário na loja.
Adicionar item ao estoque: Permite adicionar novos itens ao estoque da loja.
Ver itens no estoque: Exibe todos os itens disponíveis no estoque.
Adicionar item à cesta: Permite que um usuário adicione um item ao seu carrinho de compras.
Concluir compra: Finaliza a compra de um usuário, subtraindo o total do caixa e limpando a cesta.
Remover item do estoque: Permite que o administrador remova um item do estoque.
Ver histórico de compras: Exibe o histórico de compras realizadas, mostrando os itens comprados e os usuários.
Ver saldo do caixa: Exibe o saldo atual do caixa da loja.

Exemplo de Uso
Cadastrar usuário:
O sistema solicita o nome e CPF do usuário e o registra.

Adicionar item ao estoque:
O administrador adiciona um novo item, informando nome, preço e quantidade no estoque.

Adicionar item à cesta:
Um usuário pode buscar um item e adicionar ao seu carrinho, especificando a quantidade desejada.

Concluir compra:
O usuário finaliza a compra e o sistema calcula o total da compra, atualiza o saldo do caixa e limpa a cesta.

Ver histórico de compras e saldo do caixa:
O administrador pode consultar o histórico de compras realizadas e o saldo atual do caixa da loja.
Observações
O programa depende de entradas do usuário via console, o que exige que o programa seja executado em um ambiente interativo.
O código pode ser expandido para incluir mais funcionalidades, como a modificação de preços de itens, descontos, ou relatórios mais detalhados.

Caso seja necessário adicionar um sistema de persistência (salvar dados em arquivos ou banco de dados), o código pode ser estendido para incluir essa funcionalidade.
