iniciar = True
manifestacoes = []
id = len(manifestacoes) + 1


while(iniciar):
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

    if(acao < 1 or acao >  7):
        print("-------------------------------------")
        print("|         ! Ação invalida !         |")
        continue

    #if(acao):

    #if(acao):

    #if(acao):

    #if(acao):

    if(acao == 5):
        print("----------------------------------------------")
        print("Bem vindo ao cadastro de uma nova reclamação")
        nome = input("Informe seu nome: ")
        tipo = input("Informe o tipo da reclamação --> Opções: |Elogio|Reclamação|Sugestão| ")
        if(tipo.lower() != "elogio" and tipo.lower() != "reclamação" and tipo.lower() != "sugestão" ):
            print("-----------------------------------------------------------------")
            print("|       ! Tipo informado é invalido, tente novamente !          |")
            print("-----------------------------------------------------------------")
            continue
        conteudo = input("Nos detalhe o que deseja manifestar: ")
        novaReclamacao = (id,"#",nome + "#" + tipo + "#" + conteudo)
        manifestacoes.append(novaReclamacao)
        print("----------------------------------------------")
        print("|   Nova manifestação criada com sucesso!    |")
        continue

    #if(acao):

    if(acao == 7):
        iniciar = False
        print("Obrigado por utilizar nosso sitema !")
        print("----------------------------------------------")
        continue

