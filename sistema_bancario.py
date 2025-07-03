menu  = """

============= MENU =============
[1] - EXTRATO
[2] - DEPÓSITO
[3] - SAQUE

[0] - SAIR
================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:

    opcao = input(menu)

    if opcao == "1":
        print(f"""
============= EXTRATO =============

{extrato if extrato else "Nenhuma movimentação"}           
SALDO: R$ {saldo:.2f}

===================================
""")
    
    elif opcao == "2":
        x = float(input("Informa o valor que deseja depositar: "))
        if x > 0:
            saldo += x
            extrato += f"Depósito:  +R$ {x:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para deposito.")
    
    elif opcao == "3":
        valor = float(input("Informe o valor do saque: "))
        if valor >= saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print("Valor do saque excede o limite por operação.")
        elif numero_saques > LIMITE_SAQUES:
            print("Número máximo de saques atingido")
        elif valor < 0:
            print("Valor inválido")
        else:
            saldo -= valor
            extrato += f"Saque:  -R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
    
    elif opcao == "0":
        print("Obrigado por utilizar nosso")
        break

    else:
        print("Operação iinválida, por favor selecione novamente a operação desejada.")