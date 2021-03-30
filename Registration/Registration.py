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



    def addUser(self, name,surname,login, password,status):
        sql = 'INSERT INTO human (id,name,surname, login, password,status) VALUES (%s, %s, %s, %s, %s, %s)'
        temp = ['NULL', name,surname,login, password,status]
        password.replace('a', 'e').replace('c', 'r')
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUsers(self):
        sql = "SELECT * FROM human"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        for element in data:
            print('Имя: ' + element['name'],'Фамилия: ' + element['surname'],'Пароль: ' + element['login'])




# my_Registration = Registration()
# my_Registration.addUser(input('Введите имя: '),input('Введите фамилию: '),input('Введите логин: '),
#                             input('Введите пароль: '), input('Введите статус: '))
# my_Registration = Registration()
# my_Registration.getUsers()