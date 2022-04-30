## mensagem de sucesso para deletar manifestação
## mensagem de erro caso usuario passe uma ação invalida

from ControlerClass import Sistema
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
            self.acoes_login(acao)

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
            self.acoes_logado(acao)


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
            try:
                self.sistema.login_usuario(email, senha)

            except Exception as e:
                print("-------------------------------------------------------")
                print("|     ! Informações invalidas, tente novamente !     |")

        # cadastrar
        if acao == 2:
            print("-----------------------------------------------")
            print("|         ! Bem vindo ao cadastro !           |")
            print("-----------------------------------------------")
            nome = input("Informe seu nome: ").strip().lower()
            email = input("Informe seu e-mail: ").strip().lower()
            senha = input("Informe sua senha: ")
            sucesso = self.sistema.cadastro_usuario(nome, email, senha)
            if sucesso:
                print("| Usuario cadastrado com sucesso !")
            else:
                print("| algo não ocorreu como esperado !")
        if acao == 3:
            self.sistema.sair()

    def acoes_logado(self, acaostr):
        acao = int(acaostr)
        if acao < 0 or acao > 8:
            print("-------------------------------------")
            print("|         ! Ação invalida !         |")

        if acao == 1:
            manifestacoes = self.sistema.list_manifestacoes()
            self.sistema.imprimir_tupla(manifestacoes)
        if acao == 2:
            manifestacoes = self.sistema.busca_por_tipo('sugestão')
            self.sistema.imprimir_tupla(manifestacoes)
        if acao == 3:
            manifestacoes = self.sistema.busca_por_tipo('reclamação')
            self.sistema.imprimir_tupla(manifestacoes)
        if acao == 4:
            manifestacoes = self.sistema.busca_por_tipo('elogio')
            self.sistema.imprimir_tupla(manifestacoes)
        if acao == 5:
            print("----------------"
                  "------------------------------")
            print("Bem vindo ao cadastro de uma nova reclamação")
            tipo = input("Informe o tipo da reclamação ----> Opções: |Elogio|Reclamação|Sugestão| ").lower().strip()
            conteudo = input("Nos detalhe o que deseja manifestar: ").strip()
            id_usr = self.sistema.usuario_logado.get_id()
            try:
                self.sistema.cadastra_manifestacao(tipo, conteudo, id_usr)
                print("-----------------------------------------------------------------")
                print("|             ! Manifestação cadastrada com sucesso !             |")
            except Exception as e:
                print("-----------------------------------------------------------------")
                print("|         !Não foi possivel cadastrar a manifestação!           |")
        if acao == 6:
            print("----------------------------------------------")
            id_manifestacao = int(input("Informe o Id da manifestação que deseja procurar:").strip())
            manifestacao = self.sistema.get_by_id(id_manifestacao)
            self.sistema.imprimir_tupla(manifestacao)
        if acao == 7:
            print("----------------------------------------------")
            id_encerramento = int(input("Informe o Id da manifestação que deseja encerrar:").strip())
            try:
                self.sistema.remover_manifestacao(id_encerramento, self.sistema.usuario_logado)
                print("---------------------------------------")
                print("| !Manifestação removida com sucesso! |")
            except  Exception as e:
                print("-------------------------------------------------------------------")
                print("| !Não foi possivel excluir a manifestação, informa um ID válido! |")
        if acao == 8:
            manifestacoes_usr = self.sistema.list_manifestacoes_usr(self.sistema.usuario_logado.get_nome())
            self.sistema.imprimir_tupla(manifestacoes_usr)
        if acao == 0:
            self.sistema.logout()