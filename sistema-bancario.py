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
                print(f"Depósito no valor de {valor:.2f} reais confirmado!")
                extrato += f"Depósito: R${valor}.00\n"
                depTotal += valor
                resposta = input(f"Deseja fazer mais um depósito?[S/N]")
                if resposta.upper() != "S":
                    break

    elif opcao == "1":
        print("\nsaque")

    elif opcao == "2":
        print("EXTRATO")
        print(extrato)
        print(f"Saldo: {depTotal - saqueTotal}")

    elif opcao == "3":
        break
  
    else:
        print("Opção inválida! Por favor digite a operação desejada.")
print('Saindo do Menu!')
        
        
