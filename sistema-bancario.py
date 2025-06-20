menu = """
=== Menu ===

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
depTotal, saqueTotal = 0, 0

while True:
    opcao = input(menu)

    if opcao == "0":
        while True:
            valor = int(input("*Voltar ao menu inicial, digite 0\nValor do depósito:\n"))

            if valor == 0:
                break
            elif not isinstance(valor, int) or valor < 0:
                print("Valor Inválido!")
            else:
                extrato += f"Depósito: R${valor}.00\n"
                depTotal += valor
                saldo = depTotal - saqueTotal
                print(f"Depósito no valor de R${valor:.2f} confirmado!")
                resposta = input(f"Deseja fazer mais um depósito?[S/N]")
                if resposta.upper() != "S":
                    break

    elif opcao == "1":
        while True:
            saque = int(input("*Voltar ao menu inicial, digite 0\nValor do saque:\n"))
            numero_saques += 1
            if numero_saques > 3:
                print('Valor ultrapassado de limite de saque diário! Tente novamente amanhã!')
                break
            elif saque > saldo:
                print('Saldo Insuficiente!')
            else:
                extrato += f"Saque: R${saque}.00\n"
                saqueTotal += saque
                saldo = depTotal - saqueTotal
                print(f"Saque no valor de R${saque:.2f} confirmado!")
                resposta = input(f"Deseja fazer mais um saque?[S/N]")
                if resposta.upper() != "S":
                    break

    elif opcao == "2":
        print("EXTRATO")
        print(extrato)
        print(f"Saldo: {saldo}")

    elif opcao == "3":
        break
  
    else:
        print("Opção inválida! Por favor digite a operação desejada.")
print('Saindo do Menu!')
        
        
