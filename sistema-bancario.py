saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
usuarios = []


def menu():
    menu = """
    === Menu ===
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair

    => """
    return menu


def depositar(extrato, saldo, /):
    # ARGUMENTOS SOMENTE POR POSIÇÃO
    while True:
        prompt_deposito = (
            "*Voltar ao menu inicial, digite 0\n"
            "Valor do depósito:\n"
        )
        valor = int(input(prompt_deposito))

        if valor == 0:
            break
        elif not isinstance(valor, int) or valor < 0:
            print("Valor Inválido!")
        else:
            extrato += f"Depósito: R${valor}.00\n"
            saldo += valor
            print(f"Depósito no valor de R${valor:.2f} confirmado!")
            resposta = input("Deseja fazer mais um depósito?[S/N]")
            if resposta.upper() != "S":
                break
    return extrato, saldo


def sacar(*, extrato, saldo, numero_saques, limite, limite_saque):
    # ARGUMENTOS SOMENTE NOMEADOS
    while True:
        saque = int(input(
            "*Voltar ao menu inicial, digite 0\n"
            "Valor do saque:\n"
        ))

        if saque == 0:
            break
        elif numero_saques > limite_saque:
            print(
                'Valor ultrapassado de limite de saque diário! '
                'Tente novamente amanhã!'
            )
            break
        elif saque > saldo:
            print('Saldo Insuficiente!')
        elif saque > limite:
            print('Valor de saque maior que o limite!')
        elif saque > 0:
            numero_saques += 1
            extrato += f"Saque: R${saque}.00\n"
            saldo -= saque
            print(f"Saque no valor de R${saque:.2f} confirmado!")
            resposta = input("Deseja fazer mais um saque?[S/N]")
            if resposta.upper() != "S":
                break
        else:
            print('Valor inválido!')
    return extrato, saldo


def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO")
    print(extrato)
    print(f"Saldo: R${saldo:.2f}")


while True:
    opcao = input(menu())

    if opcao == "0":
        extrato, saldo = depositar(extrato, saldo)

    elif opcao == "1":
        extrato, saldo = sacar(
            extrato=extrato,
            saldo=saldo,
            numero_saques=numero_saques,
            limite=limite,
            limite_saque=LIMITE_SAQUE
        )
    elif opcao == "2":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "3":
        break

    else:
        print("Opção inválida! Por favor digite a operação desejada.")
print('Saindo do Menu!')

'''
def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    depTotal, saqueTotal = 0, 0

'''
