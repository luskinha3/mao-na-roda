from ConexaoClass import Conexao
from UsuarioClass import Usuario
import uuid
import hashlib
from tabulate import tabulate

class Sistema:
    manifestacoes = {}
    usuario_logado = None
    logado = False

    def get_logado(self):
        return self.logado

    def set_logado(self, estado):
        self.logado = estado

    def get_salt(self, email):
        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT salt From usuarios WHERE email = %s "
        dados = (str(email))
        cursor.execute(comandoSql, dados)
        resultado = cursor.fetchone()
        conexao.close()
        return resultado

    def get_senha(self, email):
        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        comandoSql = "SELECT senha From usuarios WHERE email = %s "
        dados = (str(email))
        cursor.execute(comandoSql, dados)
        resultado = cursor.fetchone()
        conexao.close()
        return resultado



    def cadastro_usuario(self, nome, email, senha):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        salt = uuid.uuid4().hex
        senha_hash = hashlib.sha256(senha.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        comandoSql = "INSERT INTO usuarios (nome_usuario,email,senha, salt) VALUES (%s,%s,%s,%s) "
        dados = (str(nome), str(email), str(senha_hash), str(salt))

        try:
            cursor.execute(comandoSql, dados)
            conexao.commit()
            return True
        except Exception as e:
            conexao.rollback()
            return False
        finally:
            conexao.close()

    def login_usuario(self, email, senha):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()
        hash_senha_tupla = self.get_senha(email)
        salt_tupla = self.get_salt(email)
        hash_senha = str(hash_senha_tupla[0])
        salt = str(salt_tupla[0])
        senha_digitada = hashlib.sha256(senha.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        if senha_digitada != hash_senha:
            conexao.close()
            raise Exception
        else:
            comandoSql = "SELECT  usuarios.nome_usuario, usuarios.id_usuario FROM usuarios WHERE usuarios.email = %s AND usuarios.senha = %s "
            dados = (str(email), str(hash_senha))
            cursor.execute(comandoSql, dados)
            tuplas = cursor.fetchall()
            nome = ""
            id = ""
            for linha in tuplas:
                nome = linha[0]
                id = linha[1]

            usuario = Usuario(id, nome, email, senha)

            self.usuario_logado = usuario
            conexao.close()
            self.set_logado(True)

    def sair(self):
        print("Obrigado por utilizar nosso sitema !")
        print("----------------------------------------------")
        exit()



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
            conexao.rollback()
            raise Exception
        finally:
            conexao.close()

    def remover_manifestacao(self, id_manifestacao, usuario):

        dataBase = Conexao()
        conexao = dataBase.get_conexao()
        cursor = conexao.cursor()

        id_usuario = usuario.get_id()

        comandoSql = "DELETE FROM  manifestacoes  WHERE manifestacoes.id_manifestacao = %s and manifestacoes.usuario = %s "
        dados = (int(id_manifestacao), int(id_usuario))

        try:
            resultado = cursor.execute(comandoSql, dados)
            if resultado > 0:
                conexao.commit()
            else:
                raise Exception
        except Exception as e:
            conexao.rollback()
            raise Exception
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
        conexao.close()
        return manifestacoes

    def imprimir_tupla(self, tupla):
        # receber uma tupla e transformar em array
        table = []
        for linha in tupla:
            table.append(linha)
        if len(table) > 0:
            print(tabulate(table, headers=["ID", "Conteúdo", "Tipo", "Autor"], tablefmt="grid"))
        else:
            print("--------------------------------------------------")
            print("|        ! Nenhum elemento encontrado !          |")

    def logout(self):
        self.set_logado(False)

