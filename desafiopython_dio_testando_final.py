menu = '''

[d] Deposito
[s] Saque
[e] extrato
[q] Sair

'''

saldo = 0
limite = 500
LIMITE_SAQUE = 500
extrato = ""
numero_saque = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Nenhum valor foi digitado")

    elif opcao == "s":
        valor = float(input("Informe o valor para saque:"))
        if  valor > saldo and valor > limite and valor > LIMITE_SAQUE and numero_saque > 3:
            print("verifique seu saldo no extrato e retorne na operação de saque para fazer o saque corretamente")
        elif valor < 0:
            print("Não permite valor negativos")

        else:
            print("Operação falhou! tente novamente")

    elif opcao == "e":
        print("=====================EXTRATO BANCARIO====================")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        
    elif opcao == "q":
        break

    else:
        print("operacao invalida, por favor selecione novamente a operação desejada!")