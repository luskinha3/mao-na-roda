# -*- coding: utf-8 -*-
from tabulate import tabulate

manifestacoes = {}
manifestacoes[0] = {"ID": 1, "Nome": "Kamado tanjiro", "Tipo": "reclamação", "Conteudo": "espadas quebradiças"}
manifestacoes[1] = {"ID": 2, "Nome": "Nezuko kamado", "Tipo": "sugestão", "Conteudo": "comprar uma caixa maior"}
manifestacoes[2] = {"ID": 3, "Nome": "Kyojuro Rengoku", "Tipo": "sugestão", "Conteudo": "comida estava otima"}
id = len(manifestacoes) + 1


def menu():
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
    print("----------------------------------------------")
    acao = int(input("Selecione a ação que deseja realizar: "))
    acoes(acao)


def acoes(acaostr):
    acao = int(acaostr)
    if acao < 1 or acao > 7:
        print("-------------------------------------")
        print("|         ! Ação invalida !         |")
        menu()

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
        id = input("Informe o Id da manifestação que deseja procurar:")
        get_by_id(id)

    if acao == 7:
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
        menu()
    conteudo = input("Nos detalhe o que deseja manifestar: ").strip()
    manifestacoes[id] = {"ID": id, "Nome": nome, "Tipo": tipo, "Conteudo": conteudo}
    print("----------------------------------------------")
    print("|   Nova manifestação criada com sucesso!    |")
    id = len(manifestacoes) + 1
    menu()


def sair():
    print("Obrigado por utilizar nosso sitema !")
    print("----------------------------------------------")
    exit()


def list_manifestacoes():
    table = []
    for manifestacao in manifestacoes.values():
        table.append(manifestacao)
    imprimir_dicionario(table)
    menu()


def busca_por_tipo(tipo):
    table = []

    for id, manifestacao in manifestacoes.items():
        if tipo in manifestacao['Tipo']:
            table.append(manifestacao)
    imprimir_dicionario(table)
    menu()


def get_by_id(id):
    id_int = int(id) - 1
    if not (manifestacoes.get(id_int)):
        print("--------------------------------------------")
        print("|         ! Informe um id valido !         |")
        menu()
    manifestacao = manifestacoes.get(id_int)
    imprimir_dicionario(table=[manifestacao])
    menu()


def imprimir_dicionario(table):
    print(tabulate(table, headers="keys", tablefmt="grid"))

menu()
