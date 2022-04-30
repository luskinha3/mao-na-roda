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