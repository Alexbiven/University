import pymysql
from pymysql.cursors import DictCursor


class DataBase:

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

    def search_personal_infoS(self, login):
        sql = f"SELECT * FROM progress WHERE login = '{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def search_personal_infoT(self, name, surname):
        sql = f"SELECT * FROM progress WHERE name = '{name}' and surname = '{surname}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        if data != ():
            user = data[0]
            if user['name'] == name and user['surname'] == surname:
                print('Студент:', user['name'], user['surname'], 'Курс: ', user['course'],
                      'Математика: ', user['maths'], 'Физика: ', user['physics'],
                      'Информатика: ', user['informatics'], 'Литература: ', user['literature'],
                      'Философия: ', user['philosophy'], 'Средний балл: ', user['average_ball'])
        else:
            print('There is no such User')
            my_info = DataBase()
            my_info.search_personal_infoT(input('Введите имя: '),input('Введите фамилию: '))

    def search_general_infoS(self):
        sql = "SELECT * FROM progress "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        for user in data:
            print('Студент:',user['name'],user['surname'],
                  'Курс:',user['course'], 'Средний балл:',user['average_ball'])

    def search_general_infoT(self):
        sql = "SELECT * FROM progress "
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        for user in data:
            print('Студент:',user['name'],user['surname'],'Курс: ',user['course'],
                  'Математика: ',user['maths'],'Физика: ',user['physics'],
                  'Информатика: ',user['informatics'],'Литература: ',user['literature'],
                  'Философия: ',user['philosophy'],'Средний балл: ',user['average_ball'])

    def edit_information(self, surname, name, discipline, mark):
        sql = f"UPDATE progress SET {discipline} = (%s) WHERE surname = (%s) and name = (%s) "
        temp = [mark,surname,name]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def average_ball(self):
        sql = "UPDATE progress SET average_ball = (maths+physics+informatics+literature+philosophy)/5;"
        self.cursors.execute(sql)
        self.connection.commit()

    def update_course(self, surname, name, course):
        sql = f"UPDATE progress SET course = '{course}' WHERE surname = '{surname}' and name = '{name}'"
        self.cursors.execute(sql)
        self.connection.commit()

    def update_status(self, surname, name, status):
        sql = f"UPDATE human SET status = '{status}' WHERE surname = '{surname}' and name = '{name}'"
        self.cursors.execute(sql)
        self.connection.commit()


