# -*- coding: utf-8 -*-
manifestacoes = []
id = str(len(manifestacoes) + 1)


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

def acoes(acaoStr):
 acao = int(acaoStr)
 if (acao < 1 or acao > 7):
   print("-------------------------------------")
   print("|         ! Ação invalida !         |")
   menu()

 if(acao == 1):
   listManifestacoes()

   # if(acao):

   # if(acao):

   # if(acao):

 if (acao == 5):
   cadastro()
   # if(acao):

 if (acao == 7):
   sair()

def cadastro():

 global id
 print("----------------------------------------------")
 print("Bem vindo ao cadastro de uma nova reclamação")
 nome = raw_input("Informe seu nome: ")
 tipo = raw_input("Informe o tipo da reclamação ----> Opções: |Elogio|Reclamação|Sugestão| ")
 if (tipo.lower() != "elogio" and tipo.lower() != "reclamação" and tipo.lower() != "sugestão"):
   print("-----------------------------------------------------------------")
   print("|       ! Tipo informado é invalido, tente novamente !          |")
   print("-----------------------------------------------------------------")
   menu()
 conteudo = raw_input("Nos detalhe o que deseja manifestar: ")
 novaReclamacao = (id + "#" + nome + "#" + tipo + "#" + conteudo)
 manifestacoes.append(novaReclamacao)
 print("----------------------------------------------")
 print("|   Nova manifestação criada com sucesso!    |")
 id = str(len(manifestacoes))
 menu()
def sair():
 print("Obrigado por utilizar nosso sitema !")
 print("----------------------------------------------")
 exit()
def listManifestacoes():
 print("ID|NOME|TIPO|DESCRIÇÃO")
 for manifestacao in manifestacoes:
   saida = manifestacao.split("#")
   teste = "|"
   teste = teste.join(saida)
   print(teste)

 menu()
#def listSugestoes():
#def listReclamacoes():
#def listElogios():
#def getById():

menu()


