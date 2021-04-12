import pymysql
from pymysql.cursors import DictCursor


class Authorization:
        def __init__(self):
            self.connection = self.connect()
            self.cursors = self.connection.cursor()

        def connect(self):
            connection = pymysql.connect(
                host='localhost',
                user='biven',
                password='11T32cS1',
                db='university',
                charset='utf8mb4',
                cursorclass=DictCursor
            )
            return connection




        def getUsers(self, login, password):
            sql = f"SELECT * FROM human WHERE login = '{login}' and password = '{password}'"
            self.cursors.execute(sql)
            data = self.cursors.fetchall()
            return data












