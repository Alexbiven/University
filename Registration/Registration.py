import pymysql
from pymysql.cursors import DictCursor

class Registration:

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



    def addUser(self, login, password, name, surname, status):
        sql = 'INSERT INTO human (id, login, password,name,surname,status) VALUES (%s, %s, %s, %s, %s,%s)'
        password = password.replace('a', '1').replace('c', '2')
        temp = ['NULL', login, password,name, surname,status]
        self.cursors.execute(sql, temp)
        self.connection.commit()
        if status == 'Student':
            sql = "INSERT INTO progress (id,name,surname,status,login) VALUES ( %s, %s ,%s ,%s , %s ) "
            temp = ['NULL',name,surname,status,login]
            self.cursors.execute(sql, temp)
            self.connection.commit()

    def check_login(self):
        sql = "SELECT login FROM human "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data



