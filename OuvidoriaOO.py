# -*- coding: utf-8 -*-

# adicionar hash paras senha
# consertar a captura do nome dos usuarios
# inserir e tratar exceptions
# impedir que o usuario remova manifestações que não são dele

import pymysql


class Conexao:
    conexao = None

    def get_conexao(self):
        try:
            self.conexao = pymysql.connect(host="bv2rebwf6zzsv341.cbetxkdyhwsb.us-east-1.rds.amazonaws.com", port=3306,
                                           database="o9ipsxm355ufciyi", user="yus0av9ms1xqmj1q",
                                           password="dvnwd91rnw5tyzho")
        except Exception as e:
            print("Conexão não pode ser concluída")
        finally:
            return self.conexao


class Usuario:
    id = 0
    nome = ""
    email = ""
    senha = ""
    manifestacoes = {}

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha


class Sistema:
    manifestacoes = {}
    usuario_logado = None
    logado = False

    def get_logado(self):
        return self.logado

    def set_logado(self, estado):
        self.logado = estado

    def acoes_login(self, acaostr):
        acao = int(acaostr)

        if acao < 1 or acao > 3:
            print("-------------------------------------")
            print("|         ! Ação invalida !         |")

        # logar
        if acao == 1:
            print("-----------------------------------------------")
            print("|          ! Bem vindo ao Login !             |")
            print("-----------------------------------------------")
            email = input("Informe seu E-mail: ").strip().lower()
            senha = input("Informe sua senha: ")
            resultado = self.login_usuario(email, senha)
            return resultado

        # cadastrar
        if acao == 2:
            print("-----------------------------------------------")
            print("|         ! Bem vindo ao cadastro !           |")
            print("-----------------------------------------------")
            nome = input("Informe seu nome: ").strip().lower()
            email = input("Informe seu e-mail: ").strip().lower()
            senha = input("Informe sua senha: ")
            resultado = self.cadastro_usuario(nome, email, senha)
            print(resultado)
        if acao == 3:
            self.sair()

    def cadastro_usuario(self, nome, email, senha):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "INSERT INTO usuarios (nome_usuario,email,senha) VALUES (%s,%s,%s) "
        dados = (str(nome), str(email), str(senha))

        try:
            cursor.execute(comandoSql, dados)
            conexao.commit()
        except Exception as e:
            conexao.rollback()
        finally:
            conexao.close()

    def login_usuario(self, email, senha):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT usuarios.nome_usuario FROM usuarios WHERE usuarios.email = %s AND usuarios.senha = %s "
        dados = (str(email), str(senha))

        usuario = cursor.execute(comandoSql, dados)

        nome = cursor.fetchall()

        if usuario == 0:
            conexao.close()
            raise Exception
        else:
            usuario = Usuario("puquinha", email, senha)
            self.usuario_logado = usuario
            self.usuario_logado_nome = nome
            conexao.close()
            self.set_logado(True)

    def sair(self):
        print("Obrigado por utilizar nosso sitema !")
        print("----------------------------------------------")
        exit()

    def acoes_logado(self, acaostr):
        acao = int(acaostr)
        if acao < 0 or acao > 9:
            print("-------------------------------------")
            print("|         ! Ação invalida !         |")

        if acao == 1:
            manifestacoes = self.list_manifestacoes()
        if acao == 2:
            manifestacoes = self.busca_por_tipo('sugestão')
        if acao == 3:
            manifestacoes = self.busca_por_tipo('reclamação')
        if acao == 4:
            manifestacoes = self.busca_por_tipo('elogio')
        if acao == 5:
            print("----------------------------------------------")
            print("Bem vindo ao cadastro de uma nova reclamação")
            tipo = input("Informe o tipo da reclamação ----> Opções: |Elogio|Reclamação|Sugestão| ").lower().strip()
            conteudo = input("Nos detalhe o que deseja manifestar: ").strip()
            self.cadastra_manifestacao(tipo, conteudo, 5)
        if acao == 6:
            print("----------------------------------------------")
            id_manifestacao = int(input("Informe o Id da manifestação que deseja procurar:").strip())
            manifestacao = self.get_by_id(id_manifestacao)
        if acao == 7:
            print("----------------------------------------------")
            id_encerramento = int(input("Informe o Id da manifestação que deseja encerrar:").strip())
            self.remover_manifestacao(id_encerramento)
        if acao == 8:
            manifestacoes_usr = self.list_manifestacoes_usr(self.usuario_logado.get_nome())
        if acao == 0:
            self.logout()

    def list_manifestacoes(self):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT id_manifestacao, conteudo, tipo, usuarios.nome_usuario FROM manifestacoes INNER JOIN usuarios on manifestacoes.usuario = usuarios.id_usuario"

        cursor.execute(comandoSql)
        manifestacoes = cursor.fetchall()
        conexao.close()
        return manifestacoes

    def list_manifestacoes_usr(self, nome):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT id_manifestacao, conteudo, tipo, usuarios.nome_usuario FROM manifestacoes INNER JOIN usuarios on manifestacoes.usuario = usuarios.id_usuario where usuarios.nome_usuario = %s"
        dados = nome
        cursor.execute(comandoSql, dados)
        manifestacoes = cursor.fetchall()
        conexao.close()
        return manifestacoes

    def busca_por_tipo(self, tipo):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT id_manifestacao, conteudo, tipo, usuarios.nome_usuario FROM manifestacoes INNER JOIN usuarios on manifestacoes.usuario = usuarios.id_usuario WHERE tipo = %s "
        dados = tipo
        cursor.execute(comandoSql, dados)
        manifestacoes = cursor.fetchall()

        conexao.close()
        return manifestacoes

    def cadastra_manifestacao(self, tipo, conteudo, id_usuario):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "INSERT INTO manifestacoes (conteudo,tipo,usuario) VALUES (%s,%s,%s) "
        dados = (str(conteudo), str(tipo), int(id_usuario))

        try:
            cursor.execute(comandoSql, dados)
            conexao.commit()
        except Exception as e:
            print("deu ruim")
            conexao.rollback()
        finally:
            conexao.close()

    def remover_manifestacao(self, id):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "DELETE FROM  manifestacoes  WHERE manifestacoes.id_manifestacao = %s "
        dados = int(id)

        try:
            cursor.execute(comandoSql, dados)
            conexao.commit()
        except Exception as e:
            print("deu ruim")
            conexao.rollback()
        finally:
            conexao.close()

    def get_by_id(self, id):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT id_manifestacao, conteudo, tipo, usuarios.nome_usuario FROM manifestacoes INNER JOIN usuarios on manifestacoes.usuario = usuarios.id_usuario WHERE id_manifestacao = %s "
        dados = id
        cursor.execute(comandoSql, dados)
        manifestacoes = cursor.fetchall()
        print(manifestacoes)
        conexao.close()
        return manifestacoes

    def logout(self):
        self.set_logado(False)


class Menu:
    sistema = Sistema()

    def iniciar(self):

        while True:
            if self.sistema.get_logado():
                self.usr_logado()
            else:
                self.usr_deslogado()

    def usr_deslogado(self):
        while not self.sistema.get_logado():
            print("-----------------------------------------------------------------------------------------------")
            print("Bem vindo ao sistema de ouvidoria da Facisa! Faça seu cadastro e login para utilizar o sistema.")
            print("-----------------------------------------------------------------------------------------------")
            print("| 1 - Login              |")
            print("| 2 - Cadastro           |")
            print("| 3 - Finalizar programa |")
            print("----------------------------------------------")
            acao = int(input("Selecione a ação que deseja realizar: "))
            self.sistema.acoes_login(acao)

    def usr_logado(self):
        while self.sistema.get_logado():
            print("-----------------------------------------------")
            print("Bem vindo ao sistema de ouvidoria da Facisa !")
            print("-----------------------------------------------")
            print("| 1 - Listar todas as manifestações         |")
            print("| 2 - Listar todas as sugestões             |")
            print("| 3 - Listar todas as reclamações           |")
            print("| 4 - Listar todos os elogios               |")
            print("| 5 - Criar uma nova manifestação           |")
            print("| 6 - Pesquisar uma manifestação            |")
            print("| 7 - Excluir manifestação                  |")
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

    ''' classe para ser implementado no modelo rest futuramente
  class Manifestacao:

  id_usuario = 0
  tipo = ''
  conteudo = ''
  usuario = None

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
      
       
      
      
    '''
