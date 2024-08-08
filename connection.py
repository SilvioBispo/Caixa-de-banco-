import mysql.connector

class connection:
    def __init__(self, host = "localhost", user = "root" , password = "" , database = "caixaecono"):
        self.host = host
        self.user = user
        self.pwd = password
        self.db = database

    def connect(self):
        self.conn = mysql.connector.connect(host = self.host , user = self.user , password = self.pwd , database = self.db)

        self.cur = self.conn.cursor()

    def desconnect(self):
        self.cur.close()
        self.conn.close()

    def execute_commit(self, sql):
        self.connect()
        self.cur.execute(sql)
        self.conn.commit()
        self.desconnect()

    def execute_fetchall(self,sql):
        self.connect()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.desconnect()
        return res

    def execute_fetchone(self,sql):
        self.connect()
        self.cur.execute(sql)
        res = self.cur.fetchone()
        self.desconnect()
        return res