from connection import connection

class saldo:
    def __init__(self,i,s,op):
        self.i = i
        self.s = s
        self.op = op

        cnnct = connection()
        if (self.op == 'deposito'):

          rsa = cnnct.execute_fetchone(f'SELECT saldo FROM conta WHERE id = {self.i}')

          dslda = rsa[0] + int(self.s)

          cnnct.execute_commit( f'UPDATE conta SET saldo ={dslda} WHERE id = {self.i}')

        elif (self.op == 'saque'):

            rsa = cnnct.execute_fetchone( f'SELECT saldo FROM conta WHERE id = {self.i}')

            sslda = rsa[0] - int(self.s)

            cnnct.execute_commit(f'UPDATE conta SET saldo ={sslda} WHERE id = {self.i}')


        cnnct.execute_commit(f'UPDATE conta SET dtm = (NOW()) WHERE id = {self.i}')

        shwsaldo = cnnct.execute_fetchall(f'SELECT saldo FROM conta WHERE id = {self.i}')

        shwdtm = cnnct.execute_fetchall(f'SELECT date_format(dtm, "%d/%m/%Y e %H:%i") from conta WHERE id = {self.i}')

        print('saldo atualizado:', shwsaldo[0][0])
        print('data e hora da ultima movimentaçao:', shwdtm[0][0])

        cnnct.desconnect()


