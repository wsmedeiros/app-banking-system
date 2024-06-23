'''
Desafio 01 - Sistema Bancário
Objetivo: Desenvolver um sistema bancário com as operações:\
sacar, depositar e visualizar extrato.

Requisitos:
    Depósito:
        + apenas valores positivos.
    Saque: 
        + máximo 3 saques diários;
        + limite máximo de R$500,00/saque;
        + se não houver saldo exibir mensagem;
    Extrato:
        + listar todas as operações de saque e depósito;
        + exibir no final do extrato o saldo atual da conta;
        + exibir os valores no formato 'R$ 000.00'.
'''

menu = """
[d] Depoistar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print("Depósito")
        deposito = float(input("Valor: R$ "))
        if deposito > 0:
            extrato += f"\n+ R$ {deposito:.2f}"
            saldo += deposito
        else:
            print("Valor inválido, insira valor superior a 'R$ 0.00'.")
            continue

    elif opcao == 's':
        print("Sacar")
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques diário excedido!")
            continue
        else:
            saque = float(input("Valor: R$ "))
            if (saque > 0 and saque <= 500):
                if saque <= saldo:
                    extrato += f"\n- R$ {saque:.2f}"
                    saldo -= saque
                    numero_saques += 1
                else:
                    print("Saldo insuficiente!")
                    continue
            else:
                print("Valor inválido, insira valor entre 'R$0.01' a 'R$ 500.00'.")
                continue

    elif opcao == 'e':
        print("Extrato")
        print(extrato)
        print("-----------------")
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")