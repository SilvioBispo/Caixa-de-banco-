from connection import connection

class conta:
    def __init__(self,id):
        self.id = id
        cnnct = connection()

        comp = cnnct.execute_fetchall(f'SELECT count(1) from cadastro WHERE id = {self.id}')
        if comp != 0:

            res = cnnct.execute_fetchall(f'SELECT nome , cpf from cadastro WHERE id = {self.id}')

            print('dados da conta: {}, {}'.format(res[0][0],res[0][1]))


        cnnct.desconnect()