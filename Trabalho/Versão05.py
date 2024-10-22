import sys # foi usado para o código sys.exit(0).

class Cliente:
    def __init__(self, nome, cpf, conta):
        self.nome = nome
        self.cpf = cpf
        self.contas = [conta]

    def exibir_informacoes_cliente(self):
        ''' 
            Função: Esse processo exibi informações de um cliente.
        '''
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        if self.contas:
            for conta in self.contas: 
                conta.exibir_informacoes_conta()
        else:
            print('Este cliente não possui contas.')

    @staticmethod # Permite a função ser autonoma mesmo estando na classe
    def criar_cliente():
        ''' 
            Função: Esse processo cria um cliente.  
        '''
        nome = input('Digite seu nome:').upper()
        teste = False
        while teste == False:
            cpf = input('Digite o Seu Cpf:')
            teste = validar_cpf(cpf)
        contasx = Conta.criar_conta()
        print(contasx)
        print(contasx[0])
        contasprincipal['numero'].append(contasx[0])
        contasprincipal['saldo'].append(contasx[1])
        contasprincipal['tipo'].append(contasx[2])
        
        cliente = Cliente(nome, cpf, contasx[0])
        cliente.exibir_informacoes_cliente()
        return cliente

class Conta:
    contador_conta = 1

    def __init__(self, numeroConta, saldo, tipoConta):
        self.numero = numeroConta
        self.saldo = saldo
        self.tipoConta = tipoConta

    def exibir_informacoes_conta(self):
        ''' 
            Função: 
            -
            Explicação: 
            -
            Comentários:
        '''
        print(f"\nConta Numero: {self.numero}")
        print(f"Saldo:  R$ {self.saldo:,.2f}")
        print(f"Tipo de Conta: {self.tipoConta}")

    @staticmethod # Permite a função ser autonoma mesmo estando na classe
    def criar_conta():
        ''' 
            Função: 
            -
            Explicação: 
            -
            Comentários:
        '''
        continuar = True
        while continuar:
            tipoConta = int(input('Qual o tipo da conta que deseja criar? \n1-Conta Corrente \n2-Conta Poupança\n'))
            if tipoConta == 1:
                tipoConta2 = 'Conta Corrente'
                continuar = False
            elif tipoConta == 2:
                tipoConta2 = 'Conta Poupança'
                continuar = False
            else:
                print('Tipo de conta inválido!')

        numeroConta = Conta.contador_conta
        Conta.contador_conta += 1
        contacriaconta = (numeroConta, 0, tipoConta2)
        return contacriaconta



def inicio():
    ''' 
        Função: Esse processo é responsável para proporcionar uma breve introdução para o usuário.
        -
        Explicação: Exibe no terminal menssagens(Boas Vindas ao Usuário) através de prints.
    '''
    print('+++++++++#######+++++++++')
    print('+++++++ BEM VINDO +++++++')
    print('++++++++++ AO +++++++++++')
    print('+++++++++ BANCO +++++++++')
    print('+++++++++#######+++++++++')
def validar_cpf(cpf):    # Verifica se o CPF é valido
    if len(cpf) != 11:
        return False
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"
def criacliente():
    clientedef = Cliente.criar_cliente()
    clientes["name"].append(clientedef.nome)
    clientes["cpf"].append(clientedef.cpf)
    clientes["numerodaconta"].append(clientedef.contas)
    return 
def criaconta(clientedef):
    numerodoclientedef = -1
    valido = False
    while valido == False:
        cpfdef = input('digite o cpf do cliente')
        valido = validar_cpf(cpfdef)
        if valido == False:
            print('digite um cpf valido')
    for i in range(len(clientedef['cpf'])):
        if cpfdef == clientedef['cpf'][i]:
            numerodoclientedef = i
    if numerodoclientedef == -1:
        while True:
            a = int(input("cpf não encontrado, deseja criar um cliente??\n 1 - sim\n 2 - não"))
            if a == 1: 
                criacliente()
                return
            elif a == 2:
                return
            else:
                print('digite uma opção valida')
            
    Conta.criar_conta(numerodoclientedef)
    
        
    
clientes = {"name":[],"cpf":[],"numerodaconta":[]} # Dicionario onde são armazenados todos clientes.
contasprincipal = {"numero":[0],"saldo":[0],"tipo":[0]}
while True:
    inicio()
    try: #Função: While responsável para repetir a execução do código até que o programa se encerre.
        oqueFazer = int(input('\nO que você deseja fazer? \n1- Criar cliente\n2- Criar conta_ Imcompleto\n3- Excluir cliente_ Imcompleto\n4- Excluir conta _ Imcompleto\n5- Exibir cliente_ Imcompleto\n6- Exibir conta _ Imcompleto\n7- Encerrar aplicação\n'))
        if oqueFazer == 1: #Função: Criar um objeto da classe Cliente.
            criacliente()
        elif oqueFazer == 2: #busca o cliente e cria a conta
            criaconta(clientes)
    except ValueError:
        print('Por favor, insira um número válido.')        