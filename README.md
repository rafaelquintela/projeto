Descrição Geral do Sistema
O sistema simula o funcionamento de uma loja que possui um estoque de itens (produtos) e permite que os clientes adicionem esses itens ao carrinho de compras, finalizem a compra e visualizem os produtos disponíveis no estoque. As funcionalidades são acessadas por meio de um menu interativo.

Funcionalidades do Sistema:
Cadastro de Usuários (Clientes): Permite registrar novos usuários com seus dados (nome e CPF).
Cadastro de Produtos (Itens): Permite adicionar novos produtos ao estoque da loja com nome, preço e quantidade.
Visualização de Produtos: Exibe a lista de itens disponíveis no estoque.
Adição de Produtos ao Carrinho: Clientes podem adicionar itens ao carrinho, respeitando a quantidade disponível em estoque.
Finalização de Compras: Realiza o cálculo total da compra e limpa o carrinho após a compra ser finalizada.
Gestão do Estoque: O estoque é atualizado sempre que um item é adicionado ao carrinho.

Melhorias no Código

A interação com o usuário foi organizada de forma mais intuitiva. Por exemplo, ao buscar por um item, agora é solicitado apenas o nome do item e, ao adicionar um item ao carrinho, a quantidade é solicitada de forma mais simples.
O sistema agora também verifica se a quantidade desejada do item está disponível em estoque antes de adicioná-lo ao carrinho, garantindo que o cliente não compre mais do que há disponível.

Nova opção no menu: A opção "Remover item do estoque" foi adicionada, sendo necessario apenas o cliente selecionar essa opção é o sistema ira mostrar todos os itens no estoque e qual e quantidade que ela quer remover

Conclusão
As melhorias realizadas visam tornar o código mais genérico, legível e modular, facilitando manutenções futuras e a expansão para diferentes tipos de lojas ou sistemas de vendas. 
As alterações aumentam a clareza da estrutura e garantem uma experiência de usuário mais robusta, com validações e interações bem definidas.
