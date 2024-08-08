from connection import connection

class cadastro:
    def __init__(self,n,c):
        self.nome = n
        self.cpf = c

        cnnct = connection()

        cnnct.execute_commit(f'INSERT INTO cadastro (nome, cpf) VALUES ("{self.nome}", {self.cpf})')

        cnnct.execute_commit(f'insert into conta (id) select id from cadastro ORDER BY id DESC Limit 1 ')

        rep = cnnct.execute_fetchall(f'SELECT id FROM conta ORDER BY id DESC Limit 1;')

        print(f"numero da sua conta: {rep[0][0]}")

        cnnct.execute_commit(f'UPDATE conta SET dtm = (NOW()) WHERE id > (1) ORDER BY id DESC limit 1')

        cnnct.desconnect()


       






