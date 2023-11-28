class ContaBancaria:
    def __init__(self, nome_cliente, saldo_inicial):
        self.nome_cliente = nome_cliente
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")


contas = {}


def criar_conta():
    nome_cliente = input("Digite o nome do cliente: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))

    conta = ContaBancaria(nome_cliente, saldo_inicial)
    numero_conta = len(contas) + 1
    contas[numero_conta] = conta

    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")


def acessar_conta():
    numero_conta = int(input("Digite o número da conta: "))

    conta = contas.get(numero_conta)

    if conta is None:
        print("Conta não encontrada. Verifique o número da conta e tente novamente.")
        return

    print(f"Bem-vindo, {conta.nome_cliente}!")

    while True:
        print("\nEscolha uma operação:")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Voltar ao menu principal")

        escolha = int(input())

        if escolha == 1:
            print(f"Saldo atual: {conta.saldo}")
        elif escolha == 2:
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.depositar(valor_deposito)
        elif escolha == 3:
            valor_saque = float(input("Digite o valor do saque: "))
            conta.sacar(valor_saque)
        elif escolha == 4:
            return
        else:
            print("Opção inválida. Tente novamente.")


while True:
    print("\nEscolha uma opção:")
    print("1. Criar conta")
    print("2. Acessar conta")
    print("3. Sair")

    escolha = int(input())

    if escolha == 1:
        criar_conta()
    elif escolha == 2:
        acessar_conta()
    elif escolha == 3:
        print("Saindo do simulador de banco. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
