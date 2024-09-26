import os
os.system('cls')

# Criando a conta do Usuário

class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

# Opção para verificar o saldo do Usuário (extrato)

    def verificar_saldo(self):
        return self.saldo

# Depósito

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso. Volte Sempre!')
        else:
            print('O valor do depósito deve ser positivo.')

# Saque

    def sacar(self, valor):
        if valor <= 0:
            print('O valor do saque deve ser positivo.')
        elif valor > self.saldo:
            print('Saldo insuficiente para realizar o saque.')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso. Volte Sempre!')

class CaixaEletronico:
    def __init__(self):
        self.contas = {}

# Criar Conta

    def criar_conta(self, numero, titular):
        if numero not in self.contas:
            self.contas[numero] = Conta(numero, titular)
            print(f'Uma Conta foi criada com sucesso para {titular}!')
        else:
            print('O Número da conta já existe.')

# Acessar Conta

    def acessar_conta(self, numero):
        return self.contas.get(numero, None)

def main():
    caixa = CaixaEletronico()
    caixa.criar_conta('12345', 'Eric Wallis')

    conta = caixa.acessar_conta('12345')

    if conta:
        while True:
            print("\nBem-vindo ao Wallis Bank!")
            print("\nDigite 1 para Verificar seu Saldo")
            print("Digite 2 para Depositar")
            print("Digite 3 para Sacar")
            print("Digite 4 para Sair")
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                saldo = conta.verificar_saldo()
                print(f'Seu saldo é de: R${saldo:.2f}')
            elif opcao == '2':
                valor = float(input("Digite o valor que irá depositar: "))
                conta.depositar(valor)
            elif opcao == '3':
                valor = float(input("Digite o valor que irá sacar: "))
                conta.sacar(valor)
            elif opcao == '4':
                print('Obrigado por usar o Wallis Bank. Volte Sempre!')
                break
            else:
                print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()