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