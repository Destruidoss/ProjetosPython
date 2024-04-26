menu = """
============================================
|           BANCO PYTHONIC           |
============================================
| [d] Depositar                          |
| [s] Sacar                              |
| [e] Extrato                            |
| [q] Sair                               |
============================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Você não possui saldo suficiente para este saque.")
        elif valor > limite:
            print("O valor do saque excede o limite de R$500 permitido por saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de 3 saques por dia.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n================================ Extrato =================================")
        if extrato:
            print(extrato)
        else:
            print("  _____")
            print(" /     \\")
            print("| () () |")
            print(" \\  ^  /")
            print("  |||||")
            print("  |||||")
        print("==========================================================================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços. Até logo!")
        break

    else:
        print("Opção inválida, por favor selecione novamente.")
