class Usuario:
    id = 0
    nome = ""
    email = ""
    senha = ""
    manifestacoes = {}

    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def get_id(self):
        return self.id