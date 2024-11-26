Este código implementa um sistema simples de gerenciamento de uma loja com funcionalidades para cadastro de usuários, controle de estoque, carrinho de compras, e finalização de compras. Aqui está um resumo do que ele faz:

### Classes:
1. **Item**: Representa um produto da loja, com atributos como nome, preço e estoque. Inclui métodos para reduzir o estoque quando o item é vendido e para exibir suas informações.
2. **Usuario**: Representa um cliente da loja, com atributos como nome, CPF e um carrinho de compras. Pode adicionar itens ao carrinho e visualizar sua cesta.
3. **Cesta**: Armazena os itens no carrinho de compras de um usuário. Permite adicionar itens ao carrinho, calcular o total da compra e exibir a lista de itens.
4. **Loja**: Gerencia o estoque da loja e os usuários. Permite adicionar/remover itens do estoque, buscar itens pelo nome, registrar novos usuários e realizar compras.
5. **Interface**: Contém métodos estáticos para exibir menus e solicitar entradas do usuário, facilitando a interação com o sistema.

### Funcionalidade:
- **Cadastro de usuários**: Permite registrar novos usuários com nome e CPF.
- **Gestão de estoque**: Permite adicionar novos itens ao estoque e remover itens existentes.
- **Carrinho de compras**: Os usuários podem adicionar itens ao seu carrinho, com verificação de estoque disponível.
- **Finalização de compra**: Após a escolha dos itens, o usuário pode concluir a compra, com o total sendo calculado e o carrinho sendo limpo após a compra.

### Menu interativo:
- O sistema oferece um menu com opções para cadastrar usuários, adicionar itens ao estoque, ver itens disponíveis, adicionar itens ao carrinho, concluir a compra, remover itens do estoque e sair do sistema.

Esse código é um exemplo simples de um sistema de loja, com funcionalidades básicas de controle de estoque e compras.
