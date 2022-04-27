# -*- coding: utf-8 -*-

# adicionar tratamento de rollback
# adicionar hash paras senha
# impedir mysql injection
# consertar a captura do nome do usuario

import pymysql

class Conexao:
    conexao = None
    def conexao(self):
        try:
         self.conexao =  pymysql.connect(host="bv2rebwf6zzsv341.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",port=3306,database="o9ipsxm355ufciyi",user="yus0av9ms1xqmj1q",password="dvnwd91rnw5tyzho")
        except Exception as e:
          print("Conexão não pode ser concluída")
        finally:
         return self.conexao
class Usuario:

  nome = ""
  email = ""
  senha = ""
  manifestacoes = {}

  def __init__(self,nome,email,senha):
      self.nome = nome
      self.email = email
      self.senha = senha

  def get_nome(self):
      return self.nome

  def get_email(self):
      return self.email

  def get_senha(self):
      return self.senha


class Manifestacao:

  id_usuario = 0
  tipo = ''
  conteudo = ''

  def __init__(self,Usuario,tipo,conteudo):
      self.Usuario = Usuario
      self.tipo = tipo
      self.conteudo = conteudo

  def get_tipo(self):
      return self.tipo

  def get_conteudo(self):
      return self.conteudo

  def get_Usuario(self):
      return self.Usuario



class Sistema:

  manifestacoes = {}
  usuario_logado = None



  def acoes_login(self,acaostr):
      acao = int(acaostr)

      if acao < 1 or acao > 3:
          print("-------------------------------------")
          print("|         ! Ação invalida !         |")

       #logar
      if acao == 1:
          print("-----------------------------------------------")
          print("|          ! Bem vindo ao Login !             |")
          print("-----------------------------------------------")
          email = input("Informe seu E-mail: ").strip().lower()
          senha = input("Informe sua senha: ")
          resultado = self.login_usuario(email,senha)
          return resultado

       #cadastrar
      if acao == 2:
          print("-----------------------------------------------")
          print("|         ! Bem vindo ao cadastro !           |")
          print("-----------------------------------------------")
          nome = input("Informe seu nome: ").strip().lower()
          email = input("Informe seu e-mail: ").strip().lower()
          senha = input("Informe sua senha: ")
          resultado = self.cadastro_usuario(nome,email,senha)
          print (resultado)
      if acao == 3:
          self.sair()

  def cadastro_usuario(self,nome,email,senha):

        dataBase = Conexao()
        conexao = dataBase.conexao()
        cursor = conexao.cursor()

        comandoSql = "INSERT INTO usuarios (nome_usuario,email,senha) VALUES (%s,%s,%s) "
        dados = (str(nome),str(email),str(senha))

        try:
            cursor.execute(comandoSql,dados)
            conexao.commit()
        except Exception as e:
            conexao.rollback()
        finally:
            conexao.close()

  def login_usuario(self,email,senha):

      dataBase = Conexao()
      conexao = dataBase.conexao()
      cursor = conexao.cursor()

      comandoSql = "SELECT usuarios.nome_usuario FROM usuarios WHERE usuarios.email = %s AND usuarios.senha = %s "
      dados = (str(email),str(senha))

      usuario = cursor.execute(comandoSql,dados)

      nome = cursor.fetchall()


      if usuario == 0:
          conexao.close()
          raise Exception
      else:
          usuario = Usuario("Pucca",email,senha)
          self.usuario_logado = usuario
          self.usuario_logado_nome = nome
          conexao.close()
          return True




      #return True

  def sair(self):
      print("Obrigado por utilizar nosso sitema !")
      print("----------------------------------------------")
      exit()

  def acoes_logado(self,acaostr):
      acao = int(acaostr)
      if acao < 0 or acao > 9:
          print("-------------------------------------")
          print("|         ! Ação invalida !         |")

      if acao == 1:
          self.list_manifestacoes()
      if acao == 2:
          self.busca_por_tipo('sugestão')
      if acao == 3:
          self.busca_por_tipo('reclamação')
      if acao == 4:
          self.busca_por_tipo('elogio')
      if acao == 5:
          self.cadastra_manifestacao()
      if acao == 6:
          self.get_by_id()
      if acao == 7:
          self.remover_manifestacao()
      if acao == 8:
          self.list_manifestacoes_usr()
      if acao == 0:
          self.logout()




class Menu:

    sistema = Sistema()
    logado = False

    def get_logado(self):
        return self.logado

    def set_logado(self, logado):
        self.logado = logado

    def iniciar(self):

        while True:
            if self.get_logado():
                self.usr_logado()
            else:
                self.usr_deslogado()

    def usr_deslogado(self):
        while not self.logado:
            print("-----------------------------------------------------------------------------------------------")
            print("Bem vindo ao sistema de ouvidoria da Facisa! Faça seu cadastro e login para utilizar o sistema.")
            print("-----------------------------------------------------------------------------------------------")
            print("| 1 - Login              |")
            print("| 2 - Cadastro           |")
            print("| 3 - Finalizar programa |")
            print("----------------------------------------------")
            acao = int(input("Selecione a ação que deseja realizar: "))
            resultado = self.sistema.acoes_login(acao)
            if acao == 1:
                self.set_logado(resultado)

    def usr_logado(self):
        while self.logado:
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
            print("| 8 - Listar minhas manifestações           |")
            print("| 0 - Sair                                  |")

            print("-----------------------------------------------")
            nome = self.sistema.usuario_logado.get_nome()
            print("| Usuario Logado: " + nome + " |")
            print("-----------------------------------------------")
            acao = int(input("Selecione a ação que deseja realizar: "))
            self.sistema.acoes_logado(acao)




class Main:

  menu = Menu()
  menu.iniciar()
  #banco = Conexao()
  #banco.conexao()


  '''
  def cadastra_manifestacao(self):
      global id
      global usuario_logado_nome

      print("----------------------------------------------")
      print("Bem vindo ao cadastro de uma nova reclamação")
      tipo = input("Informe o tipo da reclamação ----> Opções: |Elogio|Reclamação|Sugestão| ").lower().strip()

      if tipo != "elogio" and tipo != "reclamação" and tipo != "sugestão":
          raise NameError(("|       ! Tipo informado é invalido, tente novamente !          |"))

      conteudo = input("Nos detalhe o que deseja manifestar: ").strip()
      manifestacao = Manifestacao(self.usuario_logado,tipo,conteudo)
      manifestacoes_usuario = self.usuario_logado.getManifestacoes()
      manifestacoes_usuario[self.id] = manifestacao
      print("----------------------------------------------")
      print("|   Nova manifestação criada com sucesso!    |")
      id =+ 1
      
       def logout(self):
      self.usuario_logado = None
      self.logado = False
      
      
    '''
