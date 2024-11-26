# class CarrinhoDeCompras:
#     def __init__(self):
#         self.itens = {}
#         self.total = 0.0

#     def adicionar_item(self, nome, preco, quantidade):
#         if nome in self.itens:
#             self.itens[nome]['quantidade'] += quantidade
#         else:
#             self.itens[nome] = {'preco': preco, 'quantidade': quantidade}
        
#         self.total += preco * quantidade
#         print(f"{quantidade}x {nome}(s) adicionado(s) ao carrinho. Total: R${self.total:.2f}")

#     def remover_item(self, nome, quantidade):
#         if nome in self.itens:
#             if quantidade >= self.itens[nome]['quantidade']:
#                 quantidade_removida = self.itens[nome]['quantidade']
#                 self.total -= self.itens[nome]['preco'] * quantidade_removida
#                 del self.itens[nome]
#                 print(f"{quantidade_removida}x {nome}(s) removido(s) do carrinho.")
#             else:
#                 self.itens[nome]['quantidade'] -= quantidade
#                 self.total -= self.itens[nome]['preco'] * quantidade
#                 print(f"{quantidade}x {nome}(s) removido(s) do carrinho. Total: R${self.total:.2f}")
#         else:
#             print(f"Item {nome} não está no carrinho.")

#     def ver_saldo(self):
#         print("\nCarrinho de Compras:")
#         for item, detalhes in self.itens.items():
#             print(f"{detalhes['quantidade']}x {item} - R${detalhes['preco']:.2f} cada")
#         print(f"Total a pagar: R${self.total:.2f}\n")

#     def finalizar_compra(self):
#         if self.total > 0:
#             print(f"Compra finalizada! Total: R${self.total:.2f}")
#             self.itens.clear()
#             self.total = 0.0
#         else:
#             print("Carrinho vazio. Nenhuma compra a ser finalizada.")
    
#     def sair(self):
#         print("Saindo do sistema... Obrigado por usar o sistema de compras!")


# def menu():
#     carrinho = CarrinhoDeCompras()
#     while True:
#         print("\n--- Menu Carrinho de Compras ---")
#         print("1. Adicionar item ao carrinho")
#         print("2. Remover item do carrinho")
#         print("3. Ver saldo do carrinho")
#         print("4. Finalizar compra")
#         print("5. Sair")
        
#         escolha = input("Escolha uma opção: ")
        
#         if escolha == "1":
#             nome = input("Nome do item: ")
#             preco = float(input("Preço do item: R$"))
#             quantidade = int(input("Quantidade: "))
#             carrinho.adicionar_item(nome, preco, quantidade)
        
#         elif escolha == "2":
#             nome = input("Nome do item a remover: ")
#             quantidade = int(input("Quantidade a remover: "))
#             carrinho.remover_item(nome, quantidade)
        
#         elif escolha == "3":
#             carrinho.ver_saldo()
        
#         elif escolha == "4":
#             carrinho.finalizar_compra()
        
#         elif escolha == "5":
#             carrinho.sair()
#             break
        
#         else:
#             print("Opção inválida! Tente novamente.")

# # Iniciar o sistema de carrinho
# menu()
