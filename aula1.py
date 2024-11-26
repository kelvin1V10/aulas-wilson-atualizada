# def funcao_1():
#     n1 = 20
#     n2 = 10
#     s = n1+n2
#     print("A soma e: ", s)

# def funcao_2(n1, n2):
#     s = n1+n2
#     print("A soma e: ", s)

# numero1 = 5
# numero = 10
# funcao_2(n1=numero1, n2=numero2)




class GerenciadorFinanceiro:
    class Conta:
        def __init__(self, tipo_conta):
            self.saldo = 0.0
            self.historico_transacoes = []
            self.tipo_conta = tipo_conta

        def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                self.historico_transacoes.append(f'Depósito: R${valor:.2f}')
                print(f'Depósito de R${valor:.2f} realizado na conta {self.tipo_conta}.')
            else:
                print("Valor de depósito deve ser positivo.")

        def sacar(self, valor):
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                self.historico_transacoes.append(f'Saque: R${valor:.2f}')
                print(f'Saque de R${valor:.2f} realizado na conta {self.tipo_conta}.')
            elif valor > self.saldo:
                print("Saldo insuficiente para o saque.")
            else:
                print("Valor de saque deve ser positivo.")

        def extrato(self):
            print(f"\n--- Extrato da Conta {self.tipo_conta} ---")
            for transacao in self.historico_transacoes:
                print(transacao)
            print(f'Saldo atual: R${self.saldo:.2f}')

    def __init__(self):
        self.contas = {}

    def criar_conta(self, id_conta, tipo_conta):
        if id_conta not in self.contas:
            self.contas[id_conta] = self.Conta(tipo_conta)
            print(f'Conta {id_conta} do tipo {tipo_conta} criada com sucesso.')
        else:
            print(f'A conta {id_conta} já existe.')

    def depositar(self, id_conta, valor):
        if id_conta in self.contas:
            self.contas[id_conta].depositar(valor)
        else:
            print(f'Conta {id_conta} não encontrada.')

    def sacar(self, id_conta, valor):
        if id_conta in self.contas:
            self.contas[id_conta].sacar(valor)
        else:
            print(f'Conta {id_conta} não encontrada.')

    def transferir(self, id_origem, id_destino, valor):
        if id_origem in self.contas and id_destino in self.contas:
            conta_origem = self.contas[id_origem]
            conta_destino = self.contas[id_destino]

            if valor > 0 and valor <= conta_origem.saldo:
                conta_origem.sacar(valor)
                conta_destino.depositar(valor)
                conta_origem.historico_transacoes.append(f'Transferido: R${valor:.2f} para a conta {id_destino}')
                conta_destino.historico_transacoes.append(f'Transferido: R${valor:.2f} da conta {id_origem}')
                print(f'Transferido R${valor:.2f} da conta {id_origem} para a conta {id_destino}.')
            else:
                print("Saldo insuficiente para a transferência.")
        else:
            print("Uma ou ambas as contas não foram encontradas.")

def main():
    gf = GerenciadorFinanceiro()

    while True:
        print("\nEscolha uma operação:")
        print("1 - Criar Conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Exibir Extrato")
        print("6 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '1':
            id_conta = input("Digite o ID da conta: ")
            tipo_conta = input("Digite o tipo da conta (Poupança/Corrente): ")
            gf.criar_conta(id_conta, tipo_conta)
        elif opcao == '2':
            id_conta = input("Digite o ID da conta para depósito: ")
            valor = float(input("Digite o valor a ser depositado: R$"))
            gf.depositar(id_conta, valor)
        elif opcao == '3':
            id_conta = input("Digite o ID da conta para saque: ")
            valor = float(input("Digite o valor a ser sacado: R$"))
            gf.sacar(id_conta, valor)
        elif opcao == '4':
            id_origem = input("Digite o ID da conta de origem: ")
            id_destino = input("Digite o ID da conta de destino: ")
            valor = float(input("Digite o valor a ser transferido: R$"))
            gf.transferir(id_origem, id_destino, valor)
        elif opcao == '5':
            id_conta = input("Digite o ID da conta para exibir o extrato: ")
            if id_conta in gf.contas:
                gf.contas[id_conta].extrato()
            else:
                print("Conta não encontrada.")
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()















