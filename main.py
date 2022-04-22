# -*- coding: utf-8 -*-
# development-branch

# funcionalidades extras para implementar
# criar status da manifestação e a mudança de status
# adicionar comentario a manifestação
# sistema de cadastro e login - feito
# sistema de log-off
from tabulate import tabulate


manifestacoes = {}
manifestacoes[0] = {"ID": 1, "Nome": "Kamado tanjiro", "Tipo": "reclamação", "Conteudo": "espadas quebradiças"}
manifestacoes[1] = {"ID": 2, "Nome": "Nezuko kamado", "Tipo": "sugestão", "Conteudo": "comprar uma caixa maior"}
manifestacoes[2] = {"ID": 3, "Nome": "Kyojuro Rengoku", "Tipo": "sugestão", "Conteudo": "comida estava otima"}
id = len(manifestacoes) + 1

usuarios = {}

usuario_logado = {}

usuario_logado_nome = ""



def menu_login():
    print("-----------------------------------------------------------------------------------------------")
    print("Bem vindo ao sistema de ouvidoria da Facisa! Faça seu cadastro e login para utilizar o sistema.")
    print("-----------------------------------------------------------------------------------------------")
    print("| 1 - Login              |")
    print("| 2 - Cadastro           |")
    print("| 3 - Finalizar programa |")
    print("----------------------------------------------")
    acao = int(input("Selecione a ação que deseja realizar: "))
    acoes_login(acao)

def acoes_login(acaostr):
    acao = int(acaostr)

    if acao < 1 or acao > 3:
        print("-------------------------------------")
        print("|         ! Ação invalida !         |")
        menu_logado()

    if acao == 1:
        login_usuario()

    if acao == 2:
        cadastro_usuairo()
    if acao == 3:
        sair()

def cadastro_usuairo():
    print("-----------------------------------------------")
    print("|         ! Bem vindo ao cadastro !           |")
    print("-----------------------------------------------")
    nome = input("Informe seu nome: ").strip().lower()
    email = input("Informe seu e-mail: ").strip().lower()
    senha = input("Informe sua senha: ")
    manifestacoes = []
    usuarios[email] = {"Nome":nome,"E-mail":email,"Senha":senha, "Manifestacoes":manifestacoes}
    print("-----------------------------------------------")
    print("|          ! Usuario cadastrado !             |")
    print("-----------------------------------------------")
    menu_login()

def login_usuario():
    global  usuario_logado
    global usuario_logado_nome
    print("-----------------------------------------------")
    print("|          ! Bem vindo ao Login !             |")
    print("-----------------------------------------------")
    email = input("Informe seu E-mail: ").strip().lower()
    senha = input("Informe sua senha: ")

    if not (usuarios.get(email)):
        print("-------------------------------------------------")
        print("|         ! Informe um usuario válido !         |")
        menu_login()

    usuario = usuarios.get(email)

    if not senha in usuario['Senha']:
        print("-------------------------------------------------")
        print("|         ! Informe uma senha válida !          |")
        login_usuario()
    usuario_logado = usuario
    usuario_logado_nome = usuario["Nome"]
    menu_logado()




def menu_logado():
    global usuario_logado_nome
    print("-----------------------------------------------")
    print("Bem vindo ao sistema de ouvidoria da Facisa !")
    print("-----------------------------------------------")
    print("1 - Listar todas as manifestações")
    print("2 - Listar todas as sugestões")
    print("3 - Listar todas as reclamações")
    print("4 - Listar todos os elogios")
    print("5 - Criar uma nova manifestação")
    print("6 - Pesquisar uma manifestação")
    print("7 - Sair")
    print("-----------------------------------------------")
    print("| Usuario Logado:", usuario_logado_nome,"                        |" )
    print("-----------------------------------------------")
    acao = int(input("Selecione a ação que deseja realizar: "))
    acoes_logado(acao)


def acoes_logado(acaostr):
    acao = int(acaostr)
    if acao < 1 or acao > 8:
        print("-------------------------------------")
        print("|         ! Ação invalida !         |")
        menu_logado()

    if acao == 1:
        list_manifestacoes()
    if acao == 2:
        busca_por_tipo('sugestão')

    if acao == 3:
        busca_por_tipo('reclamação')

    if acao == 4:
        busca_por_tipo('elogio')

    if acao == 5:
        cadastro()

    if acao == 6:
        print("----------------------------------------------")
        id = input("Informe o Id da manifestação que deseja procurar:").strip()
        get_by_id(id)

    if acao == 7:
        print("remover")
        print("----------------------------------------------")
        id = input("Informe o Id da manifestação que deseja encerrar:").strip()
        # encerrar_manifestacao(id)
    if acao == 8:
        sair()




def cadastro():
    global id
    print("----------------------------------------------")
    print("Bem vindo ao cadastro de uma nova reclamação")
    nome = input("Informe seu nome: ").strip()
    tipo = input("Informe o tipo da reclamação ----> Opções: |Elogio|Reclamação|Sugestão| ").lower().strip()
    if tipo != "elogio" and tipo != "reclamação" and tipo != "sugestão":
        print("-----------------------------------------------------------------")
        print("|       ! Tipo informado é invalido, tente novamente !          |")
        print("-----------------------------------------------------------------")
        menu_logado()
    conteudo = input("Nos detalhe o que deseja manifestar: ").strip()
    manifestacoes[id] = {"ID": id, "Nome": nome, "Tipo": tipo, "Conteudo": conteudo}
    print("----------------------------------------------")
    print("|   Nova manifestação criada com sucesso!    |")
    id = len(manifestacoes) + 1
    menu_logado()


def sair():
    print("Obrigado por utilizar nosso sitema !")
    print("----------------------------------------------")
    exit()


def list_manifestacoes():
    table = []
    for manifestacao in manifestacoes.values():
        table.append(manifestacao)
    imprimir_dicionario(table)
    menu_logado()


def busca_por_tipo(tipo):
    table = []

    for id, manifestacao in manifestacoes.items():
        if tipo in manifestacao['Tipo']:
            table.append(manifestacao)
    imprimir_dicionario(table)
    menu_logado()


def get_by_id(id):
    id_int = int(id) - 1
    if not (manifestacoes.get(id_int)):
        print("--------------------------------------------")
        print("|         ! Informe um id valido !         |")
        menu_logado()
    manifestacao = manifestacoes.get(id_int)
    imprimir_dicionario(table=[manifestacao])
    menu_logado()


def imprimir_dicionario(table):
    print(tabulate(table, headers="keys", tablefmt="grid"))

menu_login()
