''' Incrementar as funções de Criar usuário e Vincular a conta'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

cores = {
    "limpar": "\033[0m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[36m",
}


def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
limpar()

while True:
    print('''===========================================\n         Bem-vindo ao Banco Python!\n===========================================''')

    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    # Depósito =================================================================================================================================================

    match opcao:
        case "1":
            valor = float(input("Digite o valor a ser depositado: "))
            limpar()
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: {cores['verde']}\tR$ {valor:.2f}{cores['limpar']}\n"
                print(f"Depósito de {cores['verde']}R$ {valor:.2f}{cores['limpar']} realizado com sucesso!")
            else:
                print(f"{cores['amarelo']}Valor inválido para depósito.{cores['limpar']}")

    # Saque ====================================================================================================================================================

        case "2":
            limpar()
            if numero_saques < LIMITE_SAQUES:
                valor = float(input("Digite o valor a ser sacado: "))
                if 0 < valor <= saldo and valor <= limite:
                    saldo -= valor
                    extrato += f"Saque: {cores['azul']}\t\t1R$ {valor:.2f}{cores['limpar']}\n"
                    numero_saques += 1
                    print(f"Saque de {cores['azul']}R$ {valor:.2f}{cores['limpar']} realizado com sucesso!")
                else:
                    print(f"{cores['amarelo']}Valor inválido para saque.{cores['limpar']}")
            else:
                print(f"{cores['amarelo']}Limite de saques diários atingido.{cores['limpar']}")

    # Extrato ==================================================================================================================================================

        case "3":
            limpar()
            print("Extrato ===========================\n")
            if extrato:
                print(extrato)
            else:
                print(f"{cores['amarelo']}Nenhuma transação realizada.{cores['limpar']}")
            print(f"Saldo atual: {cores['verde']}\tR$ {saldo:.2f}\n{cores['limpar']}")

    # Sair ====================================================================================================================================================

        case "4":
            print(f"{cores['verde']}\nObrigado por usar o Banco Python! Até logo!\n{cores['limpar']}")
            break

    # Opção inválida ===========================================================================================================================================

        case _:
            limpar()
            print(f"{cores['amarelo']}Opção inválida, tente novamente.{cores['limpar']}")