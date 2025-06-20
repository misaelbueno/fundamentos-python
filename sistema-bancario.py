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
                extrato += f"Depósito: {valor}\n"
                resposta = input(f"Deseja fazer mais um depósito?[S/N]")
                if resposta.upper() != "S":
                    break

    elif opcao == "1":
        print("\nsaque")

    elif opcao == "2":
        print("EXTRATO")
        print(extrato)

    elif opcao == "3":
        break
  
    else:
        print("Opção inválida! Por favor digite a operação desejada.")
print('Saindo do Menu!')
        
        
