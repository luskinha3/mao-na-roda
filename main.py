# -*- coding: utf-8 -*-
# development-branch

# funcionalidades extras para implementar e bug fixes
# criar status da manifestação e a mudança de status -- feito
# mudar metodo escreve dicionario -- feito
# sistema de cadastro e login -- feito
# sistema de log-off -- feito
# bug heap infinito -- feito
# tratar retorno vazio na saida dos dicionarios -- feito
# adicionar o lsitar minhas reclamações -- feito
# verificar função get_by_id -- feito
# tratar erros de inserir dados errados -- feito
# remover manifestação. -- feito

# adicionar comentario a manifestação





from tabulate import tabulate

manifestacoes = {}
manifestacoes[0] = {"ID": 1, "Nome": "Kamado tanjiro", "Tipo": "reclamação", "Conteudo": "espadas quebradiças"}
manifestacoes[1] = {"ID": 2, "Nome": "Nezuko kamado", "Tipo": "sugestão", "Conteudo": "comprar uma caixa maior"}
manifestacoes[2] = {"ID": 3, "Nome": "Kyojuro Rengoku", "Tipo": "sugestão", "Conteudo": "comida estava otima"}
id = len(manifestacoes) + 1

usuarios = {}

usuario_logado = {}

usuario_logado_nome = ""

logado = False


def acoes_login(acaostr):
    acao = int(acaostr)

    if acao < 1 or acao > 3:
        print("-------------------------------------")
        print("|         ! Ação invalida !         |")

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
    manifestacoes = {}
    usuarios[email] = {"Nome": nome, "E-mail": email, "Senha": senha, "Manifestacoes": manifestacoes}
    print("-----------------------------------------------")
    print("|          ! Usuario cadastrado !             |")
    print("-----------------------------------------------")


def logout():
    global usuario_logado
    global logado
    usuario_logado = None
    logado = False


def login_usuario():
    global usuario_logado
    global usuario_logado_nome
    global logado
    print("-----------------------------------------------")
    print("|          ! Bem vindo ao Login !             |")
    print("-----------------------------------------------")
    email = input("Informe seu E-mail: ").strip().lower()
    senha = input("Informe sua senha: ")
    usuario = usuarios.get(email)
    if not (usuarios.get(email)):
        print("-------------------------------------------------")
        print("|         ! Informe um usuario válido !         |")
    elif not senha in usuario['Senha']:
        print("-------------------------------------------------")
        print("|         ! Informe uma senha válida !          |")
    else:
        usuario_logado = usuario
        usuario_logado_nome = usuario["Nome"]
        logado = True


def list_manifestacoes_usr():
    table = {}
    global usuario_logado
    manifestacoes = usuario_logado["Manifestacoes"]
    for key, value in manifestacoes.items():
        table[key] = value

    imprimir_dicionario(table)


def acoes_logado(acaostr):
    acao = int(acaostr)
    if acao < 0 or acao > 9:
        print("-------------------------------------")
        print("|         ! Ação invalida !         |")

    if acao == 1:
        list_manifestacoes()
    if acao == 2:
        busca_por_tipo('sugestão')

    if acao == 3:
        busca_por_tipo('reclamação')

    if acao == 4:
        busca_por_tipo('elogio')

    if acao == 5:
        cadastra_manifestacao()

    if acao == 6:
        get_by_id()

    if acao == 7:
        remover_manifestacao()
    if acao == 8:
        comentar_manifestacao()

    if acao == 9:
        list_manifestacoes_usr()
    if acao == 0:
        logout()


def remover_manifestacao():
    global manifestacoes
    manifestacoes_usr = usuario_logado["Manifestacoes"]
    vazio = not bool (manifestacoes_usr)

    if  vazio:
        print("------------------------------------------------------------------")
        print("|       ! Você não tem nenhuma manifestação para excluir !       |")
        print("------------------------------------------------------------------")
    else:
        imprimir_dicionario(manifestacoes_usr)
        print("----------------------------------------------")
        id = int(input("Informe o Id da manifestação que deseja encerrar:").strip())
        id_incorreto = not bool (manifestacoes_usr.get(id))
        if id_incorreto:
            print("------------------------------------------------------------------")
            print("|                  ! Informe um ID válido !                      |")
            print("------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------")
            print("|       ! Manifestação removida com sucesso !       |")
            print("------------------------------------------------------------------")
            manifestacoes_usr.pop(id)
            manifestacoes.pop(id)

def comentar_manifestacao():
    print("-----------------------------------------------------")
    list_manifestacoes()
    print("-----------------------------------------------------")
    id = int(input("Informe o id da manifestação que deseja comentar: "))

def cadastra_manifestacao():
    global id
    global usuario_logado_nome
    print("----------------------------------------------")
    print("Bem vindo ao cadastro de uma nova reclamação")
    tipo = input("Informe o tipo da reclamação ----> Opções: |Elogio|Reclamação|Sugestão| ").lower().strip()
    if tipo != "elogio" and tipo != "reclamação" and tipo != "sugestão":
        print("-----------------------------------------------------------------")
        print("|       ! Tipo informado é invalido, tente novamente !          |")
        print("-----------------------------------------------------------------")
    else:
        conteudo = input("Nos detalhe o que deseja manifestar: ").strip()
        manifestacoes[id] = {"ID": id, "Nome": usuario_logado_nome, "Tipo": tipo, "Conteudo": conteudo }
        manifestacoes_usuario = usuario_logado["Manifestacoes"]
        manifestacoes_usuario[id] = {"ID": id, "Tipo": tipo, "Conteudo": conteudo}
        print("----------------------------------------------")
        print("|   Nova manifestação criada com sucesso!    |")
        id = len(manifestacoes) + 1


def sair():
    print("Obrigado por utilizar nosso sitema !")
    print("----------------------------------------------")
    exit()


def list_manifestacoes():
    table = {}
    global manifestacoes
    for key, value in manifestacoes.items():
        table[key] = value

    imprimir_dicionario(table)


def busca_por_tipo(tipo):
    table = {}

    for id, manifestacao in manifestacoes.items():
        if tipo in manifestacao['Tipo']:
            table[id] = manifestacao
    imprimir_dicionario(table)


def get_by_id():
    table = {}
    print("----------------------------------------------")
    id = int(input("Informe o Id da manifestação que deseja procurar:").strip()) - 1
    if not (manifestacoes.get(id)):
        print("--------------------------------------------")
        print("|         ! Informe um id valido !         |")
    else:
        manifestacao = manifestacoes.get(id)
        table[id] = manifestacao
        imprimir_dicionario(table)


def imprimir_dicionario(dicionario):
    # receber um dicionario e transformar em array
    table = []
    for key, values in dicionario.items():
        table.append(values)
    if len(table) > 0:
        print(tabulate(table, headers="keys", tablefmt="grid"))
    else:
        print("--------------------------------------------------")
        print("|        ! Nenhum elemento encontrado !          |")


def usr_deslogado():
    global logado
    while not logado:
        print("-----------------------------------------------------------------------------------------------")
        print("Bem vindo ao sistema de ouvidoria da Facisa! Faça seu cadastro e login para utilizar o sistema.")
        print("-----------------------------------------------------------------------------------------------")
        print("| 1 - Login              |")
        print("| 2 - Cadastro           |")
        print("| 3 - Finalizar programa |")
        print("----------------------------------------------")
        acao = int(input("Selecione a ação que deseja realizar: "))
        acoes_login(acao)


def usr_logado():
    global logado
    while logado:
        print("-----------------------------------------------")
        print("Bem vindo ao sistema de ouvidoria da Facisa !")
        print("-----------------------------------------------")
        print("| 1 - Listar todas as manifestações         |")
        print("| 2 - Listar todas as sugestões             |")
        print("| 3 - Listar todas as reclamações           |")
        print("| 4 - Listar todos os elogios               |")
        print("| 5 - Criar uma nova manifestação           |")
        print("| 6 - Pesquisar uma manifestação            |")
        print("| 7 - Encerrar queixa                       |")
        print("| 8 - Comentar manifestação                 |")
        print("| 9 - Listar minhas manifestações           |")
        print("| 0 - Sair                                  |")

        print("-----------------------------------------------")
        print("| Usuario Logado:", usuario_logado_nome, "                        |")
        print("-----------------------------------------------")
        acao = int(input("Selecione a ação que deseja realizar: "))
        acoes_logado(acao)


while (True):
    if logado == False:
        usr_deslogado()
    else:
        usr_logado()
