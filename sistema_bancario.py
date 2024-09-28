import textwrap
  
def main() :
    
    saldo = 0
    numeros_saques=0
    extrato = ''
    usuarios = []
    contas = []
    LIMITE=500
    LIMITE_SAQUES=50
    AGENCIA="0001"

    while True:

        opcao = menu()

        if opcao.upper() == 'D':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao.upper() == 'S':
            valor = float(input("Informe o valor de saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numeros_saques=numeros_saques, limite_saques=LIMITE_SAQUES)
        elif opcao.upper() == 'E':
            historico(saldo, extrato=extrato)
        elif opcao.upper() == 'NU':
            criar_cliente(usuarios)
        elif opcao.upper() == 'LU':
            listar_cliente(usuarios)
        elif opcao.upper() == "NC":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas, LIMITE, LIMITE_SAQUES)
        elif opcao.upper() == "LC":
            listar_contas(contas)
        elif opcao.upper() == 'X':
            break
        else :
            print('Opção inválida')    
def menu():

    menu = '''

      [d] Depositar
      [s] Sacar
      [e] Extrato
      [nu] Novo usuário
      [lu] Listar usuário
      [nc] Nova conta
      [lc] Listar conta
      [x] Sair

    ==> '''
    return input(textwrap.dedent(menu))
def filtrar_cliente(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print("\n### Depósito realizado com sucesso! ###")
    else :
        print("\n### Valor inválido! ###")
    
    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques > limite_saques

    if excedeu_saldo:
        print("\n### Saldo insuficiente! ###")
    elif excedeu_limite :
        print("\n### Limite de saque excedido! ###")
    elif excedeu_saques:
        print("\n### Limite de saques excedido! ###")
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:   \tR$ {valor:.2f}\n'
        numeros_saques += 1
        print("\n### Saque realizado com sucesso! ###")
    else :
        print("\n### Valor inválido! ###")
    
    return saldo, extrato
def historico(saldo, /, *, extrato):
    
    print("\n================== EXTRATO ==================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f'\nSaldo:   \tR$ {saldo:.2f}' if extrato else '')
    print("==============================================")
def criar_cliente(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, usuarios)

    if cliente:
        print("\n### Já existe cliente com esse CPF! ###")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Cliente criado com sucesso! ===")
def listar_cliente(usuarios):
    if len(usuarios) > 0 :
        print('\n############## Listagem de Clientes ##############\n')
        for usuario in usuarios: 
            print(f'CPF: \t\t\t{usuario['cpf']}')
            print(f'Nome: \t\t\t{usuario['nome']}')
            print(f'Data nascimento: \t{usuario['data_nascimento']}')
            print(f'Endereço: \t\t{usuario['endereco']}')
            print('\n----------------------------------------------------\n')      

        print('################ Fim da listagem #################')
    else:
        print('Nenhum cliente encontrado')
def criar_conta(agencia,numero_conta, usuarios, contas, limite, limite_saques):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\n### Cliente não encontrado, fluxo de criação de conta encerrado! ###")
        return

    contas.append({"usuarios": usuarios, "agencia": agencia,  "numero_conta": numero_conta, "limite": limite, "limite_saques": limite_saques})
        
    print("\n=== Conta criada com sucesso! ===")
def listar_contas(contas):
    print("=" * 90)
    if len(contas) > 0 :
        for conta in contas:
            for indice in conta:
                if indice == 'usuarios' :
                    for usuario in conta[indice] :
                        print(f"CPF:      \t\t{usuario['cpf']}")
                        print(f"Nome:     \t\t{usuario['nome']}")
                elif indice == 'agencia' :
                    print(f'Agencia: \t\t{conta[indice]}')    
                elif indice == 'numero_conta' :
                    print(f'Número da Conta: \t{conta[indice]}')    
                elif indice == 'limite' :
                    print(f'Limite:      \t\t{conta[indice]}')    
                elif indice == 'limite_saques' :
                    print(f'Limite de Saque:  \t{conta[indice]}')    
                
            print('----------------------------------------------------\n')      
    else: 
        print('Nenhuma conta cadastrada')

main()
